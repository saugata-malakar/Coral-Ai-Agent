"""
Authentication routes for login, signup, and password management.
Integrates Google OAuth with IIT KGP domain restriction.
"""
import os
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr

from .config import DATA_DIR
from .auth import (
    UserDatabase,
    LoginRequest,
    SignupRequest,
    GoogleAuthRequest,
    TokenResponse,
    create_access_token,
    verify_access_token,
    verify_google_token,
    is_valid_iit_kgp_email,
    extract_roll_number_from_email
)

router = APIRouter(prefix="/auth", tags=["authentication"])

# Initialize user database
user_db = UserDatabase(DATA_DIR)

# Google OAuth configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")


# ── Request/Response Models ─────────────────────────────────────────────────

class SignupResponse(BaseModel):
    message: str
    user: dict


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict


class PasswordResetRequest(BaseModel):
    email: str


class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str


class UserProfile(BaseModel):
    user_id: str
    email: str
    full_name: str
    roll_number: Optional[str] = None
    department: str
    created_at: str


# ── Dependencies ────────────────────────────────────────────────────────────

async def get_current_user(token: str) -> dict:
    """Extract current user from JWT token."""
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    
    payload = verify_access_token(token)
    if "error" in payload:
        raise HTTPException(status_code=401, detail=payload["error"])
    
    return payload


# ── Endpoints ───────────────────────────────────────────────────────────────

@router.post("/signup", response_model=SignupResponse)
def signup(req: SignupRequest):
    """
    Create new user account (IIT KGP domain only).
    
    Args:
        email: Must be @kgpian.itkgp.ac.in
        password: Strong password
        full_name: User's full name
        roll_number: Optional IIT KGP roll number
        
    Returns:
        User info and confirmation message
    """
    if not is_valid_iit_kgp_email(req.email):
        raise HTTPException(
            status_code=400,
            detail="Only IIT KGP email (@kgpian.iitkgp.ac.in or @kgpian.itkgp.ac.in) or demo accounts allowed"
        )
    
    if len(req.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters"
        )
    
    try:
        user = user_db.create_user(
            email=req.email,
            password=req.password,
            full_name=req.full_name,
            roll_number=req.roll_number
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return SignupResponse(
        message="Account created successfully. Welcome to Coral!",
        user={
            "user_id": user.user_id,
            "email": user.email,
            "full_name": user.full_name,
            "roll_number": user.roll_number,
            "department": user.department
        }
    )


@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    """
    Login with email and password.
    Returns JWT access token.
    """
    user = user_db.get_user_by_email(req.email)
    if not user or not user_db.verify_password(req.email, req.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Create JWT token
    token = create_access_token(user.user_id, user.email)
    
    # Update last login
    user.last_login = datetime.now().isoformat()
    user_db.update_user(user)
    
    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user={
            "user_id": user.user_id,
            "email": user.email,
            "full_name": user.full_name,
            "roll_number": user.roll_number,
            "department": user.department
        }
    )


@router.post("/google-auth", response_model=LoginResponse)
def google_auth(req: GoogleAuthRequest):
    """
    Authenticate with Google OAuth token (IIT KGP domain only).
    
    Args:
        id_token: Google JWT ID token
        access_token: Google access token
        
    Returns:
        JWT access token or new user created
    """
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google OAuth not configured")
    
    # Verify Google token
    idinfo = verify_google_token(req.id_token, GOOGLE_CLIENT_ID)
    if "error" in idinfo:
        raise HTTPException(status_code=401, detail=idinfo["error"])
    
    email = idinfo.get("email", "")
    given_name = idinfo.get("given_name", "")
    family_name = idinfo.get("family_name", "")
    picture = idinfo.get("picture", "")
    google_id = idinfo.get("sub", "")
    
    # Check if user exists
    user = user_db.get_user_by_email(email)
    
    if not user:
        # Create new user from Google OAuth
        full_name = f"{given_name} {family_name}".strip()
        roll_number = extract_roll_number_from_email(email)
        
        user = user_db.create_user(
            email=email,
            password=google_id,  # Use Google ID as password
            full_name=full_name,
            roll_number=roll_number
        )
        
        user.google_id = google_id
        user.avatar_url = picture
        user.is_verified = True
        user_db.update_user(user)
    else:
        # Update existing user
        user.last_login = datetime.now().isoformat()
        user.google_id = google_id
        if picture:
            user.avatar_url = picture
        user_db.update_user(user)
    
    # Create JWT token
    token = create_access_token(user.user_id, user.email)
    
    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user={
            "user_id": user.user_id,
            "email": user.email,
            "full_name": user.full_name,
            "roll_number": user.roll_number,
            "department": user.department
        }
    )


@router.get("/profile", response_model=UserProfile)
def get_profile(token: str):
    """Get current user profile."""
    payload = verify_access_token(token)
    if "error" in payload:
        raise HTTPException(status_code=401, detail=payload["error"])
    
    user = user_db.get_user_by_id(payload["user_id"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserProfile(
        user_id=user.user_id,
        email=user.email,
        full_name=user.full_name,
        roll_number=user.roll_number,
        department=user.department,
        created_at=user.created_at
    )


@router.post("/forgot-password")
def forgot_password(req: PasswordResetRequest):
    """
    Request password reset.
    Sends reset token (in production, email this to user).
    """
    user = user_db.get_user_by_email(req.email)
    if not user:
        # Don't reveal if email exists (security best practice)
        return {"message": "If account exists, reset link will be sent"}
    
    token = user_db.create_password_reset_request(req.email)
    
    # TODO: In production, send this via email
    # For now, return for demo (in production, never return token to user)
    return {
        "message": "Password reset token created",
        "reset_token": token  # ONLY FOR DEVELOPMENT - remove in production
    }


@router.post("/reset-password")
def reset_password(req: PasswordResetConfirm):
    """
    Reset password using reset token.
    """
    email = user_db.verify_reset_token(req.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired reset token")
    
    if len(req.new_password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters"
        )
    
    # Update password
    user_db.set_password(email, req.new_password)
    user_db.mark_reset_used(req.token)
    
    return {"message": "Password reset successfully"}


@router.get("/validate-token")
def validate_token(token: str):
    """Validate if token is still active."""
    payload = verify_access_token(token)
    if "error" in payload:
        return {"valid": False, "error": payload["error"]}
    
    return {"valid": True, "user_id": payload.get("user_id")}


@router.get("/google-client-id")
def get_google_client_id():
    """Get the configured Google Client ID for OAuth."""
    return {"client_id": GOOGLE_CLIENT_ID}


# Add datetime import
from datetime import datetime
