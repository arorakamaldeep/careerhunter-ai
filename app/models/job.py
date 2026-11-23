
from typing import Optional

from pydantic import BaseModel, Field


class Job(BaseModel):
    id: Optional[int] = None

    title: str
    company: str
    location: str

    salary_min: Optional[float] = None
    salary_max: Optional[float] = None

    experience_years: Optional[int] = None

    skills: list[str] = Field(default_factory=list)

    job_url: Optional[str] = None
    job_type: Optional[str] = None
