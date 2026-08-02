# AI OS — Flow Diagrams

> Call hierarchy and request flow for Clavex AI OS (WAT framework + an agent runtime).
> Rendered from: `OS.md`, `docs/ARCHITECTURE.md`, `03-engineering-os/**`, `07-scripts/`, `12-memory/`.

## Two machines on the LAN

The OS can span two machines on a private home network *(names anonymized)*:

- **Desktop** — the workstation PC running the **agent desktop app**. It is
  the vault's master writer and runs its own local cron scheduler.
- **Server** — an always-on LAN server running the **agent gateway + cron
  scheduler**, a **private git host** (for this repo and the vault), a
  **deployment tool**, and **n8n**. It keeps its own, separate cron scheduler.

Scheduled jobs run where their delivery requires them; vault sync flows
desktop → git host → server.

---

## 1. Call hierarchy — who invokes what

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 8, "rankSpacing": 16, "padding": 4, "useMaxWidth": false}, "themeVariables": {"fontSize": "12.5px"}}}%%
flowchart LR
    subgraph RT["Runtime"]
        direction TB
        AG["Agent"]
        CR["cron ⭐"]
    end
    EN["bridge file<br/>3 adapters"]
    OS["OS.md"]
    subgraph RO["Router"]
        direction TB
        IM["intent-map"]
        PF["11 profiles"]
    end
    WF["10 workflows"]
    SC["scripts"]
    ME["12-memory"]
    RT --> EN --> OS
    OS --> RO
    CR --> PF
    RO --> WF
    WF --> SC
    WF --> ME
    SC --> ME
```

> ⭐ = **promoted**. Five agent-driven cron jobs (Email
> Intelligence, Daily Note Compile, Concept Sweep, Tool Matrix, Update Manager)
> no longer carry their procedure inline in the cron prompt.
>
> The cron now owns only the **schedule + gather script + workdir**; it fires a
> one-line prompt that loads the matching **profile → workflow** (versioned in
> git, reusable from a chat). The same workflow runs whether triggered by cron
> or by an intent match in a live session — one source of truth.
>
> See `03-engineering-os/context-router/intent-map.md`.

---

## 2. Flow chart — request to output

From `docs/ARCHITECTURE.md` § "How a request moves":

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 8, "rankSpacing": 16, "padding": 4, "useMaxWidth": false}, "themeVariables": {"fontSize": "12.5px"}}}%%
flowchart LR
    REQ["Request / cron"] --> OS["OS.md"]
    OS --> GOV["Governance +<br/>knowledge"]
    GOV --> ENG["Router →<br/>workflow + agent"]
    ENG --> EXEC["Scripts execute<br/>deterministic actions"]
    EXEC --> OUT["Output tested,<br/>reviewed, released"]
    OUT --> MEM["Decisions + lessons<br/>→ memory"]
    MEM -. compounds .-> REQ
```

---

## 3. Runtime decision loop inside a workflow

Example: `03-engineering-os/workflows/backup_health.md`:

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 6, "rankSpacing": 12, "padding": 3, "useMaxWidth": false}, "themeVariables": {"fontSize": "12px"}}}%%
flowchart TD
    A["Trigger"] --> B["Read workflow SOP"]
    B --> C["Run script<br/>(T in WAT)"]
    C --> D{"has_issues?"}
    D -- false --> E["Log healthy → 12-memory"]
    D -- true --> F["Draft alert: target + fix<br/>append to 12-memory log"]
    E --> H["Done"]
    F --> H
```

---

## 4. Machine architecture

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 8, "rankSpacing": 16, "padding": 4, "useMaxWidth": false}, "themeVariables": {"fontSize": "12.5px"}}}%%
flowchart TB
    subgraph DESK["🖥️ Desktop"]
        direction LR
        D_H["Agent desktop app"]
        D_C["cron scheduler"]
        D_V["Notes vault (master)"]
        D_P["5 promoted ⭐ jobs"]
    end
    subgraph SRV["🖧 Server"]
        direction LR
        S_GW["Agent gateway + cron"]
        S_G["Private git host"]
        S_A["Deploy tool · n8n"]
        S_T["3 Telegram jobs"]
    end
    D_V -->|"git push"| S_G
    S_G -->|"git pull"| S_GW
```

Vault sync: **desktop writes → pushes to the server's git host → server pulls**.
Telegram-delivering cron jobs run on the **server only** (the desktop's gateway
has no Telegram channel). The two machines keep **separate** scheduler configs —
the 5 promoted ⭐ jobs live in the desktop's scheduler; the server runs its own
set (Backup Guardian, Meta-Check, Weekly Summary).
