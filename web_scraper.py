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
        self.text = self._extract_all_articles()  # Combine all articles into one text

    def _fetch_website(self):
        response = requests.get(self.url, headers=self.HEADERS)
        response.raise_for_status()  # Raise an error for bad status codes
        return BeautifulSoup(response.content, 'html.parser')

    def _extract_title(self):
        return self.soup.title.string if self.soup.title else "No title found"

    def _extract_all_articles(self):
        """
        Extracts and combines the content of all articles.
        """
        combined_text = ""
        article_links = self.soup.find_all("a", class_="article-link") 

        for link in article_links:
            article_url = link["href"]
            article_content = self._extract_article_content(article_url)
            if article_content:
                combined_text += f"{article_content}\n\n"

        return combined_text.strip()

    def _extract_article_content(self, article_url):
        """
        Extracts the content of a single article.
        """
        try:
            response = requests.get(article_url, headers=self.HEADERS)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            content = soup.find("div", class_="article-content").get_text() 
            return content.strip()
        except Exception as e:
            print(f"Error scraping article: {e}")
            return None