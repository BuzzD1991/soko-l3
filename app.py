import streamlit as st

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="SOKO-L³ – Lehrkräftefortbildung zur Förderung der sozial-emotionalen Kompetenzen",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# NAVIGATION
# =============================================================================

with st.sidebar:
    st.markdown("### SOKO-L³")
    st.caption(
        "Lehrkräftefortbildung zur Förderung der sozial-emotionalen Kompetenzen · "
        "IKOM ÜL im Rahmen des Startchancen-Programms"
    )
    st.divider()

pages = {
    "Programm": [
        st.Page("views/start.py", title="Start", icon="🏠", default=True),
        st.Page("views/ansatz.py", title="Ansatz & Zielgruppe", icon="🎯"),
    ],
    "Praxis": [
        st.Page("views/uebungssammlung.py", title="Übungssammlung", icon="📚"),
    ],
}

navigation = st.navigation(pages)
navigation.run()
