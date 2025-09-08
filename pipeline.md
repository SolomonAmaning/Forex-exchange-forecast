##  Pipeline Plan: Automated Model Training and Inferencing Portal  

Prepared by  Solomon Odum

### Goals
- Centralize dataset management, training, evaluation, and serving behind a single UI/API.
- Make reproducible runs with clear configs and artifacts.
- Provide observability for jobs and system health.

###  Architecture 
```mermaid
flowchart LR
  UI["Frontend (React)"] --> API["Backend (FastAPI)"]
  API --> SVC["Service Layer"]
  SVC --> DB["Database"]
  SVC --> CACHE["Cache/Queue"]
  SVC --> FS["Portal Data (uploads/models/backups)"]
  SVC --> FW["Framework (models code)"]
  SVC --> SRV["Model Serving (GPU)"]
  SVC --> LOGS["Logs/Monitoring"]
```

###  Operational Flow
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

### Data Flow
```mermaid
sequenceDiagram
  participant User
  participant UI as Portal UI
  participant API as FastAPI
  participant FS as Storage
  participant DB as Database
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
  - Database for jobs/metadata (e.g., PostgreSQL)
  - Cache/Queue for background work (e.g., Redis)
