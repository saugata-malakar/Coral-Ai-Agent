"""
User profile and personalization system.
Tracks user learning history, preferences, and adapts responses accordingly.
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class UserProfile:
    """User learning profile and preferences."""
    user_id: str
    created_at: str
    updated_at: str
    expertise_level: str = "beginner"  # beginner, intermediate, advanced
    preferred_format: str = "detailed"  # brief, detailed, mathematical
    preferred_thinking_mode: str = "standard"
    topics_of_interest: list[str] = None
    interaction_count: int = 0
    last_topics: list[str] = None  # Recent topics asked about
    
    def __post_init__(self):
        if self.topics_of_interest is None:
            self.topics_of_interest = []
        if self.last_topics is None:
            self.last_topics = []


@dataclass
class UserInteraction:
    """Record of a user-model interaction."""
    timestamp: str
    user_id: str
    question: str
    thinking_mode: str
    topic_tags: list[str]
    answer_length: int
    rating: Optional[int] = None  # 1-5 star rating
    feedback: Optional[str] = None


class UserProfileManager:
    """Manage user profiles and learning history."""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.profiles_dir = data_dir / "user_profiles"
        self.interactions_dir = data_dir / "interactions"
        
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.interactions_dir.mkdir(parents=True, exist_ok=True)
    
    def get_profile(self, user_id: str) -> UserProfile:
        """Load or create user profile."""
        profile_path = self.profiles_dir / f"{user_id}.json"
        
        if profile_path.exists():
            data = json.loads(profile_path.read_text())
            return UserProfile(**data)
        
        # Create new profile
        now = datetime.now().isoformat()
        profile = UserProfile(
            user_id=user_id,
            created_at=now,
            updated_at=now
        )
        self.save_profile(profile)
        return profile
    
    def save_profile(self, profile: UserProfile) -> None:
        """Save user profile."""
        profile.updated_at = datetime.now().isoformat()
        profile_path = self.profiles_dir / f"{profile.user_id}.json"
        profile_path.write_text(json.dumps(asdict(profile), indent=2))
    
    def update_expertise_level(self, user_id: str, level: str) -> None:
        """Update user expertise level based on interactions."""
        profile = self.get_profile(user_id)
        valid_levels = ["beginner", "intermediate", "advanced"]
        if level in valid_levels:
            profile.expertise_level = level
            self.save_profile(profile)
    
    def record_interaction(
        self,
        user_id: str,
        question: str,
        thinking_mode: str,
        topic_tags: list[str],
        answer_length: int,
        rating: Optional[int] = None,
        feedback: Optional[str] = None
    ) -> None:
        """Record a user interaction."""
        interaction = UserInteraction(
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            question=question,
            thinking_mode=thinking_mode,
            topic_tags=topic_tags,
            answer_length=answer_length,
            rating=rating,
            feedback=feedback
        )
        
        # Save interaction
        filename = f"{user_id}_{interaction.timestamp.replace(':', '-')}.json"
        path = self.interactions_dir / filename
        path.write_text(json.dumps(asdict(interaction), indent=2))
        
        # Update profile
        profile = self.get_profile(user_id)
        profile.interaction_count += 1
        
        # Update topics
        profile.last_topics = (topic_tags + profile.last_topics)[:10]
        profile.topics_of_interest = list(set(
            profile.topics_of_interest + topic_tags
        ))
        
        self.save_profile(profile)
    
    def get_expertise_adjusted_prompt(self, user_id: str, base_prompt: str) -> str:
        """Adjust prompt based on user expertise level."""
        profile = self.get_profile(user_id)
        
        if profile.expertise_level == "beginner":
            adjustment = "\n\nAdapt your explanation for BEGINNERS: Use simple language, explain all terminology, provide step-by-step reasoning."
        elif profile.expertise_level == "advanced":
            adjustment = "\n\nAdapt your explanation for ADVANCED users: Use technical terminology, focus on derivations and mathematical rigor."
        else:
            adjustment = "\n\nAdapt your explanation for INTERMEDIATE users: Balance accessibility with technical depth."
        
        return base_prompt + adjustment
    
    def get_interaction_history(self, user_id: str, limit: int = 10) -> list[dict]:
        """Get recent interaction history for a user."""
        interactions = []
        for file in sorted(
            self.interactions_dir.glob(f"{user_id}_*.json"),
            reverse=True
        )[:limit]:
            data = json.loads(file.read_text())
            interactions.append(data)
        return interactions
    
    def get_learning_stats(self, user_id: str) -> dict:
        """Get learning statistics for a user."""
        profile = self.get_profile(user_id)
        history = self.get_interaction_history(user_id, limit=100)
        
        avg_rating = None
        if history:
            ratings = [h.get("rating") for h in history if h.get("rating")]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
        
        return {
            "total_interactions": profile.interaction_count,
            "expertise_level": profile.expertise_level,
            "main_topics": profile.topics_of_interest[:5],
            "recent_topics": profile.last_topics[:5],
            "average_rating": avg_rating,
            "preferred_format": profile.preferred_format,
            "preferred_thinking_mode": profile.preferred_thinking_mode
        }


def create_user_profile_tool():
    """Create tool for managing user preferences."""
    from langchain_core.tools import tool
    
    @tool
    def update_learning_preference(
        preference_type: str,
        value: str
    ) -> str:
        """
        Update user learning preferences.
        
        Supported preferences:
        - expertise_level: beginner, intermediate, advanced
        - format: brief, detailed, mathematical
        - thinking_mode: standard, deep, critical, analytical, comprehensive
        
        Args:
            preference_type: Type of preference to update
            value: New preference value
            
        Returns:
            Confirmation message
        """
        valid_preferences = {
            "expertise_level": ["beginner", "intermediate", "advanced"],
            "format": ["brief", "detailed", "mathematical"],
            "thinking_mode": ["standard", "deep", "critical", "analytical", "comprehensive"]
        }
        
        if preference_type not in valid_preferences:
            return f"Unknown preference type. Valid: {list(valid_preferences.keys())}"
        
        if value not in valid_preferences[preference_type]:
            return f"Invalid {preference_type}. Valid options: {valid_preferences[preference_type]}"
        
        return f"✓ Updated {preference_type} to '{value}'"
    
    return update_learning_preference
