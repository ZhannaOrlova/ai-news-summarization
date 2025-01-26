from config import Config
from prompt_builder import PromptBuilder
from web_scraper import WebsiteScraper
from gpt_summarizer import GPTSummarizer
from display import SummaryDisplay

def main(url):
    """
    Main function to summarize a website. Returns the summary.
    """
    try:
        config = Config()
        print("Configuration initialized...")
        scraper = WebsiteScraper(url)
        print("Scrapping...")
        summarizer = GPTSummarizer(config.api_key)
        print("Summarizing...")
        summary = summarizer.summarize(scraper)
        print("Summary generated.")
        SummaryDisplay.display(summary)
        return summary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    main("https://economictimes.indiatimes.com/tech/artificial-intelligence?from=mdr")



