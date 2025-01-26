from IPython.display import Markdown, display

class SummaryDisplay:
    """
    Handles the display of the summarized content
    """
    # @staticmethod
    # def display(summary):
    #     try:
    #         display(Markdown(summary))
    #     except:
    #         print("\nSummary:\n")
    #         print(summary)
    @staticmethod
    def display(summary):
        try:
            print("\nSummary:\n")
            print(summary)            
        except Exception as e:
            print(f"An error occurred: {e}")
        return None