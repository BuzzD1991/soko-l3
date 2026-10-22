import streamlit as st

from common import inject_css

inject_css()

st.title("Hinweise für Lehrkräfte")

st.markdown(
    """
    Die einzelnen Übungen wirken am besten, wenn sie in einen größeren
    Rahmen eingebettet sind. Die folgenden beiden Impulse sind deshalb
    nicht an eine konkrete Übung gebunden, sondern zeigen übergreifend,
    wie das Gelernte nachbesprochen und dauerhaft im Schulalltag verankert
    werden kann.
    """
)

st.divider()

# =============================================================================
# 1. NACHBESPRECHUNG ANLEITEN
# =============================================================================

st.subheader("1. Eine Übung nachbesprechen")

st.markdown(
    """
    Eine Übung wirkt stärker, wenn sie nicht für sich steht, sondern im
    Anschluss kurz reflektiert wird. Moderieren Sie dazu ein Gespräch, das
    die Erfahrung auf die zuvor ausdrücklich vermittelte SEL-Kompetenz
    zurückbezieht – vier aufeinander aufbauende Phasen haben sich dafür
    bewährt.
    """
)

st.info(
    "Je nach Lernvoraussetzungen innerhalb der Gruppe können Anpassungen "
    "nötig sein, damit alle teilnehmen können."
)

REFLECTION_PHASES = [
    {
        "icon": "🌬️",
        "titel": "1. Ankommen",
        "fragen": [
            "Nimm dir einen Moment Zeit und spüre in dich hinein – achte "
            "auf deine Atmung sowie auf Gefühle und Gedanken, die gerade "
            "da sind.",
        ],
    },
    {
        "icon": "💭",
        "titel": "2. Eigene Erfahrung benennen",
        "fragen": [
            "Wie hast du dich bei dieser Aktivität gefühlt, und was hat "
            "dazu geführt?",
            "Was hast du dabei an dir selbst bemerkt?",
        ],
    },
    {
        "icon": "👥",
        "titel": "3. Die Gruppe einbeziehen",
        "fragen": [
            "Wem ging es ähnlich? Wer hat sich vielleicht anders gefühlt?",
            "Was hast du in unserer Gruppe beobachtet, das hilfreich "
            "war – und was eher schwierig?",
        ],
    },
    {
        "icon": "🔗",
        "titel": "4. Transfer herstellen",
        "fragen": [
            "Welche sozial-emotionale Kompetenz haben wir bei dieser "
            "Aktivität eingesetzt?",
            "In welchen Situationen im Schulalltag könnten wir sie "
            "ebenfalls brauchen?",
            "Was könnten wir beim nächsten Mal anders machen?",
        ],
    },
]

