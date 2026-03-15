from dotenv import load_dotenv
import os
import json
import re

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = PromptTemplate.from_template(
"""
You are an expert second-hand clothing reseller in Japan.

Evaluate this resale opportunity.

Item title: {title}
Buy price: {price} yen
Estimated resale: {resale} yen

Respond ONLY with JSON in this format:

{{
"reason": "short explanation",
"confidence": 0.0
}}
"""
)


def evaluate_deal(title, price, resale):

    chain = prompt | llm

    result = chain.invoke({
        "title": title,
        "price": price,
        "resale": resale
    })

    text = result.content

    try:

        # Extract JSON block
        json_text = re.search(r"\{.*\}", text, re.DOTALL).group()

        data = json.loads(json_text)

        return {
            "reason": data.get("reason", ""),
            "confidence": data.get("confidence", 0.5)
        }

    except Exception:

        return {
            "reason": "Could not parse AI reasoning",
            "confidence": 0.5
        }