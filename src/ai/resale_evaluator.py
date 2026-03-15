from dotenv import load_dotenv
import os

load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from src.ai.resale_cache import load_cache, save_cache

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

cache = load_cache()


prompt = PromptTemplate.from_template(
"""
Estimate the resale value (JPY) of this item on the Japanese second-hand market.

Item:
{title}

Respond ONLY with a number.
"""
)


def estimate_resale(title):

    if title in cache:
        return cache[title]

    chain = prompt | llm

    result = chain.invoke({"title": title})

    try:
        resale = int(result.content.strip())
    except:
        resale = 0

    cache[title] = resale
    save_cache(cache)

    return resale