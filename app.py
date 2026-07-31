import streamlit as st

from constants import (
    APP_TITLE,
    CATEGORIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
)

from prompts import build_prompt
from llm import generate_quote

st.set_page_config(
    page_title="AI Quote Generator",
    page_icon="🤖",
    layout="centered",
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("⚙ Settings")

temperature = st.sidebar.slider(
    "Creativity",
    0.0,
    1.0,
    DEFAULT_TEMPERATURE,
)

max_tokens = st.sidebar.slider(
    "Quote Length",
    50,
    200,
    DEFAULT_MAX_TOKENS,
)

if st.sidebar.button("🗑 Clear History"):
    st.session_state.history = []

# ---------------- Session ---------------- #

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- Main ---------------- #

st.title(APP_TITLE)

st.write("Generate inspiring AI-powered quotes using Groq.")

category = st.selectbox(
    "Choose a Category",
    CATEGORIES,
)

if st.button("✨ Generate Quote"):

    prompt = build_prompt(category)

    quote = generate_quote(
        prompt,
        temperature,
        max_tokens,
    )

    st.success("Quote Generated Successfully!")

    st.text_area(
        "Generated Quote",
        quote,
        height=170,
    )

    st.download_button(
        "📥 Download Quote",
        data=quote,
        file_name="AI_Quote.txt",
        mime="text/plain",
    )

    st.session_state.history.insert(
        0,
        f"{category} : {quote}",
    )

# ---------------- History ---------------- #

if st.session_state.history:

    st.divider()

    st.subheader("🕘 Quote History")

    for item in st.session_state.history:
        st.write("•", item)