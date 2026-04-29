import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def extract_json(text):
    match = re.search(r"\[\s*{.*}\s*\]", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except:
            return []
    return []


def parse_test_case(test_case):
    print(f"🤖 AI analyzing: {test_case}")

    prompt = f"""
You are a STRICT QA automation step generator.

ONLY OUTPUT VALID JSON ARRAY LIKE THIS:

[
  {{"action": "click", "target": "backpack"}},
  {{"action": "click", "target": "cart"}},
  {{"action": "click", "target": "checkout"}},
  {{"action": "type", "target": "first", "value": "John"}},
  {{"action": "type", "target": "last", "value": "Doe"}},
  {{"action": "type", "target": "zip", "value": "12345"}},
  {{"action": "click", "target": "finish"}},
  {{"action": "verify", "target": "complete"}}
]

RULES:
- ONLY click / type / verify
- NO extra words
- NO custom actions
- NO empty targets
- NO explanations

Test Case:
{test_case}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=60
        )

        result = response.json().get("response", "")
        return extract_json(result)

    except Exception as e:
        print("❌ AI Error:", e)
        return []