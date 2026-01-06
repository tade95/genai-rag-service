GenAI RAG Service – Production-Ready Data Product
Overview

This project implements a production-ready GenAI data product that enables users to query internal documents using a Retrieval-Augmented Generation (RAG) approach.

The service is designed as a scalable backend API, emphasizing software engineering best practices, MLOps principles, and platform-level concerns such as observability, infrastructure as code, and CI/CD.

It reflects how GenAI solutions are built, deployed, and operated in real-world environments.

Problem Statement

Teams often struggle to extract actionable knowledge from large volumes of internal documentation.

This project addresses that problem by providing:

A backend API to ingest documents

A GenAI-powered question-answering interface

A production-oriented architecture suitable for cloud environments

Key Features

RAG-based GenAI pipeline

Document ingestion

Embedding generation

Semantic retrieval

Context-aware LLM responses

Backend API

RESTful API built with FastAPI

Clear separation of concerns

Health check endpoint for platform monitoring

Production Engineering

Containerized with Docker

Infrastructure defined using Terraform

CI/CD pipeline for build and validation

Environment-based configuration

Observability (Lightweight)

Structured JSON logging

Request-level metrics (latency, errors)

Designed to integrate with cloud-native monitoring tools


Tech Stack
Layer	Technology
Cloud	Google Cloud Platform (Cloud Run)
Backend	Python, FastAPI
GenAI	Retrieval-Augmented Generation (RAG)
Infrastructure	Terraform
CI/CD	GitHub Actions
Containers	Docker
Observability	Structured logging, basic metrics



API Endpoints
POST /ingest

Ingests and indexes documents for later retrieval.

Request

{
  "documents": ["doc1 text", "doc2 text"]
}



POST /ask

Executes a semantic search and generates an answer using retrieved context.

Request

{
  "question": "What is the onboarding process?"
}

GET /health

Health check endpoint for monitoring and orchestration systems.


Infrastructure & Deployment

The service is designed to run on Google Cloud Run, providing:

Fully managed scalability

Stateless container execution

Secure service-to-service authentication

Infrastructure is defined using Terraform, enabling:

Reproducible environments

Clear separation between infrastructure and application logic

Easy promotion across environments (dev/staging/prod)



CI/CD Pipeline

The CI pipeline includes:

Code linting and formatting

Basic unit tests

Docker image build

This setup enforces consistent engineering standards and enables rapid iteration.

MLOps & GenAI Considerations

Prompt versioning to ensure reproducibility

Embedding version control for traceability

Clear separation between ingestion and query pipelines

Designed to support experimentation and evaluation frameworks

Observability & Reliability

The application emits:

Structured logs for request tracing

Latency and error metrics per endpoint

This allows seamless integration with cloud monitoring, alerting, and incident response workflows.

Future Improvements

Add model and embedding registry (e.g. MLflow)

Integrate distributed tracing

Support batch ingestion pipelines (Airflow)

Implement A/B testing for prompts and retrieval strategies

Add authentication and rate limiting