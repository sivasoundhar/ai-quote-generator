from datetime import datetime

import streamlit as st

MAX_HISTORY = 10


def add_quote(
    quote: str,
    category: str,
    language: str,
    style: str,
):
    """Store a generated quote in session history."""
    if not quote:
        return

    item = {
        "quote": quote,
        "category": category,
        "language": language,
        "style": style,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M"),
    }

    st.session_state.history.insert(0, item)
    st.session_state.generated_count += 1
    st.session_state.history = st.session_state.history[:MAX_HISTORY]


def render_history():
    """Render the recent quotes list with a clear button."""
    st.markdown("---")
    st.subheader("🕒 Recent Quotes")

    if not st.session_state.history:
        st.info("No quotes generated yet.")
        return

    for item in st.session_state.history:
        with st.container(border=True):
            st.markdown(f"**{item['quote']}**")

            c1, c2 = st.columns(2)

            with c1:
                st.caption(f"📚 {item['category']}")
                st.caption(f"🌍 {item['language']}")

            with c2:
                st.caption(f"🎨 {item['style']}")
                st.caption(f"🕒 {item['time']}")

    if st.button("🗑 Clear History", width="stretch"):
        st.session_state.history.clear()
        st.toast("History cleared")
