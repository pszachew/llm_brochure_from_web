from agents.brochure_links import BrochureAgent
from utils.llm import LLM
from utils.website import Website

class Summarizer:
    def __init__(self, url: str, links: dict, model: str = 'gpt-4o-mini'):
        self.llm_model = LLM(model)
        self.links = links
        self.url = url
    
    def create_user_prompt(self):
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
    
    def create_system_prompt(self):
        pass
