import streamlit as st

from constants import DOWNLOAD_FILE
from utils.clipboard import render_copy_button
from utils.pdf import generate_pdf


def render_quote_card(
    quote: str,
    category: str,
    language: str,
    style: str,
):
    """Render the generated quote with TXT / Copy / Favorite / PDF actions."""
    if not quote:
        return

    st.markdown("## 💬 Generated Quote")

    st.markdown(
        f"""
<div style="
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 30px;
    border-radius: 18px;
    border-left: 8px solid #4F8BF9;
    box-shadow: 0 0 15px rgba(0, 0, 0, .25);
    font-size: 22px;
    line-height: 1.8;
    color: white;
">
    ✨ {quote}
</div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.download_button(
            "⬇ TXT",
            data=quote,
            file_name=DOWNLOAD_FILE,
            mime="text/plain",
            width="stretch",
        )

    with col2:
        render_copy_button(quote)

    with col3:
        if st.button("❤️ Favorite", width="stretch"):
            if quote not in st.session_state.favorites:
                st.session_state.favorites.append(quote)
                st.toast("❤️ Added to favorites!")
            else:
                st.toast("Already in favorites")

    with col4:
        pdf = generate_pdf(quote, category, language)
        st.download_button(
            "📄 PDF",
            data=pdf,
            file_name="quote.pdf",
            mime="application/pdf",
            width="stretch",
        )
