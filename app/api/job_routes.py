from fastapi import APIRouter
from app.models.job import Job

router = APIRouter(prefix="/jobs", tags=["Jobs"])

# Temporary in-memory storage
jobs: list[Job] = []


@router.post("/")
def create_job(job: Job):
    job.id = len(jobs) + 1
    jobs.append(job)

    return {
        "message": "Job created successfully",
        "job": job
    }


@router.get("/")
def get_jobs():
    return {
        "total": len(jobs),
        "jobs": jobs
    }
