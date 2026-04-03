---
title: SupportDesk Triage Environment
emoji: "📨"
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
app_port: 8000
base_path: /docs
tags:
  - openenv
---

# SupportDesk Triage Environment

`supportdesk_triage_env` is a real-world customer support operations benchmark for agent training and evaluation. The agent works through a realistic support inbox, classifies tickets, routes them to the right team, drafts grounded replies, and resolves work without inventing unsupported promises.

## Why this environment is useful

Support triage is a real workflow with high practical value:

- revenue risk from outages
- security risk from account compromise
- user experience risk from bad routing or weak replies
- long-horizon reasoning across multiple tickets, not one-shot classification

This makes it a strong fit for OpenEnv-style post-training and agent evaluation.

## Environment API

The server exposes the standard environment loop:

- `POST /reset` -> returns the initial typed observation
- `POST /step` -> accepts a typed action and returns `observation`, `reward`, `done`, and `info`
- `GET /state` -> returns the current environment state
- `GET /health` -> simple readiness check

The project uses typed Pydantic models for:

- `SupportAction`
- `SupportObservation`
- `RewardSignal`
- `SupportState`

## Action space

Each step accepts a `SupportAction` with one of these `action_type` values:

- `view_queue`
- `open_ticket`
- `classify_ticket`
- `assign_team`
- `draft_reply`
- `resolve_ticket`
- `submit_task`

Optional fields let the agent provide:

- `ticket_id`
- `category`
- `priority`
- `assigned_team`
- `draft_reply`
- `resolution_note`

## Observation space

Each observation contains:

- task metadata: `task_id`, `difficulty`, `objective`
- trajectory metadata: `step_count`, `max_steps`, `steps_remaining`
- queue overview: `queue_summary`
- focused context: `active_ticket`
- progress state: `completed_ticket_ids`
- feedback: `last_action`, `last_message`, `last_reward`

## Tasks and graders

All tasks have deterministic graders with scores in `[0.0, 1.0]`.

### 1. `easy_refund_request`

- One billing ticket about a duplicate charge
- Expected difficulty: easy
- Tests basic classification, routing, reply grounding, and closeout

### 2. `medium_multi_queue`

- Three-ticket mixed inbox: account access, technical support, and sales
- Expected difficulty: medium
- Tests queue management and consistent execution across different ticket types

### 3. `hard_incident_escalation`

- Four-ticket pressure scenario: security incident, production outage, VAT issue, feature request
- Expected difficulty: hard
- Tests escalation judgment, prioritization, and keeping factual replies under pressure

### Grading logic

Every ticket is scored on five dimensions:

- category correctness: 25%
- priority correctness: 20%
- team routing correctness: 25%
- reply quality via keyword coverage: 20%
- resolved status: 10%

Task score = average of per-ticket totals.

## Reward design

The reward function gives dense trajectory feedback instead of only terminal success:

- small positive reward for viewing the queue and opening unseen tickets
- positive reward for correct classification and routing
- partial reward for reply quality based on required keyword coverage
- positive reward for resolving a well-triaged ticket
- penalties for wrong labels, wrong routing, missing context, repeated low-value actions, and hitting the step limit
- final grader score added when the agent submits the task

## Project structure

```text
.
├── Dockerfile
├── inference.py
├── openenv.yaml
├── pyproject.toml
├── requirements.txt
├── README.md
├── supportdesk_env/
│   ├── __init__.py
│   ├── environment.py
│   ├── graders.py
│   ├── models.py
│   ├── server.py
│   └── tasks.py
└── tests/
    └── test_environment.py
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn supportdesk_env.server:app --host 0.0.0.0 --port 8000
```

Open:

- API docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

## Docker usage

```bash
docker build -t supportdesk-triage-env .
docker run --rm -p 8000:8000 supportdesk-triage-env
```

## Baseline inference

The required root-level `inference.py` uses the OpenAI client with these environment variables:

- `API_BASE_URL`
- `MODEL_NAME`
- `HF_TOKEN`

Optional:

- `OPENAI_API_KEY` can be used instead of `HF_TOKEN`

Run it with:

```bash
python inference.py
```

The script prints structured logs using the required tags:

- `[START]`
- `[STEP]`
- `[END]`

It uses a tightly constrained JSON prompt to reduce hallucinations:

- fixed label sets for category, priority, and team
- temperature `0`
- strict JSON object output
- deterministic post-processing through typed actions

## Baseline scores

Because baseline scores depend on the external model selected through `MODEL_NAME` and the remote endpoint behind `API_BASE_URL`, this repository includes a reproducible evaluation script rather than hard-coded scores. Run `python inference.py` once with your target model and copy the emitted task scores into your submission form or README snapshot.

## Validation checklist

- `docker build -t supportdesk-triage-env .`
- `docker run --rm -p 8000:8000 supportdesk-triage-env`
- `pytest`
- `python inference.py`
- `openenv validate`
