import os 
from dotenv import load_dotenv

class Config:
    """
    Handles loading and validating environment variables like API keys
    """
    def __init__(self):
        load_dotenv(override=True)
        self.api_key=os.getenv('OPENAI_API_KEY')
        self.validate_api_key()

    def validate_api_key(self):
        """
        Validates the API key for common issues like missing or incorrect formats
        """
        if not self.api_key:
            raise ValueError("No API key was found")
        elif not self.api_key.startswith("sk-proj-"):
            raise ValueError("Incorrect API key")
        elif self.api_key.strip() != self.api_key:
            raise ValueError("The API key definition contains whitespaces")