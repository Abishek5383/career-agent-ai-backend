from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routes.health import router as health_router
from app.routes.resume import router as resume_router
from app.routes.roadmap import router as roadmap_router
from app.routes.profile import router as profile_router
from app.routes.jobs import router as jobs_router
from app.routes.apply import router as apply_router


app = FastAPI(
    title="Career Agent AI",
    version="1.0.0"
)

# ✅ Create DB tables
Base.metadata.create_all(bind=engine)

# ✅ CORS (Frontend + Cloud safe)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(health_router)
app.include_router(resume_router)
app.include_router(roadmap_router)
app.include_router(profile_router)
app.include_router(jobs_router)
app.include_router(apply_router)






@app.get("/")
def root():
    return {"message": "Career Agent AI Backend is Live 🔥"}
