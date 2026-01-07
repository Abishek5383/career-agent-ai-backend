JOB_ROLE_SKILLS = {
    "backend developer": [
        "python", "sql", "fastapi", "docker", "git"
    ],
    "frontend developer": [
        "html", "css", "javascript", "react", "git"
    ],
    "data scientist": [
        "python", "sql", "machine learning", "data analysis"
    ],
    "ai engineer": [
        "python", "machine learning", "deep learning"
    ]
}

def find_skill_gap(user_skills: list[str], job_role: str):
    job_role = job_role.lower()

    required_skills = JOB_ROLE_SKILLS.get(job_role, [])

    missing_skills = [
        skill for skill in required_skills
        if skill not in user_skills
    ]

    return {
        "job_role": job_role,
        "required_skills": required_skills,
        "missing_skills": missing_skills
    }
