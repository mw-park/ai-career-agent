# Architecture

## Purpose

AI Career Agent is a persistent, context-aware application that discovers, evaluates, tracks, and helps users act on career opportunities.

The architecture will evolve incrementally as new capabilities create a need for additional technology.

## Current Architecture

The application is currently a minimal Python web API.

```text
Client / Swagger
       |
       v
    FastAPI
       |
       v
  Health Endpoint
