"""
Authentication and user management system.
Supports Google OAuth for IIT KGP domain, JWT tokens, and password reset.
"""
import os
import jwt
import secrets
from datetime import datetime, timedelta
from typing import Optional
from pathlib import Path
from dataclasses import dataclass, asdict
import json
import hashlib

from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
import requests


# ── Configuration ───────────────────────────────────────────────────────────
ALLOWED_DOMAIN = "@kgpian.itkgp.ac.in"
JWT_SECRET = os.getenv("JWT_SECRET", "coastal-hydrodynamics-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ── Data Models ─────────────────────────────────────────────────────────────

@dataclass
class User:
    """User account information."""
    user_id: str
    email: str
    full_name: str
    department: str = "Civil Engineering"
    roll_number: Optional[str] = None
    created_at: str = None
    last_login: Optional[str] = None
    is_verified: bool = False
    google_id: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()


@dataclass
class PasswordReset:
    """Password reset request."""
    email: str
    token: str
    created_at: str
    expires_at: str
    used: bool = False


class LoginRequest(BaseModel):
    email: str
    password: str


class SignupRequest(BaseModel):
    email: str
    password: str
    full_name: str
    roll_number: Optional[str] = None


class GoogleAuthRequest(BaseModel):
    id_token: str
    access_token: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


# ── Password Management ──────────────────────────────────────────────────────

def hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash."""
    return pwd_context.verify(plain_password, hashed_password)


def generate_reset_token() -> str:
    """Generate a secure password reset token."""
    return secrets.token_urlsafe(32)


# ── JWT Token Management ─────────────────────────────────────────────────────

def create_access_token(user_id: str, email: str, expires_in_hours: int = JWT_EXPIRY_HOURS) -> str:
    """Create JWT access token."""
    expires_at = datetime.utcnow() + timedelta(hours=expires_in_hours)
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": expires_at,
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def verify_access_token(token: str) -> dict:
    """Verify and decode JWT token."""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}


# ── Domain Validation ────────────────────────────────────────────────────────

def is_valid_iit_kgp_email(email: str) -> bool:
    """Check if email is from IIT KGP domain."""
    return email.lower().endswith(ALLOWED_DOMAIN)


def extract_roll_number_from_email(email: str) -> Optional[str]:
    """Extract roll number from IIT KGP email format."""
    if is_valid_iit_kgp_email(email):
        # Format: rollnumber@kgpian.itkgp.ac.in
        local_part = email.split("@")[0]
        return local_part
    return None


# ── Google OAuth Verification ───────────────────────────────────────────────

def verify_google_token(id_token: str, google_client_id: str) -> dict:
    """
    Verify Google ID token.
    
    Args:
        id_token: Google JWT ID token
        google_client_id: Your Google OAuth client ID
        
    Returns:
        Decoded token payload if valid, empty dict otherwise
    """
    try:
        # Verify token with Google's public keys
        from google.auth.transport import requests as google_requests
        from google.oauth2 import id_token as google_id_token
        
        request = google_requests.Request()
        idinfo = google_id_token.verify_oauth2_token(id_token, request, google_client_id)
        
        # Check if email is from IIT KGP domain
        email = idinfo.get("email", "")
        if not is_valid_iit_kgp_email(email):
            return {"error": f"Email domain not allowed. Only {ALLOWED_DOMAIN} emails accepted."}
        
        return idinfo
    except Exception as e:
        return {"error": str(e)}


# ── User Storage (File-based) ────────────────────────────────────────────────

class UserDatabase:
    """Simple file-based user database."""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.users_dir = data_dir / "users"
        self.passwords_dir = data_dir / "passwords"
        self.resets_dir = data_dir / "password_resets"
        
        self.users_dir.mkdir(parents=True, exist_ok=True)
        self.passwords_dir.mkdir(parents=True, exist_ok=True)
        self.resets_dir.mkdir(parents=True, exist_ok=True)
    
    def user_exists(self, email: str) -> bool:
        """Check if user exists."""
        user_file = self.users_dir / f"{self._email_to_filename(email)}.json"
        return user_file.exists()
    
    def create_user(self, email: str, password: str, full_name: str, roll_number: Optional[str] = None) -> User:
        """Create a new user."""
        if self.user_exists(email):
            raise ValueError(f"User with email {email} already exists")
        
        if not is_valid_iit_kgp_email(email):
            raise ValueError(f"Email must be from {ALLOWED_DOMAIN} domain")
        
        user = User(
            user_id=self._generate_user_id(),
            email=email,
            full_name=full_name,
            roll_number=roll_number or extract_roll_number_from_email(email),
            department="Civil Engineering"
        )
        
        # Save user
        self._save_user_file(user)
        
        # Save password hash
        self._save_password(email, password)
        
        return user
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        user_file = self.users_dir / f"{self._email_to_filename(email)}.json"
        if user_file.exists():
            data = json.loads(user_file.read_text())
            return User(**data)
        return None
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        for user_file in self.users_dir.glob("*.json"):
            data = json.loads(user_file.read_text())
            if data.get("user_id") == user_id:
                return User(**data)
        return None
    
    def update_user(self, user: User) -> None:
        """Update user information."""
        self._save_user_file(user)
    
    def verify_password(self, email: str, password: str) -> bool:
        """Verify user password."""
        pwd_file = self.passwords_dir / f"{self._email_to_filename(email)}.txt"
        if not pwd_file.exists():
            return False
        
        hashed = pwd_file.read_text()
        return verify_password(password, hashed)
    
    def set_password(self, email: str, password: str) -> None:
        """Set user password (for password reset)."""
        self._save_password(email, password)
    
    def create_password_reset_request(self, email: str) -> str:
        """Create password reset request and return token."""
        if not self.user_exists(email):
            raise ValueError(f"User with email {email} not found")
        
        token = generate_reset_token()
        reset = PasswordReset(
            email=email,
            token=token,
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() + timedelta(hours=1)).isoformat(),
            used=False
        )
        
        reset_file = self.resets_dir / f"{token}.json"
        reset_file.write_text(json.dumps(asdict(reset), indent=2))
        
        return token
    
    def verify_reset_token(self, token: str) -> Optional[str]:
        """Verify reset token and return email if valid."""
        reset_file = self.resets_dir / f"{token}.json"
        if not reset_file.exists():
            return None
        
        data = json.loads(reset_file.read_text())
        reset = PasswordReset(**data)
        
        # Check if expired or already used
        if datetime.fromisoformat(reset.expires_at) < datetime.now():
            return None
        if reset.used:
            return None
        
        return reset.email
    
    def mark_reset_used(self, token: str) -> None:
        """Mark reset token as used."""
        reset_file = self.resets_dir / f"{token}.json"
        if reset_file.exists():
            data = json.loads(reset_file.read_text())
            data["used"] = True
            reset_file.write_text(json.dumps(data, indent=2))
    
    def get_user_stats(self, email: str) -> dict:
        """Get user statistics and profile info."""
        user = self.get_user_by_email(email)
        if not user:
            return {}
        
        return {
            "user_id": user.user_id,
            "email": user.email,
            "full_name": user.full_name,
            "roll_number": user.roll_number,
            "department": user.department,
            "created_at": user.created_at,
            "last_login": user.last_login,
            "is_verified": user.is_verified
        }
    
    # Private helpers
    
    def _email_to_filename(self, email: str) -> str:
        """Convert email to safe filename."""
        return hashlib.sha256(email.lower().encode()).hexdigest()[:16]
    
    def _generate_user_id(self) -> str:
        """Generate unique user ID."""
        return secrets.token_urlsafe(16)
    
    def _save_user_file(self, user: User) -> None:
        """Save user to file."""
        filename = self._email_to_filename(user.email)
        user_file = self.users_dir / f"{filename}.json"
        user_file.write_text(json.dumps(asdict(user), indent=2))
    
    def _save_password(self, email: str, password: str) -> None:
        """Save password hash."""
        filename = self._email_to_filename(email)
        pwd_file = self.passwords_dir / f"{filename}.txt"
        hashed = hash_password(password)
        pwd_file.write_text(hashed)
