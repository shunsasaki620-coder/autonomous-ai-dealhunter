from langchain_core.messages import SystemMessage, HumanMessage
from src.core.llm import get_llm

PLANNER_PROMPT = """
You are a planning agent.

Your job:
- Break the user's request into clear, ordered steps
- Do NOT use tools
- Do NOT execute anything

Output format (strict JSON):
{
  "steps": [
    "step 1",
    "step 2",
    "step 3"
  ]
}
"""

def create_plan(user_input: str) -> list[str]:
    llm = get_llm()

    messages = [
        SystemMessage(content=PLANNER_PROMPT),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    data = response.content

    import json
    plan = json.loads(data)

    return plan["steps"]

