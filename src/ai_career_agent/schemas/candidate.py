from pydantic import BaseModel


class CandidatePreferences(BaseModel):
    minimum_salary: int | None = None
    preferred_work_arrangement: str | None = None
    maximum_travel_percent: int | None = None


class CandidateProfileCreate(BaseModel):
    name: str
    headline: str
    summary: str
    skills: list[str]
    target_roles: list[str]
    location: str | None = None
    preferences: CandidatePreferences | None = None

class CandidateProfileResponse(CandidateProfileCreate):
    id: int
