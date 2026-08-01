import html
import json

import streamlit as st
from streamlit.components.v1 import html as st_html


def render_copy_button(quote: str):
    """Render a copy-to-clipboard button styled like the app buttons."""
    if not quote:
        return

    # json.dumps produces a valid JS string literal (quotes safely escaped).
    payload = json.dumps(quote)

    onclick = (
        f"navigator.clipboard.writeText({payload}).then(() => "
        f"{{ this.textContent = '✅ Copied!'; this.style.background = '#16a34a'; }});"
    )

    st_html(
        f"""
<button onclick="{html.escape(onclick, quote=True)}"
    style="
        width: 100%;
        height: 50px;
        border-radius: 12px;
        font-size: 17px;
        font-weight: bold;
        background: #4F8BF9;
        color: white;
        border: none;
        cursor: pointer;
    ">
    📋 Copy
</button>
        """,
        height=70,
    )
