import streamlit as st
import base64
from config import Config
from web_scraper import WebsiteScraper
from gpt_summarizer import GPTSummarizer

st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="📰",
    layout="wide"
)

def get_base64_image(image_path):
    """
    Encodes an image to base64 to use as a background.
    """
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Background image '{image_path}' not found.")
        return ""

BACKGROUND_IMAGE_PATH = "wallpaper.jpg"
background_image_base64 = get_base64_image(BACKGROUND_IMAGE_PATH)  

st.markdown(
    f"""
    <style>
    /* Apply background image to the main app container */
    [data-testid="stAppViewContainer"] {{
        background: url("data:image/jpeg;base64,{background_image_base64}") no-repeat center center fixed;
        background-size: cover;
    }}
    [data-testid="stHeader"] {{
        background: transparent;  /* Remove header background */
    }}
    [data-testid="stToolbar"] {{
        display: none;  /* Remove Streamlit toolbar */
    }}
    /* Style the button */
    button[data-testid="stButton"] {{
        background-color: white;
        border: 2px solid #f03e3e;
        border-radius: 15px;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: bold;
        color: #f03e3e;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }}
    button[data-testid="stButton"]:hover {{
        background-color: #f03e3e;
        color: white;
        transform: scale(1.05);
    }}
    /* Style the summary container */
    .summary-container {{
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px 30px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
        max-width: 800px;
        margin: 30px auto;
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Try Out The AI News Summarizer</h1>", unsafe_allow_html=True)

# Initialize session state variables
if "summary_generated" not in st.session_state:
    st.session_state.summary_generated = False
if "summary" not in st.session_state:
    st.session_state.summary = ""

button_placeholder = st.empty()
summary_placeholder = st.empty()

def generate_summary():
    """
    Generates the summary by scraping the website and summarizing the content.
    """
    try:
        config = Config()
        scraper = WebsiteScraper("https://economictimes.indiatimes.com/tech/artificial-intelligence?from=mdr")
        summarizer = GPTSummarizer(config.api_key)

        summary = summarizer.summarize(scraper)
        st.session_state.summary = summary
        st.session_state.summary_generated = True  # Mark summary as generated
    except Exception as e:
        st.error(f"An error occurred while generating the summary: {e}")
        st.session_state.summary_generated = False  # Reset the state if there's an error

# Handle button click and summary generation
if st.session_state.summary_generated:
    if st.session_state.summary:
        button_placeholder.empty()

        summary_placeholder.markdown(
            f"""
            <div class='summary-container'>
                <h2>Your Daily AI News Digest!</h2>
                <p style="text-align: justify;">{st.session_state.summary}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    with button_placeholder.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Generate AI News Article", key="generate_button"):
                with summary_placeholder.container():
                    with st.spinner("Generating summary, please wait..."):
                        generate_summary()
                st.session_state.summary_generated = True
                st.rerun()  