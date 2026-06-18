# 1. Imports
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# 2. Setup API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. AI Function
def summarize(text):
    prompt = f"""
    Given the following text, provide:
    1. A 3-sentence summary
    2. 3 key bullet points
    3. Overall sentiment (Positive / Negative / Neutral) with one reason

    Text: {text}
    """
    response = model.generate_content(prompt)
    return response.text

# 4. Streamlit UI
st.title("🧠 AI Text Summarizer")
st.write("Paste any text below and get an instant AI summary")

user_input = st.text_area("Your Text", height=200,
                           placeholder="Paste a news article, notes, anything...")

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing..."):
            result = summarize(user_input)
        st.success("Done!")
        st.markdown(result)
    else:
        st.warning("Please paste some text first!")