import streamlit as st

from common import MODULES, inject_css

inject_css()

# =============================================================================
# HERO
# =============================================================================

st.title("SOKO-L³ | Lehrkräftefortbildung Sozial-emotionale Kompetenzen")

st.markdown(
    """
    **Eine sechsteilige Fortbildung für Lehrkräfte an Schulen in
    benachteiligten Lagen bzw. mit Schülerschaft mit hohen Bildungsrisiken.**

    Entwickelt im Rahmen der wissenschaftlichen Begleitung eines
    Startchancen-Programm-Projekts am Interdisziplinären Kompetenzzentrum
    Überfachliches Lernen (IKOM ÜL). Die Fortbildung folgt dem Prinzip
    *Train-the-Teacher-as-Multiplier*: Lehrkräfte entwickeln zunächst ihre
    eigenen sozial-emotionalen Kompetenzen (SEK) und übertragen diese
    anschließend über passende Materialien direkt in den Unterricht.
    """
)

st.info(
    "Die Fortbildung ist ressourcen- und stärkenorientiert angelegt – "
    "bewusst **nicht** defizit- oder belastungszentriert."
)

st.divider()

# =============================================================================
# KENNZAHLEN
# =============================================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Module", "6")

with col2:
    n_done = sum(1 for m in MODULES if m["status"] == "vollständig ausgearbeitet")
    st.metric("Vollständig ausgearbeitet", n_done)

with col3:
    st.metric("Kompetenzbereiche", "2")

with col4:
    st.metric("Ansatz", "Train-the-Trainer")

st.divider()

# =============================================================================
# ZWEI SÄULEN
# =============================================================================

st.subheader("Zwei Kompetenzbereiche")

pillar_col1, pillar_col2 = st.columns(2)

with pillar_col1:
    st.markdown("#### Personale Kompetenzen")
    st.markdown(
        """
        Emotionswahrnehmung und -verstehen, Emotionsregulation sowie
        Achtsamkeit und Wertorientierung (ACT-basiert) – die Grundlage,
        auf der professionelles Handeln im Schulalltag aufbaut.
        """
    )

with pillar_col2:
    st.markdown("#### Soziale Kompetenzen")
    st.markdown(
        """
        Perspektivübernahme und Empathie, beziehungsorientierter Unterricht
        sowie konstruktive Konfliktbewältigung – die Übertragung ins
        Miteinander mit der Schülerschaft.
        """
    )

st.divider()

# =============================================================================
# CTA
# =============================================================================

cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    st.markdown("**Sie möchten wissen, was die einzelnen Module inhaltlich abdecken?**")
    st.page_link("views/module.py", label="Zu den Modulen im Überblick", icon="🧩")

with cta_col2:
    st.markdown("**Sie suchen konkrete Übungen für den Unterricht?**")
    st.page_link("views/uebungssammlung.py", label="Zur Übungssammlung", icon="📚")
