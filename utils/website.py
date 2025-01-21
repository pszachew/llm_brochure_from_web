import requests
from bs4 import BeautifulSoup


class Website:
    def __init__(self, url):
        """
        Initialize the Website instance.

        Parameters:
        url (str): The URL of the website to fetch and parse.
        """
        self.url = url
        self.links = []  # List to store all links
        self.text = ""
        self.title = ""

        # Fetch and parse the HTML
        self._fetch_and_parse()

    def _fetch_and_parse(self):
        """
        Fetch the HTML content of the website and parse it to extract all links and clean the HTML.
        """
        try:
            # Fetch the HTML content
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> tags with an href attribute
            for a_tag in soup.find_all('a', href=True):
                self.links.append(a_tag['href'])

            # Remove irrelevant elements
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()

            # Store the cleaned HTML
            self.text = soup.body.get_text(strip=True, separator='\n')
            self.title = soup.title.string.strip() if soup.title else "No ttile found"
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the URL: {e}")

    def get_links(self):
        """
        Get the list of all links found on the website.

        Returns:
        list: A list of URLs (strings).
        """
        return self.links

    def get_content(self):
        return f"Webpage Title:\n {self.title} \nWebpage content:\n {self.text}"