import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.image("assets/logo.png", width=180)

        st.markdown("## 🤖 AI Quote Generator")
        st.caption("Powered by Groq")

        st.divider()

        language = st.selectbox(
            "🌍 Language",
            [
                "English",
                "தமிழ்",
                "हिन्दी",
                "Español",
                "Français",
                "Deutsch"
            ]
        )

        style = st.selectbox(
            "🎨 Quote Style",
            [
                "Motivational",
                "Professional",
                "Funny",
                "Short",
                "Deep",
                "Leadership"
            ]
        )

        st.divider()

        st.info(
            """
💡 Generate beautiful AI quotes.

Version 2.0
            """
        )

    return language, style