import streamlit as st

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
# Wird EINMALIG hier gesetzt. Die einzelnen Seiten unter views/ dürfen
# st.set_page_config NICHT erneut aufrufen.

st.set_page_config(
    page_title="SOKO-L³ – Fortbildung Sozial-emotionale Kompetenzen",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# NAVIGATION
# =============================================================================
#
# Die Seitenleiste dient hier ausschließlich der Orientierung zwischen den
# Bereichen der Website (nicht mehr der Übungsfilterung – die Filter der
# Übungssammlung bleiben bewusst im Hauptbereich, siehe views/uebungssammlung.py).

pages = {
    "Programm": [
        st.Page("views/start.py", title="Start", icon="🏠", default=True),
        st.Page("views/module.py", title="Module im Überblick", icon="🧩"),
        st.Page("views/ansatz.py", title="Ansatz & Zielgruppe", icon="🎯"),
    ],
    "Praxis": [
        st.Page("views/uebungssammlung.py", title="Übungssammlung", icon="📚"),
        st.Page("views/ressourcen.py", title="Ressourcen", icon="🔗"),
    ],
}

with st.sidebar:
    st.markdown("### SOKO-L³")
    st.caption(
        "Lehrkräftefortbildung Sozial-emotionale Kompetenzen · "
        "IKOM ÜL im Rahmen des Startchancen-Programms"
    )
    st.divider()

navigation = st.navigation(pages)
navigation.run()
