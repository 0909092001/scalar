from __future__ import annotations

import json
import os
from typing import Dict, List

from openai import OpenAI

from supportdesk_env.environment import SupportDeskEnvironment
from supportdesk_env.models import ActionType, SupportAction
from supportdesk_env.tasks import TASKS


SYSTEM_PROMPT = """
You are an extremely careful support-operations triage agent.
Return strict JSON only.
Choose only from the provided categories, priorities, and teams.
Ground the reply in the ticket text and avoid inventing policies.
""".strip()


def log_event(tag: str, payload: Dict[str, object]) -> None:
    print("{0} {1}".format(tag, json.dumps(payload, sort_keys=True)))


def build_client() -> OpenAI:
    api_key = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("HF_TOKEN or OPENAI_API_KEY is required.")

    base_url = os.getenv("API_BASE_URL")
    if not base_url:
        raise RuntimeError("API_BASE_URL is required.")

    return OpenAI(api_key=api_key, base_url=base_url)


def ask_model(client: OpenAI, model_name: str, ticket: Dict[str, object]) -> Dict[str, str]:
    user_prompt = """
Task: Triage the customer-support ticket.

Allowed categories:
- billing
- account_access
- technical_support
- sales
- security
- product_feedback

Allowed priorities:
- low
- medium
- high
- urgent

Allowed teams:
- billing_ops
- customer_success
- technical_support
- sales
- trust_safety
- platform_oncall
- product_ops

Return JSON with keys:
category, priority, assigned_team, draft_reply, resolution_note

Ticket:
{ticket_json}
""".strip().format(ticket_json=json.dumps(ticket, sort_keys=True))

    response = client.chat.completions.create(
        model=model_name,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    content = response.choices[0].message.content
    return json.loads(content)


def run_task(client: OpenAI, model_name: str, task_id: str) -> Dict[str, object]:
    env = SupportDeskEnvironment()
    observation = env.reset(task_id)

    log_event(
        "[START]",
        {"task_id": task_id, "difficulty": TASKS[task_id].difficulty.value, "model": model_name},
    )

    env.step(SupportAction(action_type=ActionType.VIEW_QUEUE))

    for preview in observation.queue_summary:
        ticket_id = preview.ticket_id
        env.step(SupportAction(action_type=ActionType.OPEN_TICKET, ticket_id=ticket_id))
        state = env.state()
        ticket = next(ticket for ticket in state.tickets if ticket.ticket_id == ticket_id)
        plan = ask_model(client, model_name, ticket.model_dump(mode="json"))

        actions: List[SupportAction] = [
            SupportAction(
                action_type=ActionType.CLASSIFY_TICKET,
                ticket_id=ticket_id,
                category=plan["category"],
                priority=plan["priority"],
            ),
            SupportAction(
                action_type=ActionType.ASSIGN_TEAM,
                ticket_id=ticket_id,
                assigned_team=plan["assigned_team"],
            ),
            SupportAction(
                action_type=ActionType.DRAFT_REPLY,
                ticket_id=ticket_id,
                draft_reply=plan["draft_reply"],
            ),
            SupportAction(
                action_type=ActionType.RESOLVE_TICKET,
                ticket_id=ticket_id,
                resolution_note=plan.get("resolution_note") or "Resolved after triage.",
            ),
        ]

        for action in actions:
            result = env.step(action)
            log_event(
                "[STEP]",
                {
                    "task_id": task_id,
                    "step": result.observation.step_count,
                    "ticket_id": ticket_id,
                    "action_type": action.action_type.value,
                    "reward": result.reward,
                },
            )

    final_result = env.step(SupportAction(action_type=ActionType.SUBMIT_TASK))
    summary = {
        "task_id": task_id,
        "final_score": final_result.info["final_score"],
        "episode_reward": env.state().cumulative_reward,
        "steps": final_result.observation.step_count,
    }
    log_event("[END]", summary)
    return summary


def main() -> None:
    model_name = os.getenv("MODEL_NAME")
    if not model_name:
        raise RuntimeError("MODEL_NAME is required.")

    client = build_client()
    summaries = []
    for task_id in ["easy_refund_request", "medium_multi_queue", "hard_incident_escalation"]:
        summaries.append(run_task(client, model_name, task_id))

    overall = round(sum(item["final_score"] for item in summaries) / float(len(summaries)), 4)
    print(json.dumps({"overall_score": overall, "tasks": summaries}, sort_keys=True))


if __name__ == "__main__":
    main()
