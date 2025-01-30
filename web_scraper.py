import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)

class WebsiteScraper:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    def __init__(self, url):
        self.url = url
        self.soup = self._fetch_website()
        self.title = self._extract_title()
        self.text = self._extract_all_articles()
        logging.info(f"Scraped {len(self.text)} characters of content")

    def _fetch_website(self):
        logging.info(f"Fetching URL: {self.url}")
        try:
            response = requests.get(self.url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logging.error(f"Failed to fetch page: {e}")
            return None

    def _extract_title(self):
        return self.soup.title.string.strip() if self.soup.title else "No title found"

    def _extract_all_articles(self):
        if not self.soup:
            return ""
            
        combined_text = ""
        article_cards = self.soup.select('div[class*="uwU81"]')  # article cards container
        
        logging.info(f"Found {len(article_cards)} article cards")
        
        for i, card in enumerate(article_cards[:5]): 
            link = card.find('a', href=True)
            if not link:
                continue
                
            article_url = urljoin(self.url, link['href'])
            logging.info(f"Scraping article {i+1}: {article_url}")
            article_content = self._extract_article_content(article_url)
            if article_content:
                combined_text += f"{article_content}\n\n"
        
        return combined_text.strip()

    def _extract_article_content(self, article_url):
        try:
            response = requests.get(article_url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            content = soup.find('div', class_='_s30J') or \
                     soup.find('div', class_='ga-headlines') or \
                     soup.find('article')
            
            if content:
                for element in content.select('.ad-container, .comments-section, script'):
                    element.decompose()
                return content.get_text(separator='\n', strip=True)
            
            logging.warning(f"No content found at {article_url}")
            return None
            
        except Exception as e:
            logging.error(f"Error scraping article: {e}")
            return None