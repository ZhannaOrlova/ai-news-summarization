class PromptBuilder:
    """
    Constructs system and user prompts for GPT-4-mini model interaction.
    """
    SYSTEM_PROMPT = (
        "You're a news reporter writer that is invited to convey the latest news on AI. "
        "You must read the latest news from a website and summarize them in an engaging style."
    )

    @staticmethod
    def user_prompt(website):
        """
        Constructs the user prompt for summarizing all articles.
        """
        return (
            f"The following website '{website.title}' has a collection of the latest news."
            f"Your task is to create an engaging and intelligent and professional summary in the style of a newspaper article and reporting clearly on each topic but in a continous way avoiding ennumaration."
            f"Avoid unnecesary introductions and overly generic comments, but do make a conclusion in an academic style"
            f"Don't use enumeration or bullet points or any kind of listing."
            f"Don't create a title."
            f"Don't use subtitles. Avoid any formatting. The output must be plain text."
            f"Here are the news:\n\n{website.text}"
        )

    @staticmethod
    def messages(website):
        """
        Constructs the messages for the OpenAI API.
        """
        return [
            {"role": "system", "content": PromptBuilder.SYSTEM_PROMPT},
            {"role": "user", "content": PromptBuilder.user_prompt(website)}
        ]