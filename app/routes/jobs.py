from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.db.models import Company, Job

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs & Companies"]
)

# ➕ Add a company
@router.post("/company")
def add_company(name: str, location: str = None, website: str = None, db: Session = Depends(get_db)):
    company = Company(name=name, location=location, website=website)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


# ➕ Add a job
@router.post("/add")
def add_job(
    title: str,
    description: str,
    required_skills: List[str],
    company_id: int,
    db: Session = Depends(get_db)
):
    job = Job(
        title=title,
        description=description,
        required_skills=required_skills,
        company_id=company_id
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


# 📄 Get all jobs
@router.get("/all")
def get_all_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()
