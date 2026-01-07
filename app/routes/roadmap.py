from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.skill_gap import find_skill_gap
from app.services.roadmap_generator import generate_roadmap

router = APIRouter(
    prefix="/roadmap",
    tags=["Skill Gap & Roadmap"]
)

class RoadmapRequest(BaseModel):
    skills: List[str]
    job_role: str

@router.post("/generate")
def generate_learning_roadmap(data: RoadmapRequest):
    gap = find_skill_gap(data.skills, data.job_role)
    roadmap = generate_roadmap(gap["missing_skills"])

    return {
        "job_role": gap["job_role"],
        "current_skills": data.skills,
        "missing_skills": gap["missing_skills"],
        "learning_roadmap": roadmap
    }
