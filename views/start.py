import streamlit as st

from common import MODULES, inject_css

inject_css()

# =============================================================================
# HERO
# =============================================================================

st.title("SOKO-L³ | Lehrkräftefortbildung Sozial-emotionale Kompetenzen")

st.markdown(
    """
    **Ein sechsteiliges Fortbildungsangebot für Lehrkräfte an Schulen in
    benachteiligten Lagen bzw. mit Schülerschaft mit hohen Bildungsrisiken.**

    Entwickelt im Rahmen der wissenschaftlichen Begleitung eines
    Startchancen-Programm-Projekts am Interdisziplinären Kompetenzzentrum
    Überfachliches Lernen (IKOM ÜL). Die teilnehmenden Lehrkräfte stärken zunächst
    ihre eigenen sozial-emotionalen Kompetenzen; diese sollen als Grundlage für
    einen souveränen Umgang mit herausfordernden Situationen und die Gestaltung 
    tragfähiger Beziehungen zu den Schüler:innen dienen. Zusätzlich erhalten die
    Lehrkräfte passgenaue Materialien, um die Inhalte direkt mit ihren Klassen zu erarbeiten.
    Die Fortbildung vermittelt unmittelbar einsetzbare Strategien für den Schulalltag, 
    die sich an den Bedarfen von Schulen mit besonderen Herausforderungen orientieren, 
    ohne eine defizitorientierte Perspektive einzunehmen.
    """
)

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
        In den ersten drei Modulen richten wir den Blick zunächst auf die eigene Person: 
        Wir vertiefen unser Verständnis für das individuelle emotionale Erleben und stärken 
        die persönliche Grundlage für einen souveränen Schulalltag.
        """
    )

with pillar_col2:
    st.markdown("#### Soziale Kompetenzen")
    st.markdown(
        """
        In den folgenden drei Modulen weiten wir den Blick auf die tägliche Zusammenarbeit 
        mit den Schüler:innen.
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
