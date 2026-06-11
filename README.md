#  Healthcare Interoperability Assistant

An AI-powered Retrieval-Augmented Generation (RAG) and Agent-based system designed to help healthcare IT engineers understand, navigate, and apply healthcare interoperability standards, terminology systems, and regulatory requirements (HL7, FHIR, IHE, DICOM, openEHR, ISiK, ISO 27001, GDPR, etc.).



##  Overview

The goal of this project is to apply modern AI engineering concepts by building an end-to-end LLM application that combines Retrieval-Augmented Generation (RAG), agent-based orchestration, and healthcare interoperability knowledge.

The system is designed to:

- Ingest and retrieve healthcare interoperability knowledge
- Provide context-aware answers grounded in source documentation
- Use tools and agents to solve interoperability-related tasks
- Evaluate response quality and retrieval performance
- Provide an API and user interface for interaction
- Support observability, monitoring, and user feedback collection


## Problem Statement

Healthcare interoperability knowledge is fragmented across multiple standards organizations, implementation guides, technical specifications, and regulatory documents.

Engineers frequently need to:

- Search through large volumes of documentation
- Understand relationships between standards
- Convert concepts across different interoperability frameworks
- Troubleshoot integration issues
- Validate implementation approaches

This project aims to build an end-to-end AI assistant that combines retrieval, reasoning, and domain-specific tools to provide accurate and actionable guidance.

## Scope

The initial project scope focuses on the following standards and terminology systems.

### Interoperability Standards

- FHIR R3 and FHIR R4
- US Core
- HL7 v2
- C-CDA

### Terminology Systems

- SNOMED CT
- LOINC
- RxNorm

### Future Expansion

- IHE Profiles
- DICOM
- openEHR
- ISiK
- ISO 27001
- ISO 27799
- GDPR
- MDR


## Key Features

### Standards Knowledge Assistant

Ask questions about:

- HL7 v2 messaging
- FHIR R4 resources and profiles
- US Core implementation guidance
- C-CDA documents
- Terminology standards and coding systems

### Cross-Standard Mapping

Understand how concepts translate across standards:

- HL7 v2 → FHIR
- C-CDA → FHIR
- Terminology mapping and normalization
- Resource and message transformations

### Integration Guidance

Receive recommendations for:

- System integration patterns
- Healthcare API design
- Event-driven interoperability
- Data exchange workflows

### Compliance and Security Insights

Understand healthcare regulatory requirements:

- GDPR
- ISO 27001
- ISO 27799
- Healthcare security best practices

### Troubleshooting Assistant

Debug interoperability issues including:

- HL7 parsing errors
- FHIR validation problems
- Mapping inconsistencies
- Terminology mismatches


## High-Level Architecture

```text
User / API / UI
        │
        ▼
+----------------------+
|  FastAPI Application |
+----------------------+
           │
           ▼
+----------------------+
|   Input Guardrails   |
|   (NeMo Guardrails)  |
+----------------------+
           │
           ▼
+----------------------+
|     Agent Planner    |
+----------------------+
           │
           ▼
+----------------------+
|  Agent Orchestrator  |
+----------------------+
     │        │        │
     ▼        ▼        ▼
   RAG      Tools   Direct LLM
     │
     ▼
+----------------------+
|      Qdrant          |
|   Vector Database    |
+----------------------+
     │
     ▼
Healthcare Standards
Knowledge Base
           |
           ▼
+----------------------+
|       LiteLLM        |
+----------------------+
           │
           ▼
OpenAI / Groq / Claude / Gemini

           │
           ▼
+----------------------+
|  Output Guardrails   |
|   (NeMo Guardrails)  |
+----------------------+
           │
           ▼
        Response

Observability:
LangSmith / Langfuse
```



---

## LiteLLM

LiteLLM acts as a unified gateway between the application and multiple LLM providers.

Capabilities include:

- Model abstraction
- Provider switching
- Automatic fallback
- Retry handling
- Cost tracking
- Budget controls
- Load balancing
- Response caching

The application interacts only with LiteLLM while LiteLLM manages communication with underlying providers.

### Benefits of LiteLLM

- Provides a single unified API for multiple LLM providers
- Enables easy switching between models without changing application code
- Supports automatic fallback when a provider fails
- Offers cost tracking and token usage monitoring
- Helps control spending with budgets and usage limits
- Enables caching to reduce repeated API costs and latency
- Supports load balancing across multiple LLM providers
- Centralizes API key management
- Improves reliability and uptime in production systems
- Reduces engineering complexity in multi-model AI applications

---

## Evaluation and Monitoring

The project includes:

- RAG evaluation workflows
- Agent evaluation workflows
- Prompt testing
- Retrieval quality assessment
- User feedback collection
- Application observability

Potential monitoring platforms include:

- LangSmith
- Langfuse
- Grafana


---

## Technology Stack

### LLM Layer

- LiteLLM
- OpenAI
- Groq
- Anthropic
- Gemini
- Nemo Guardrails 

### Knowledge Layer

- Qdrant (Vector Database)
- Sentence Transformers (Embeddings)
- FAISS (Local experimentation)
- SQLite (Metadata storage, optional)


### Application Layer

- FastAPI
- Python

### Monitoring

- LangSmith
- Langfuse

### Interfaces

- FastAPI API
- Streamlit  
  

### Ingestion Pipelines

- Python scripts
- Airflow
- Prefect
- Mage
- Kestra
- dlt

If a technology outside the course material is used, the project documentation will explain:

- What the technology does
- Why it was selected
- How it is used within the project

---

## Project Structure

```text
healthcare-interoperability-assistant/
│
├── src/
│   ├── main.py
│   │
│   ├── agents/
│   │   ├── agent_service.py
│   │   ├── planner.py
│   │   ├── prompts.py
│   │
│   ├── api/
│   │   ├── routes.py
│   │
│   ├── config/
│   │   ├── config.py
│   │
│   ├── llm/
│   │   ├── llm_service.py
│   │
│   ├── rag/
│   │   ├── retriever.py
│   │   ├── rag_service.py
│   │
│   ├── tools/
│   │   ├── hl7_tools.py
│   │   ├── fhir_tools.py
│   │
│   ├── guardrails/
│   │   ├── input.py
│   │   ├── output.py
│   │
│   ├── services/
│   │   ├── orchestration.py
│
├── tests/
├── evals/
├── frontend/
├── config.json
├── pyproject.toml
├── Dockerfile
└── README.md
```

---

## Prerequisites

- Python 3.11+
- OpenAI API Key and/or Groq API Key
- UV Package Manager

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd healthcare-interoperability-assistant
```

### 2. Create and activate a virtual environment

```bash
uv venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

### 5. Configure model settings

Create a `config.json` file:

```json
{
  "LLM_PROVIDER": "groq",
  "LLM_MODEL": "llama-3.3-70b-versatile",
  "EMBEDDING_PROVIDER": "huggingface",
  "EMBEDDING_MODEL": "all-MiniLM-L6-v2"
}
```

---

## Roadmap

### Phase 1

- [x] Project setup
- [ ] LiteLLM integration
- [ ] FastAPI integration
- [ ] Vector database integration
- [ ] Document ingestion pipeline

### Phase 2

- [ ] RAG implementation
- [ ] Healthcare standards knowledge base
- [ ] Retrieval evaluation

### Phase 3

- [ ] Agent planner
- [ ] Tool integration
- [ ] HL7 support
- [ ] FHIR support
- [ ] Terminology support

### Phase 4

- [ ] LangSmith observability
- [ ] Guardrails
- [ ] User feedback collection
- [ ] Docker deployment
- [ ] Cloud deployment