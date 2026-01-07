COMMON_SKILLS = [
    "python", "java", "c++", "sql", "html", "css", "javascript",
    "react", "node", "fastapi", "django", "flask",
    "machine learning", "deep learning", "data analysis",
    "aws", "docker", "git"
]

def extract_skills(text: str):
    text_lower = text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))
