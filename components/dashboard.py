import streamlit as st

from constants import CATEGORIES, LANGUAGES, QUOTE_STYLES


def render_dashboard():
    """Render stats metrics and the quote configuration controls.

    Returns:
        tuple: (category, language, style) selected by the user.
    """
    history = st.session_state.history
    favorites = st.session_state.favorites
    generated = st.session_state.generated_count
    languages = len({item["language"] for item in history if item.get("language")})

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🤖 Quotes Generated", value=generated)

    with col2:
        st.metric(label="❤️ Favorites", value=len(favorites))

    with col3:
        st.metric(label="🌍 Languages Used", value=languages)

    st.divider()

    st.markdown("## ⚙️ Quote Configuration")

    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.selectbox("📚 Category", CATEGORIES)

    with col2:
        language = st.selectbox("🌍 Language", LANGUAGES)

    with col3:
        style = st.selectbox("🎨 Style", QUOTE_STYLES)

    st.write("")

    return category, language, style
