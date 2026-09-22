import streamlit as st

from common import MODULES, inject_css

inject_css()

st.title("Module im Überblick")

st.markdown(
    """
    Die Fortbildung gliedert sich in sechs Module, verteilt auf zwei
    Kompetenzbereiche.
    """
)

st.divider()

st.divider()

st.page_link("views/ansatz.py", label="Zum methodischen Ansatz & zur Zielgruppe", icon="🎯")
