from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from src.tools.mercari_tool import mercari_search

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

tools = [mercari_search]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are an AI that searches Mercari listings using available tools."
)

while True:

    user_input = input("\nAsk the AI: ")

    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}
    )

    print("\nAI Response:\n")
    print(result["messages"][-1].content)