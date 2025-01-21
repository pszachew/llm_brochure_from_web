from agents.brochure_links import BrochureAgent
from agents.summarizer import Summarizer


def main():
    url = "https://edwarddonner.com/"
    brochure_agent = BrochureAgent(url)
    brochure = brochure_agent.make_brochure()
    # print(brochure)
    summarizer = Summarizer(url, brochure)
    print(summarizer.create_user_prompt())


if __name__ == "__main__":
    main()
