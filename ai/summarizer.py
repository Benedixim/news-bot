import json

from ai.client import GeminiClient
from ai.prompts import SYSTEM_PROMPT


class NewsSummarizer:

    def __init__(self):

        self.client = GeminiClient()

    def summarize(self, text):

        prompt = f"""
{SYSTEM_PROMPT}

Новость:

{text}
"""

        result = self.client.generate(prompt)

        answer = (
            result["candidates"][0]
            ["content"]["parts"][0]["text"]
        )

        answer = answer.replace("```json", "")
        answer = answer.replace("```", "")
        answer = answer.strip()

        return json.loads(answer)