from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills

router = APIRouter(
    prefix="/resume",
    tags=["Resume Analyzer"]
)

@router.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    text = extract_text_from_pdf(file)

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    name = lines[0] if lines else "NIL"

    skills = extract_skills(text)
    skills_output = skills if skills else ["NIL"]

    projects = "Mentioned" if "project" in text.lower() else "NIL"
    experience = "Mentioned" if "experience" in text.lower() else "NIL"

    return {
        "name": name,
        "skills": skills_output,
        "projects": projects,
        "experience": experience
    }
