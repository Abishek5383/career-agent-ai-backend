from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from app.db.database import get_db
from app.db.models import JobApplication

router = APIRouter(
    prefix="/apply",
    tags=["Job Applications"]
)

class ApplyRequest(BaseModel):
    user_profile_id: int
    job_ids: List[int]  # one or many

@router.post("/")
def apply_jobs(data: ApplyRequest, db: Session = Depends(get_db)):
    applied_jobs = []

    for job_id in data.job_ids:
        application = JobApplication(
            user_profile_id=data.user_profile_id,
            job_id=job_id
        )
        db.add(application)
        applied_jobs.append(job_id)

    db.commit()

    return {
        "message": "Applied successfully ✅",
        "jobs_applied": applied_jobs
    }

@router.get("/user/{user_id}")
def get_user_applications(user_id: int, db: Session = Depends(get_db)):
    return db.query(JobApplication).filter(
        JobApplication.user_profile_id == user_id
    ).all()
