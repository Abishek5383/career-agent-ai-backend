from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from datetime import datetime

from app.db.database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    skills = Column(JSON, nullable=True)
    projects = Column(String, nullable=True)
    experience = Column(String, nullable=True)
    job_role = Column(String, nullable=True)
    missing_skills = Column(JSON, nullable=True)
    roadmap = Column(JSON, nullable=True)


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)
    website = Column(String, nullable=True)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    required_skills = Column(JSON, nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"))


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_profile_id = Column(Integer, ForeignKey("user_profiles.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    applied_at = Column(DateTime, default=datetime.utcnow)
