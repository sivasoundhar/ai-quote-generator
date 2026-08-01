import streamlit as st


def render_favorites():
    """Render favorite quotes with the ability to remove them."""
    st.markdown("---")
    st.markdown("## ❤️ Favorite Quotes")

    if not st.session_state.favorites:
        st.info("No favorite quotes yet.")
        return

    for index, quote in enumerate(st.session_state.favorites):
        col1, col2 = st.columns([6, 1])

        with col1:
            st.success(quote)

        with col2:
            if st.button("🗑 Remove", key=f"fav_{index}", width="stretch"):
                st.session_state.favorites.pop(index)
                st.toast("Removed from favorites")
                st.rerun()
