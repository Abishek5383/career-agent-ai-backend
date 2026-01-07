from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/health")
def health():
    return {
        "status": "OK",
        "message": "Backend is running perfectly 🚀"
    }
