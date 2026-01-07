from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Dict

from app.db.database import get_db
from app.db.models import UserProfile

router = APIRouter(
    prefix="/profile",
    tags=["User Profile"]
)

class ProfileRequest(BaseModel):
    name: str
    skills: List[str]
    projects: str
    experience: str
    job_role: str
    missing_skills: List[str]
    roadmap: Dict

@router.post("/save")
def save_profile(data: ProfileRequest, db: Session = Depends(get_db)):
    profile = UserProfile(
        name=data.name,
        skills=data.skills,
        projects=data.projects,
        experience=data.experience,
        job_role=data.job_role,
        missing_skills=data.missing_skills,
        roadmap=data.roadmap
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return {
        "message": "Profile saved successfully ✅",
        "profile_id": profile.id
    }

@router.get("/{profile_id}")
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()

    if not profile:
        return {"error": "Profile not found"}

    return profile
