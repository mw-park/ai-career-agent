from pydantic import BaseModel


class JobCreate(BaseModel):
    company: str
    title: str
    description: str
    location: str | None = None
    work_arrangement: str | None = None
    travel_percent: int | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    salary_currency: str | None = None
    salary_period: str | None = None
    employment_type: str | None = None
    source: str | None = None
    source_url: str | None = None

class JobResponse(JobCreate):
    id: int