def render_phase_card(column, phase):

    fragen_html = "".join(f"<li>{frage}</li>" for frage in phase["fragen"])

    with column:
        st.markdown(
            f"""
            <div class="info-card">
            <h4>{phase["icon"]} {phase["titel"]}</h4>
            <ul style="margin-bottom:0; padding-left:1.1rem;">{fragen_html}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Zeilenweise angeordnet (nicht spaltenweise), damit die Lesereihenfolge
# 1 → 2 → 3 → 4 der Lese-/Klickreihenfolge auf der Seite entspricht.
phase_row1_col1, phase_row1_col2 = st.columns(2)
render_phase_card(phase_row1_col1, REFLECTION_PHASES[0])
render_phase_card(phase_row1_col2, REFLECTION_PHASES[1])

phase_row2_col1, phase_row2_col2 = st.columns(2)
render_phase_card(phase_row2_col1, REFLECTION_PHASES[2])
render_phase_card(phase_row2_col2, REFLECTION_PHASES[3])

st.success(
    "**Reflexionsimpuls für Sie:** Zeigen die Schülerinnen und Schüler "
    "durch diese Nachbesprechungen ein größeres Bewusstsein für "
    "sozial-emotionale Kompetenzen – im Unterricht wie darüber hinaus?"
)

st.divider()

# =============================================================================
# 2. SEL IM SCHULALLTAG VERANKERN
# =============================================================================

st.subheader("2. Sozial-emotionale Kompetenzen im Schulalltag verankern")

st.markdown(
    """
    Das Vermitteln konkreter Kompetenzen ist nur der erste Schritt. Damit
    Schülerinnen und Schüler sie auch im Alltag anwenden und
    verinnerlichen, braucht es Gelegenheiten zum Üben, zum Vorleben und
    zur Anerkennung – im Unterricht wie in der gesamten Schulgemeinschaft.
    """
)

st.info(
    "**Tipp:** Legen Sie einen konkreten Plan mit festen Zeiten und "
    "Unterrichtseinheiten an, mit denen Sie die Anwendung "
    "sozial-emotionaler Kompetenzen im Klassenzimmer und in der gesamten "
    "Schule fördern möchten."
)

st.markdown("#### Im Unterricht")

UNTERRICHT_STRATEGIEN = [
    {
        "icon": "🔁",
        "titel": "Beständigkeit",
        "text": (
            "Vermitteln Sie sozial-emotionale Kompetenzen regelmäßig und "
            "konsequent – fest eingeplant im Wochenablauf statt als "
            "Gelegenheitsthema."
        ),
    },
    {
        "icon": "🗣️",
        "titel": "Vorleben und benennen",
        "text": (
            "Nutzen Sie eigene Momente, um eine Kompetenz vorzuleben und "
            "ausdrücklich zu benennen. Beispiel: „Ich bin gerade "
            "verärgert und muss erst ruhig durchatmen, bevor wir "
            "weitermachen.“"
        ),
    },
    {
        "icon": "🤝",
        "titel": "In der Gruppenarbeit üben",
        "text": (
            "Geben Sie neben der fachlichen Aufgabe gezielt eine "
            "SEL-Kompetenz mit, die die Zusammenarbeit verbessert – etwa "
            "aktives Zuhören oder Problemlösung."
        ),
    },
    {
        "icon": "👏",
        "titel": "Anwendung anerkennen",
        "text": (
            "Benennen Sie positive Auswirkungen konkret: „Mir ist "
            "aufgefallen, dass du gerade [Kompetenz] einsetzt – das wird "
            "dir dabei helfen, …“"
        ),
    },
    {
        "icon": "📖",
        "titel": "Verbindung zu Büchern herstellen",
        "text": (
            "Greifen Sie Gefühle aus gelesenen Geschichten auf, z. B.: "
            "„Wie fühlt sich die Figur gerade? Hast du dich auch schon "
            "einmal so gefühlt?“"
        ),
    },
]

def render_strategy_card(column, strategie):

    with column:
        st.markdown(
            f"""
            <div class="info-card">
            <h4>{strategie["icon"]} {strategie["titel"]}</h4>
            {strategie["text"]}
            </div>
            """,
            unsafe_allow_html=True,
        )


# Wieder zeilenweise (nicht spaltenweise) für die korrekte Lesereihenfolge;
# bei fünf Karten bleibt die letzte Spalte der dritten Zeile leer.
strat_row1_col1, strat_row1_col2 = st.columns(2)
render_strategy_card(strat_row1_col1, UNTERRICHT_STRATEGIEN[0])
render_strategy_card(strat_row1_col2, UNTERRICHT_STRATEGIEN[1])

strat_row2_col1, strat_row2_col2 = st.columns(2)
render_strategy_card(strat_row2_col1, UNTERRICHT_STRATEGIEN[2])
render_strategy_card(strat_row2_col2, UNTERRICHT_STRATEGIEN[3])

strat_row3_col1, strat_row3_col2 = st.columns(2)
render_strategy_card(strat_row3_col1, UNTERRICHT_STRATEGIEN[4])

st.markdown("#### In der Schulgemeinschaft")

st.markdown(
    """
    SEL wirkt stärker, wenn es über das einzelne Klassenzimmer
    hinausgeht und von der ganzen Schule mitgetragen wird:
    """
)

schulgemeinschaft_col1, schulgemeinschaft_col2 = st.columns(2)

with schulgemeinschaft_col1:
    st.markdown(
        """
        - **Sichtbarkeit schaffen:** SEL-Begriffe und -Kompetenzen in
          Cafeteria, Eingangsbereich, Sekretariat und auf den Fluren
          sichtbar darstellen.
        - **Unterstützungspersonal einbinden:** Fachkräfte aus anderen
          Bereichen (z. B. Busfahrer:innen, Cafeteria-Personal) nutzen
          ihre besonderen Beziehungen zu den Schüler:innen, um
          Kompetenzen zu stärken – etwa per Daumen-hoch/-runter beim
          Einsteigen in den Bus oder Lob für freundliches Verhalten in
          der Cafeteria.
        - **Pausenspiele nutzen:** Gemeinschaftsfördernde Aktivitäten und
          Spiele in den Pausen einsetzen.
        """
    )

with schulgemeinschaft_col2:
    st.markdown(
        """
        - **Morgendliche Durchsagen nutzen:** SEL-Kompetenzen zum Thema
          machen, z. B. die Schüler:innen ermutigen, im Laufe des Tages
          Empathie füreinander zu zeigen.
        - **Schulhof und Cafeteria einbeziehen:** Schüler:innen
          ermutigen, dort ihre Problemlösefähigkeiten einzusetzen.
        - **Schulweite Anlässe nutzen:** Versammlungen und
          Familientreffen als Gelegenheit, bei der Schüler:innen teilen
          können, was sie gelernt haben.
        """
    )

st.success(
    "**Reflexionsimpuls für Sie:** Bemerken Sie Verbesserungen im Klassen- "
    "oder Schulklima, seit sozial-emotionale Kompetenzen häufiger "
    "angewendet werden?"
)
