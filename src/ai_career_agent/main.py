from fastapi import FastAPI
from ai_career_agent.schemas.job import JobCreate, JobResponse
from ai_career_agent.schemas.candidate import CandidateProfileCreate, CandidateProfileResponse

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/jobs", response_model=JobResponse, status_code=201)
def create_job(job: JobCreate):
    return JobResponse(id=1, **job.model_dump())

@app.post("/candidates", response_model=CandidateProfileResponse, status_code=201)
def create_candidate(candidate: CandidateProfileCreate):
    return CandidateProfileResponse(id=1, **candidate.model_dump())

