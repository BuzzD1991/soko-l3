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
# ZWEI KOMPETENZBEREICHE
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
# SECHS MODULE
# =============================================================================

st.subheader("Sechs Module")

module_col123, module_col456 = st.columns(2)

with module_col123:
    st.markdown("#### Modul 1 – Emotionen erkennen und verstehen")
    st.markdown(
        """
        Im ersten Modul legen wir den Grundstein für einen souveränen Umgang mit dem eigenen emotionalen Erleben. 
        Wir beschäftigen uns damit, wie Emotionen entstehen, was sie ausmacht und welchen Sinn und Zweck sie erfüllen. 
        Darauf aufbauend betrachten wir, welchen Einfluss Emotionen auf unser Verhalten haben und welche uns besonders 
        häufig im Schulalltag begegnen.
        """
    )
    
    st.markdown("#### Modul 2 – Emotionen regulieren")
    st.markdown(
        """
        Im zweiten Modul widmen wir uns der Frage, wie es gelingen kann, auch in fordernden Momenten handlungsfähig zu bleiben. 
        Konkret betrachten wir auf Basis des bereits angeeigneten Verständnisses zum Thema Emotionen verschiedene Strategien 
        zur Emotionsregulation im Schulalltag.
        """
    )
    
    st.markdown("#### Modul 3 – Achtsamkeit und Commitment")
    st.markdown(
        """
        Im dritten Modul behandeln wir verschiedene Ansätze, um Achtsamkeit im Schulalltag zu üben und Akzeptanz für 
        belastende Gedanken und Emotionen zu erreichen. Darüber hinaus  laden wir die teilnehmenden Lehrkräfte dazu ein, 
        ihre individuellen berufsbezogenen Werte zu reflektieren und erarbeiten auf dieser Basis Möglichkeiten, ihr 
        berufliches Handeln (wieder) an ebendiesen Werten auszurichten.
        """
    )

with module_col456:
    st.markdown("#### Modul 4 – Perspektivübernahme")
    st.markdown(
        """
        Im vierten Modul richten wir unseren Blick auf die häufigsten Interaktionspartner:innen im schulischen Alltag: die Schüler:innen. 
        Wir betrachten Möglichkeiten, ihre Perspektive einzunehmen und ihre Handlungen nachzuvollziehen, um Ansatzpunkte für eine gelingende 
        Verständigung im Unterricht und darüber hinaus zu finden.
        """
    )

    st.markdown("#### Modul 5 – Beziehungsgestaltung")
    st.markdown(
        """
        Im fünften Modul stellen wir positive Ausgestaltung der Lehrkraft-Schüler:innen-Beziehung in den Mittelpunkt, weil diese eine Grundlage 
        erfolgreichen Lernens darstellt. Wir besprechen die notwendigen Voraussetzungen für eine professionelle Wahrnehmung der Lehrkraft-Schüler:innen-Beziehung 
        und wie der Unterricht so gestaltet werden kann, dass er die  psychologischen Grundbedürfnisse nach Autonomie, Kompetenz und sozialer Eingebundenheit unterstützt.
        """
    )

    st.markdown("#### Modul 6 – Konflikte konstruktiv lösen")
    st.markdown(
        """
        Im sechsten Modul widmen wir uns abschließend dem sozialen Konflikt, der unweigerlich zum schulischen Alltag dazugehört. Wir reflektieren die verschiedenen Haltungen 
        gegenüber Konflikten und die jeweiligen Konsequenzen. Zudem erarbeiten wir konstruktive Verhaltensmöglichkeiten in der akuten Konfliktsituation sowie für 
        die nachhaltige Lösung von Konflikten.
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
