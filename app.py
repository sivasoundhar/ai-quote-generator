import streamlit as st

from components.dashboard import render_dashboard
from components.favorites import render_favorites
from components.footer import render_footer
from components.hero import render_hero
from components.history import add_quote, render_history
from components.quote_card import render_quote_card
from components.sidebar import render_sidebar
from constants import APP_TITLE
from llm import generate_quote
from utils.session import initialize_session

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_css():
    try:
        with open("assets/styles.css", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass


load_css()
initialize_session()

# ---------------- Sidebar ---------------- #

temperature, max_tokens = render_sidebar()

# ---------------- Main ---------------- #

render_hero()

category, language, style = render_dashboard()

if st.button("✨ Generate Quote", type="primary", width="stretch"):
    with st.spinner("🤖 AI is writing your quote..."):
        try:
            quote = generate_quote(
                category=category,
                language=language,
                style=style,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as exc:
            st.error(f"Failed to generate quote: {exc}")
            quote = None

    if quote:
        add_quote(quote, category, language, style)
        st.session_state.last_quote = quote
        st.session_state.last_category = category
        st.session_state.last_language = language
        st.session_state.last_style = style
        st.toast("🎉 Quote generated!")

# ---------------- Last Generated Quote ---------------- #

if st.session_state.get("last_quote"):
    render_quote_card(
        quote=st.session_state.last_quote,
        category=st.session_state.last_category,
        language=st.session_state.last_language,
        style=st.session_state.last_style,
    )

# ---------------- History & Favorites ---------------- #

render_history()
render_favorites()
render_footer()
