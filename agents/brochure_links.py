from utils.website import Website
from utils.llm import LLM
import json


class BrochureAgent:
    def __init__(self, url: str, model: str = 'gpt-4o-mini'):
        self.page = Website(url)
        self.llm_model = LLM(model)
        self.user_prompt = self.__create_user_prompt()
        self.system_prompt = self.__create_system_prompt()

    def __create_user_prompt(self) -> str:
        prompt = f"Here is the list of link found on the website of {self.page.url}\n"
        prompt += "Some of them may be relevant. Please decide which of them really are relevant and respond "
        prompt += "with full URL in JSON format."
        prompt += "\nLinks:"
        prompt += "\n".join(self.page.get_links())
        return prompt

    def __create_system_prompt(self) -> str:
        sys_prompt = """You receive list of links found on a webpage.
        Your role is to determine which of them are relevent to include
        in brochure about the company.\n"""
        sys_prompt += "Please respond in json format as in the example below: "
        sys_prompt += """
            {
                "links:": [
                    {"type": "about page", "url":"https://full.url/aboutus/here"},
                    {"type:" "career", "url":"https://another.full.url/career/open_positions"}
                ]
            }
        """
        return sys_prompt.strip()
    
    def make_brochure(self) -> dict:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt}
        ]
        response = self.llm_model.make_completion(messages=messages)
        json_response = json.loads(response.content)
        return json_response
    

