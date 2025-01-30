from web_scraper import WebsiteScraper

def test_scraping():
    url = "https://timesofindia.indiatimes.com/topic/artificial-intelligence/news"
    scraper = WebsiteScraper(url)
    
    print("\n" + "=" * 50)
    print("Extracted Title:")
    print(scraper.title)
    print("=" * 50)
    
    print("\nExtracted Articles Content:")
    print(scraper.text[:2000])  # first 2000 characters to check
    print("\n" + "=" * 50)
    
    print(f"Total Content Length: {len(scraper.text)} characters")

if __name__ == "__main__":
    test_scraping()