## Document Processing Portal – Pipeline Plan

### Audience
- Engineering, Ops, and Stakeholders who need a high‑level, visual overview of how the portal runs end‑to‑end.

### Goals
- Centralize dataset management, training, evaluation, and serving behind a single UI/API.
- Make reproducible runs with clear configs and artifacts.
- Provide observability for jobs and system health.

### Low‑Level Architecture (Components)
```mermaid
flowchart LR
  %% Frontend
  subgraph UI[Frontend (React)]
    UI1[Dashboard]
    UI2[Document Types]
    UI3[Pipeline]
    UI4[Models]
    UI5[Evaluation]
    UI6[Monitoring]
  end

  %% Backend Routers
  subgraph API[Backend (FastAPI Routers)]
    Rauth[/auth_router/]
    Rdoc[/doctype_router/]
    Rpipe[/pipeline_router/]
    Rmodel[/model_router/]
    Reveal[/evaluation_router/]
    Rmon[/monitoring_router/]
  end

  %% Services (Business Logic)
  subgraph SVC[Service Layer]
    FM[file_manager]
    JM[job_manager]
    PM[pipeline_manager]
    MT[model_trainer]
    EV[evaluator]
    DM[data_manager]
    BM[backup_manager]
    CG[config_generator]
  end

  %% Persistence & Infra
  DB[(PostgreSQL via SQLAlchemy)]
  RD[(Redis Optional)]
  LOG[(Logs)]

  %% File Storage
  subgraph FS[(Portal Data)]
    UP[uploads/]
    CK[models/checkpoints/]
    SVdir[models/serving/]
    BK[backups/]
  end

  %% Framework / Models
  FW[(FRAMEWORK_PATH)]
  BMPath[(BASE_MODEL_PATH)]

  %% Serving
  SRV[(Model Serving: vLLM/REST)]

  %% Edges
  UI --> API
  API --> SVC
  SVC <--> DB
  SVC <--> RD
  SVC --> FS
  SVC --> FW
  SVC --> BMPath
  SVC --> SRV
  SVC --> LOG
```

### Flow Chart (Operational)
```mermaid
flowchart TD
  A[Create Document Type] --> B[Upload Data / Config]
  B --> C[Start Pipeline (UI -> /pipeline)]
  C --> D[Create Job in DB]
  D --> E[Generate Train Config]
  E --> F[Run Training]
  F --> G[Write Checkpoints to models/checkpoints/<doctype>]
  G --> H[Evaluate Model]
  H --> I[Register/Expose in Models]
  I --> J[Start Serving]
  J --> K[Inference via REST]
  K --> L[Monitor + Logs]
```

### Data Flow (Happy Path)
```mermaid
sequenceDiagram
  participant User
  participant UI as Portal UI
  participant API as FastAPI
  participant FS as Storage
  participant DB as Postgres
  participant SV as Serving

  User->>UI: Upload images/configs
  UI->>API: POST /pipeline/start {doctype, config}
  API->>DB: Create Job (Queued)
  API->>FS: Read training data
  API->>FW: Generate/Run train config
  API-->>DB: Update Job (Running)
  API-->>FS: Write checkpoints
  API-->>DB: Update Job (Completed)
  User->>UI: Start Serving
  UI->>API: POST /models/{doctype}/serving/start
  API->>SV: Launch model server
  User->>UI: Inference request
  UI->>API: GET /{doctype}/inference?image=...
  API->>SV: Forward request
  SV-->>API: Prediction
  API-->>UI: Response
```

### Job Lifecycle
```mermaid
stateDiagram-v2
  [*] --> Queued
  Queued --> Running
  Running --> Completed
  Running --> Failed
  Failed --> [*]
  Completed --> [*]
```

### Environments & Configuration
- Config via `.env` and `backend/api/core/config.py`
- Key paths:
  - `UPLOAD_DIR`: user uploads
  - `MODELS_DIR`: `checkpoints/` and `serving/`
  - `FRAMEWORK_PATH`, `BASE_MODEL_PATH`: model framework roots
- Services:
  - PostgreSQL for jobs/metadata
  - Optional Redis for queuing

### Deployment Topology (SIT)
```mermaid
graph TD
  U[Users] -- HTTP/8000 --> P[Portal (FastAPI + UI)]
  P --> D[(PostgreSQL)]
  P --> R[(Redis)]
  P --> S[(Storage: /app/portal/data)]
  P --> F[(Framework: /app/meta-jv-reasoning/...)]
  P --> V[(Model Serving GPUs)]
```

### Operations Checklist
- Before run
  - PostgreSQL reachable (localhost:5432)
  - `.env` paths valid on host (absolute in SIT)
  - Port open (8000 or auto‑selected)
- During run
  - Monitor `/docs`, `/health`, and logs
  - Track job IDs in Dashboard
- After run
  - Check `models/checkpoints/<doctype>`
  - Optionally start serving and verify status

### Rollout Plan
- Phase 1: SIT validation (single node, manual runs)
- Phase 2: Add Redis queue + background workers
- Phase 3: Containerize and add Nginx + SSL
- Phase 4: CI/CD for configs and reproducible jobs

### Risks & Mitigations
- Misconfigured paths → provide SIT `.env` template and path verifier script
- Port conflicts → auto port selection script (`start_sit_port.py`)
- GPU memory pressure → tune `gpu_memory_utilization`, model size
- DB unavailable → degraded mode (limited features), alerting

### Next Steps
- Confirm SIT `.env` absolute paths
- Decide where to host serving (same node vs separate)
- Define evaluation datasets per doctype

---
For details, see `README.md`, `SIT_CONFIGURATION_GUIDE.md`, and API at `/docs`.


