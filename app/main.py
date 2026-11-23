
from fastapi import FastAPI

from app.api.job_routes import router as job_router

app = FastAPI(
    title="CareerHunter AI",
    description="An AI-powered job discovery and matching platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareerHunter AI",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CareerHunter AI"
    }


# Register Job API
app.include_router(job_router)
