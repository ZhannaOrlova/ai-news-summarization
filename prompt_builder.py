class PromptBuilder:
    """
    Constructs system and user prompts for GPT-4-mini model interaction
    """
    SYSTEM_PROMPT = (
        "You're a news reporter writer that is invited to convey the latest news on AI."  
        "You must read the latest news from a website and summarize them in an engaging style."
    )

    @staticmethod
    def user_prompt(website):
        return(
            f"The Economic Times tech section {website.title} has a relevant collection of the lates news."
            f"You're task is to create an engaging and intelligent summary in the style of a newsparer artichle story that includes all the topics"
            f"Don't use subtitles. Avoid any formating. The output must be plain text."
            f"Here are the news {website.text}"
        )

    @staticmethod
    def messages(website):
        return [
            {"role": "system", "content": PromptBuilder.SYSTEM_PROMPT},
            {"role": "user", "content": PromptBuilder.user_prompt(website)}
            ]
