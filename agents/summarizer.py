from agents.brochure_links import BrochureAgent
from utils.llm import LLM
from utils.website import Website

class Summarizer:
    def __init__(self, url: str, links: dict, model: str = 'gpt-4o-mini'):
        self.llm_model = LLM(model)
        self.links = links
        self.url = url
        self.user_prompt = self.__create_user_prompt()
        self.system_prompt = self.__create_system_prompt()

    def __create_user_prompt(self):
        prompt = "Below you have type of link content and content itself"
        for link in self.links['links']:
            try:
                # print(link['url'])
                page = Website(link['url'])
                prompt += f"\n Type of link: {link['type']}"
                prompt += f"\n content of this link: \n {page.get_content()} \n \n"
                
            except Exception:
                pass
        return prompt

    def __create_system_prompt(self):
        prompt = """
            Your role is to create brochure using received informations about website.
            In user message you get type of link on the website and content of the page.
            Use all informations that you find relevant.
        """
        return prompt

    def make_prediction(self):
        messages = [
            {"role":"system", "content":self.system_prompt},
            {"role":"user", "content":self.user_prompt}
        ]
        response = self.llm_model.make_completion(messages=messages, json=False)
        return response