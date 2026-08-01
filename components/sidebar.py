import streamlit as st

from constants import (
    APP_SUBTITLE,
    APP_TITLE,
    APP_VERSION,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
    LOGO_PATH,
)


def render_sidebar():
    """Render the sidebar (branding + AI settings).

    Returns:
        tuple: (temperature, max_tokens) slider values.
    """
    with st.sidebar:
        st.image(LOGO_PATH, width=180)

        st.markdown(f"## {APP_TITLE}")
        st.caption(APP_SUBTITLE)

        st.divider()

        st.markdown("### ⚙️ AI Settings")

        temperature = st.slider(
            "🔥 Creativity",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.1,
        )

        max_tokens = st.slider(
            "📏 Quote Length",
            min_value=50,
            max_value=300,
            value=DEFAULT_MAX_TOKENS,
            step=10,
        )

        st.divider()

        st.info(
            f"💡 Generate beautiful AI quotes.\n\n"
            f"Version {APP_VERSION}"
        )

        with st.expander("ℹ About"):
            st.write(
                "This project demonstrates:\n\n"
                "• Streamlit\n"
                "• Groq\n"
                "• Docker\n"
                "• CI/CD\n"
                "• Render Deployment\n"
                "• Prompt Engineering"
            )

    return temperature, max_tokens
