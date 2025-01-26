# AI News Summarizer

## Overview

The **AI News Summarizer** is a Python-based project that scrapes the latest news from a given website and generates an engaging and intelligent summary in the style of a newspaper story. The project focuses on summarizing the latest advancements in AI technology by using OpenAI's GPT-based language model. Every time you run the project, it retrieves the most recent news articles from *The Economic Times* (or any specified URL) and presents a concise, readable summary, ideal for staying informed about AI trends.

---

## Features

- **Automated News Scraping**: The project scrapes the latest articles from a news website using BeautifulSoup.
- **Engaging Summaries**: It leverages OpenAI's GPT model to generate intelligent and engaging summaries tailored to a newspaper-style format.
- **Daily Updates**: Each time you run the project, it retrieves and summarizes the most recent news articles, ensuring you’re always up-to-date.

### Prompts Used
- **System Prompt**:
  ```plaintext
  You're a news reporter writer that is invited to convey the latest news on AI. 
  You must read the latest news from a website and summarize them in an engaging style.

## How it works

- **Website Scraping**: The WebsiteScraper class fetches the latest news articles and cleans the content by removing irrelevant elements like scripts, styles, and ads.
- **Prompt Building**: The PromptBuilder class prepares system and user prompts for the OpenAI GPT model.
- **GPT Summarization**: The GPTSummarizer class sends the prompts to OpenAI's GPT model to generate the summary.
- **Output**: The summary is displayed directly in the terminal in a readable format.

## Setup Instructions
### Prerequisites
1. Python 3.8 or later
2. Virtual environment (optional but recommended)
3. OpenAI API Key (you can obtain one from OpenAI for 5$ credits that is more than enough to run this proyect)

### Installation
1. Clone this repository

    ```plaintext
    git clone <repository-url>
    cd <repository-folder>

2. Set up a virtual environment (recommended):
- On MacOS/Linux

    ```plaintext
    python -m venv venv
    source venv/bin/activate
- On Windows 

    ```plaintext
    python -m venv venv
    venv\Scripts\activate

3. Install the required dependencies

    `pip install -r requirements.txt`

4. Create a `.env` file and add your API key

    `OPENAI_API_KEY=sk-proj-your-api-key`

5. Run the project
    `python main.py`

### Configuration

To scrape a different website, update the `main.py` script with the desired URL:

main("https://your-preferred-news-website.com")

### Contribution 

Pull requests are welcome. 

### Future enhancements 
While the current implementation runs entirely in the terminal, a major future enhancement will involve the creation of a user-friendly streamlit interface and deployed to streamlit cloud. 

