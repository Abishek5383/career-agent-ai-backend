LEARNING_RESOURCES = {
    "python": {
        "roadmap": ["Basics", "OOP", "Modules", "APIs"],
        "websites": [
            "https://docs.python.org",
            "https://realpython.com"
        ],
        "youtube": [
            "https://www.youtube.com/@freecodecamp"
        ]
    },
    "fastapi": {
        "roadmap": ["REST APIs", "CRUD", "Auth", "Deployment"],
        "websites": [
            "https://fastapi.tiangolo.com"
        ],
        "youtube": [
            "https://www.youtube.com/@freecodecamp"
        ]
    },
    "machine learning": {
        "roadmap": ["Math", "Algorithms", "Projects"],
        "websites": [
            "https://scikit-learn.org"
        ],
        "youtube": [
            "https://www.youtube.com/@krishnaik06"
        ]
    }
}

def generate_roadmap(missing_skills: list[str]):
    roadmap = {}

    for skill in missing_skills:
        roadmap[skill] = LEARNING_RESOURCES.get(
            skill,
            {
                "roadmap": ["Basics", "Practice", "Projects"],
                "websites": ["https://www.google.com"],
                "youtube": ["https://www.youtube.com"]
            }
        )

    return roadmap
