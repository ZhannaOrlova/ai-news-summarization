import requests
from bs4 import BeautifulSoup

class WebsiteScraper:
    """
    Scrapes and extracts relevant content from a website URL.
    """
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    def __init__(self, url):
        self.url = url
        self.soup = self._fetch_website()
        self.title = self._extract_title()
        self.text = self._extract_text()

    def _fetch_website(self):
        response = requests.get(self.url, headers=self.HEADERS)
        response.raise_for_status # e.g., 404
        return BeautifulSoup(response.content, 'html.parser') 
    
    def _extract_title(self):
        return self.soup.title.string if self.soup.title else "No title found"
    
    def _extract_text(self):
        for irrelevant in self.soup.body([
            "script",
            "style",
            "img",
            "input"
        ]):
            irrelevant.decompose()
        return self.soup.body.get_text(separator="\n", strip=True)
    