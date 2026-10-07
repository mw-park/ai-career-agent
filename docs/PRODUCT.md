# Product

## Vision

AI Career Agent is a persistent, context-aware system that helps users discover, evaluate, track, and act on career opportunities.

The goal is not simply to recommend jobs. The system should remember what the user has already encountered, understand the user's career profile and preferences, and use that context when evaluating future opportunities.

## Core Workflow

Discover → Deduplicate → Research → Evaluate → Remember → Track → Act

## V0.1 Goal

V0.1 should answer:

> Given my candidate profile and this job, should I pursue it, and have I already dealt with this opportunity?

## V0.1 Capabilities

- Store a structured candidate profile
- Add jobs manually through the API
- Persist jobs and application history
- Detect duplicate opportunities
- Evaluate a candidate against a job using an LLM
- Produce structured evaluation results:
  - Fit score (0–100)
  - Strengths
  - Gaps
  - Disqualifiers
  - Pursue / Maybe / Pass recommendation
  - Concise reasoning
- Store evaluations for future reference

## Core Domain Objects

- Candidate Profile
- Job
- Application
- Job Evaluation

## Not V0.1

These are intentionally deferred:

- Automated job discovery/search
- Autonomous agents
- RAG / vector search
- MCP
- Web UI
- User authentication
- Cloud deployment
- Kubernetes

## Product Principles

- Remember prior opportunities and decisions
- Avoid repeatedly recommending the same jobs
- Ground recommendations in the candidate's actual profile and preferences
- Explain recommendations rather than only producing scores
- Keep AI output structured and testable
- Add automation gradually rather than making the system autonomous by default

## Evaluation Model

Job evaluation separates objective job facts, candidate preferences, and AI-generated evaluation.

### Job Facts

Examples include:

- Salary range
- Location
- Work arrangement (remote / hybrid / onsite)
- Travel percentage
- Employment type
- Job description

### Candidate Preferences

Candidate preferences define constraints and priorities used when evaluating opportunities, such as compensation requirements, acceptable travel, and preferred work arrangement.

### Evaluation Dimensions

The initial evaluation will consider:

- Interview probability
- Resume fit
- Company quality
- Technology stack
- Long-term career value

The evaluation will also produce an overall fit, strengths, gaps, disqualifiers, recommendation, and concise reasoning.

A strong overall fit does not override a candidate constraint. For example, an otherwise strong opportunity may still receive a Pass recommendation if compensation, travel, or work arrangement violates an important candidate requirement.


