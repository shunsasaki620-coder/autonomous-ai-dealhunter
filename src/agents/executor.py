import json
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.core.llm import get_llm
from src.tools import TOOLS

EXECUTOR_PROMPT = """
You are an execution agent.

Rules:
- Execute ONE step at a time
- Use tools when needed
- If a tool is required, respond ONLY in JSON:
  {"tool": "...", "args": {...}}

- If the step is complete, respond ONLY with:
  DONE
"""

def execute_step(step: str):
    llm = get_llm()

    messages = [
        SystemMessage(content=EXECUTOR_PROMPT),
        HumanMessage(content=f"Execute this step: {step}")
    ]

    for _ in range(3):  # short loop per step
        response = llm.invoke(messages)
        content = response.content.strip()

        if content == "DONE":
            return

        try:
            data = json.loads(content)
            tool = data["tool"]
            args = data.get("args", {})

            result = TOOLS[tool](**args)

            messages.append(AIMessage(content=content))
            messages.append(HumanMessage(content=f"Tool result: {result}"))

        except Exception:
            messages.append(AIMessage(content=content))

    raise RuntimeError("Step execution failed")
