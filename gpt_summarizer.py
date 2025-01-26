from openai import OpenAI
from prompt_builder import PromptBuilder

class GPTSummarizer:
    """
    Interacts with OpenAI API to summarize websites.
    """

    def __init__(self, api_key):
        self.openai = OpenAI()
        self.openai.api_key = api_key

    def summarize(self, website):
        messages = PromptBuilder.messages(website)
        response = self.openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages
        )
        return response.choices[0].message.content
    

        