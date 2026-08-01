import os

import streamlit as st

from constants import APP_SUBTITLE, APP_TITLE, APP_VERSION, BANNER_PATH


def render_hero():
    if os.path.exists(BANNER_PATH):
        st.image(BANNER_PATH, width="stretch")

    st.markdown(f"# {APP_TITLE}")
    st.caption(APP_SUBTITLE)

    col1, col2 = st.columns([3, 1])

    with col2:
        st.success(APP_VERSION)

    st.divider()
