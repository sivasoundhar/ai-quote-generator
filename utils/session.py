import streamlit as st


def initialize_session():

    defaults = {
        "history": [],
        "favorites": [],
        "generated_count": 0,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value