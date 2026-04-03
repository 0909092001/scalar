# GitHub And Hugging Face Setup

## Suggested GitHub repository name

`supportdesk-openenv`

## Suggested GitHub description

Real-world OpenEnv customer support triage environment with deterministic graders, dense rewards, Docker deployment, and OpenAI-client baseline inference.

## Suggested topics

- openenv
- reinforcement-learning
- ai-agents
- customer-support
- fastapi
- huggingface-spaces
- docker
- evaluation

## Local git commands

Run these inside the project folder:

```bash
git init
git checkout -b main
git add .
git commit -m "Initial hackathon submission"
git remote add origin https://github.com/YOUR_USERNAME/supportdesk-openenv.git
git push -u origin main
```

If GitHub asks for authentication, use GitHub Desktop, Git Credential Manager, or a personal access token.

## Hugging Face Space setup

Create a new Space with:

- Space SDK: `Docker`
- Space name: `supportdesk-openenv`
- Visibility: your choice
- Tag: `openenv`

Then push this repository to the Space:

```bash
git remote add hf https://huggingface.co/spaces/YOUR_HF_USERNAME/supportdesk-openenv
git push hf main
```

## Required Space variables

Add these in the Space settings if you want to run `inference.py` there:

- `API_BASE_URL`
- `MODEL_NAME`
- `HF_TOKEN`

## Recommended validation flow

```bash
docker build -t supportdesk-triage-env .
docker run --rm -p 8000:8000 supportdesk-triage-env
pytest
python inference.py
```

## Submission checklist

- GitHub repo is public or accessible
- Hugging Face Space is live and returns `200`
- `README.md` is present and complete
- `inference.py` is in the repo root
- `openenv.yaml` is in the repo root
- Docker build succeeds
- Baseline run logs `[START]`, `[STEP]`, and `[END]`
