# AI Career Agent Roadmap

The project will evolve incrementally. Each milestone introduces new technology only when the application has a reason to need it.

## 1. Application Foundation

Build the basic Career Agent application and domain model.

- FastAPI application
- Job model and API
- Candidate profile
- Pydantic validation
- Automated tests

## 2. Persistence

Make application data survive restarts.

- PostgreSQL
- SQLAlchemy
- Alembic database migrations
- Persist jobs and candidate profiles

## 3. AI Job Evaluation

Evaluate a candidate against a job.

- LLM API integration
- Structured LLM output
- Fit score
- Strengths
- Gaps
- Disqualifiers
- Pursue / Maybe / Pass recommendation
- Store evaluations
- Prompt versioning
- Initial evaluations/tests for AI output quality

## 4. Application Tracking

Track the lifecycle of opportunities.

- Application status
- Application history
- Notes
- Exact duplicate detection
- Improved/fuzzy duplicate detection

## 5. Agent and Tools

Allow the AI to take multiple steps and use application capabilities as tools.

- Tool calling
- Application-history lookup
- Job research/search tools
- Agent orchestration
- MCP where appropriate

## 6. Knowledge and RAG

Ground evaluations and recommendations in persistent career context.

- Resume/profile knowledge
- Application history
- Embeddings
- Retrieval
- Vector search
- RAG
- RAG evaluation

## 7. Productionization

Turn the project into a deployable production-style system.

- Docker
- Docker Compose
- AWS
- ECR
- ECS/Fargate
- RDS PostgreSQL
- CI/CD with GitHub Actions
- Infrastructure as Code with Terraform
- Observability and production configuration

## 8. Infrastructure Experimentation

Explore additional infrastructure where it provides learning value.

- Kubernetes
- EKS
- Compare Kubernetes deployment with ECS/Fargate
