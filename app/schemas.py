from pydantic import BaseModel
from typing import Optional

class UserProfileSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    skills: Optional[str]
    projects: Optional[str]
    experience: Optional[str]

    class Config:
        from_attributes = True
