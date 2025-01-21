from dotenv import load_dotenv
from openai import OpenAI
import os


class LLM:
    def __init__(self, model: str = 'gpt-4o-mini'):
        self.model = model
        self.client = self.__initialize_openai()

    def __initialize_openai(self):
        load_dotenv()
        key = os.environ.get("OPENAI_API_KEY")
        if key is None:
            raise ValueError("OPEN_AI_API_KEY cannot be None.")
        client = OpenAI()
        return client

    def make_completion(self, messages: list):
        completion = self.client.chat.completions.create(
            model=self.model, messages=messages,
            response_format={"type": "json_object"})
        return completion.choices[0].message

    def make_completion_stream(self, messages: list):
        stream = self.client.chat.completions.create(
            model=self.model, messages=messages, stream=True
        )
        return stream