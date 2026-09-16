import streamlit as st

from common import MODULES, inject_css

inject_css()

st.title("Module im Überblick")

st.markdown(
    """
    Die Fortbildung gliedert sich in sechs Module, verteilt auf zwei
    Kompetenzbereiche. Modul 6 liegt aktuell als vollständig ausgearbeitetes
    Online-Modul vor; die übrigen Module befinden sich in Entwicklung und
    sind hier mit ihrem inhaltlichen Grobfokus hinterlegt.
    """
)

st.divider()


def render_module_card(module):

    status_class = (
        "status-done" if module["status"] == "vollständig ausgearbeitet" else "status-progress"
    )

    st.markdown(
        f"""
        <div class="module-card">
        <div class="module-nr">Modul {module["nr"]}</div>
        <div class="module-title">{module["titel"]}</div>
        <span class="status-badge {status_class}">{module["status"]}</span>
        <div>{module["kurz"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =============================================================================
# PERSONALE KOMPETENZEN
# =============================================================================

st.subheader("Personale Kompetenzen")

for module in [m for m in MODULES if m["bereich"] == "Personale Kompetenzen"]:
    render_module_card(module)

st.divider()

# =============================================================================
# SOZIALE KOMPETENZEN
# =============================================================================

st.subheader("Soziale Kompetenzen")

for module in [m for m in MODULES if m["bereich"] == "Soziale Kompetenzen"]:
    render_module_card(module)

st.divider()

st.page_link("views/ansatz.py", label="Zum methodischen Ansatz & zur Zielgruppe", icon="🎯")
