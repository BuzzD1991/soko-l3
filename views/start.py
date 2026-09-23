import streamlit as st

from common import MODULES, inject_css

inject_css()

# =============================================================================
# HERO
# =============================================================================

st.title(
    "SOKO-L³ | Lehrkräftefortbildung zur Förderung der sozial-emotionalen Kompetenzen"
)

st.markdown(
    """
    **Ein sechsteiliges Fortbildungsangebot für Lehrkräfte an Schulen in
    benachteiligten Lagen bzw. mit Schülerschaft mit hohen Bildungsrisiken.**

    **Entwickelt im Rahmen der wissenschaftlichen Begleitung eines
    Startchancen-Programm-Projekts am Interdisziplinären Kompetenzzentrum
    Überfachliches Lernen (IKOM ÜL); gefördert durch das Bundesministerium 
    für Bildung, Familie, Senioren, Frauen und Jugend.** 
    
    Die teilnehmenden Lehrkräfte stärken zunächst
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
# ZWEI KOMPETENZBEREICHE / SECHS MODULE
# =============================================================================

st.subheader("Zwei Kompetenzbereiche, sechs Module")

PERSONALE_MODULE = [
    {
        "nr": 1,
        "titel": "Emotionen erkennen und verstehen",
        "text": (
            "Im ersten Modul legen wir den Grundstein für einen souveränen "
            "Umgang mit dem eigenen emotionalen Erleben. Wir beschäftigen "
            "uns damit, wie Emotionen entstehen, was sie ausmacht und "
            "welchen Sinn und Zweck sie erfüllen. Darauf aufbauend "
            "betrachten wir, welchen Einfluss Emotionen auf unser Verhalten "
            "haben und welche uns besonders häufig im Schulalltag begegnen."
        ),
    },
    {
        "nr": 2,
        "titel": "Emotionen regulieren",
        "text": (
            "Im zweiten Modul widmen wir uns der Frage, wie es gelingen "
            "kann, auch in fordernden Momenten handlungsfähig zu bleiben. "
            "Konkret betrachten wir auf Basis des bereits angeeigneten "
            "Verständnisses zum Thema Emotionen verschiedene Strategien "
            "zur Emotionsregulation im Schulalltag."
        ),
    },
    {
        "nr": 3,
        "titel": "Achtsamkeit und Commitment",
        "text": (
            "Im dritten Modul behandeln wir verschiedene Ansätze, um "
            "Achtsamkeit im Schulalltag zu üben und Akzeptanz für "
            "belastende Gedanken und Emotionen zu erreichen. Darüber "
            "hinaus laden wir die teilnehmenden Lehrkräfte dazu ein, ihre "
            "individuellen berufsbezogenen Werte zu reflektieren und "
            "erarbeiten auf dieser Basis Möglichkeiten, ihr berufliches "
            "Handeln (wieder) an ebendiesen Werten auszurichten."
        ),
    },
]

SOZIALE_MODULE = [
    {
        "nr": 4,
        "titel": "Perspektivübernahme",
        "text": (
            "Im vierten Modul richten wir unseren Blick auf die "
            "häufigsten Interaktionspartner:innen im schulischen Alltag: "
            "die Schüler:innen. Wir betrachten Möglichkeiten, ihre "
            "Perspektive einzunehmen und ihre Handlungen nachzuvollziehen, "
            "um Ansatzpunkte für eine gelingende Verständigung im "
            "Unterricht und darüber hinaus zu finden."
        ),
    },
    {
        "nr": 5,
        "titel": "Beziehungsgestaltung",
        "text": (
            "Im fünften Modul stellen wir die positive Ausgestaltung der "
            "Lehrkraft-Schüler:innen-Beziehung in den Mittelpunkt, weil "
            "diese eine Grundlage erfolgreichen Lernens darstellt. Wir "
            "besprechen die notwendigen Voraussetzungen für eine "
            "professionelle Wahrnehmung der Lehrkraft-Schüler:innen-"
            "Beziehung und wie der Unterricht so gestaltet werden kann, "
            "dass er die psychologischen Grundbedürfnisse nach Autonomie, "
            "Kompetenz und sozialer Eingebundenheit unterstützt."
        ),
    },
    {
        "nr": 6,
        "titel": "Konflikte konstruktiv lösen",
        "text": (
            "Im sechsten Modul widmen wir uns abschließend dem sozialen "
            "Konflikt, der unweigerlich zum schulischen Alltag dazugehört. "
            "Wir reflektieren die verschiedenen Haltungen gegenüber "
            "Konflikten und die jeweiligen Konsequenzen. Zudem erarbeiten "
            "wir konstruktive Verhaltensmöglichkeiten in der akuten "
            "Konfliktsituation sowie für die nachhaltige Lösung von "
            "Konflikten."
        ),
    },
]


def render_module_card(module, accent):
    st.markdown(
        f"""
        <div class="module-card-wide accent-{accent}">
        <div class="module-card-head">
        <div class="module-card-badge {accent}">{module["nr"]}</div>
        <div class="module-card-title">{module["titel"]}</div>
        </div>
        <div class="module-card-text">{module["text"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


pillar_col1, pillar_col2 = st.columns(2, gap="large")

with pillar_col1:

    with st.container(border=True):

        st.markdown(
            """
            <div class="pillar-header personale">
            <div class="pillar-header-title">Personale Kompetenzen</div>
            <div class="pillar-header-sub">
            In den ersten drei Modulen richten wir den Blick zunächst auf
            die eigene Person: Wir vertiefen unser Verständnis für das
            individuelle emotionale Erleben und stärken die persönliche
            Grundlage für einen souveränen Schulalltag.
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for module in PERSONALE_MODULE:
            render_module_card(module, "personale")

with pillar_col2:

    with st.container(border=True):

        st.markdown(
            """
            <div class="pillar-header soziale">
            <div class="pillar-header-title">Soziale Kompetenzen</div>
            <div class="pillar-header-sub">
            In den folgenden drei Modulen weiten wir den Blick auf die
            tägliche Zusammenarbeit mit den Schüler:innen.
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for module in SOZIALE_MODULE:
            render_module_card(module, "soziale")

st.divider()
