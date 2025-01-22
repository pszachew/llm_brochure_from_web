from agents.brochure_links import BrochureAgent
from agents.summarizer import Summarizer
import markdown
from weasyprint import HTML


def main():
    url = "https://www.pw.edu.pl/"
    filename = url.split('.')[1]
    brochure_agent = BrochureAgent(url)
    brochure = brochure_agent.make_brochure()
    # print(brochure)
    summarizer = Summarizer(url, brochure)
    response = summarizer.make_prediction()
    final_result = f"**URL:** {url}\n \n" + response.content 
    """ with open(f"results/{filename}.md", 'w') as f:
        f.write(final_result) """
    html_content = markdown.markdown(final_result)
    output_pdf_path = f"results/{filename}.pdf"
    HTML(string=html_content).write_pdf(output_pdf_path)


if __name__ == "__main__":
    main()
