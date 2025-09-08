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
  subgraph UI["Frontend (React)"]
    UI1["Dashboard"]
    UI2["Document Types"]
    UI3["Pipeline"]
    UI4["Models"]
    UI5["Evaluation"]
    UI6["Monitoring"]
  end

  subgraph API["Backend (FastAPI Routers)"]
    Rauth["/auth_router/"]
    Rdoc["/doctype_router/"]
    Rpipe["/pipeline_router/"]
    Rmodel["/model_router/"]
    Reveal["/evaluation_router/"]
    Rmon["/monitoring_router/"]
  end

  subgraph SVC["Service Layer"]
    FM["file_manager"]
    JM["job_manager"]
    PM["pipeline_manager"]
    MT["model_trainer"]
    EV["evaluator"]
    DM["data_manager"]
    BM["backup_manager"]
    CG["config_generator"]
  end

  DB["PostgreSQL (SQLAlchemy)"]
  RD["Redis (optional)"]
  LOG["Logs"]

  subgraph FS["Portal Data"]
    UP["uploads/"]
    CK["models/checkpoints/"]
    SVdir["models/serving/"]
    BK["backups/"]
  end

  FW["FRAMEWORK_PATH"]
  BMPath["BASE_MODEL_PATH"]
  SRV["Model Serving (vLLM/REST)"]

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
  A["Create Document Type"] --> B["Upload Data / Config"]
  B --> C["Start Pipeline (UI -> /pipeline)"]
  C --> D["Create Job in DB"]
  D --> E["Generate Train Config"]
  E --> F["Run Training"]
  F --> G["Write Checkpoints to models/checkpoints/{doctype}"]
  G --> H["Evaluate Model"]
  H --> I["Register/Expose in Models"]
  I --> J["Start Serving"]
  J --> K["Inference via REST"]
  K --> L["Monitor + Logs"]
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


