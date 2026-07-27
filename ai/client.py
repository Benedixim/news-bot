import requests

from config import GEMINI_API_KEY


class GeminiClient:

    URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

    def generate(self, prompt):

        response = requests.post(
            self.URL,
            headers={
                "Content-Type": "application/json",
                "X-goog-api-key": GEMINI_API_KEY
            },
            json={
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            },
            timeout=60
        )

        response.raise_for_status()

        return response.json()