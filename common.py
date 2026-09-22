"""
Gemeinsame Daten-, Filter- und Style-Logik der Fortbildungs-Website.

Wird von allen Seiten unter views/ importiert. So existiert jede Funktion
(Datenladen, Filterung, Tag-Rendering, CSS) nur an einer Stelle und
Änderungen (z. B. an ALTER_COLS) wirken automatisch überall.
"""

from pathlib import Path

import pandas as pd
import streamlit as st

# =============================================================================
# 1. DATENQUELLE
# =============================================================================

DATA_FILE = Path(__file__).parent / "Übungssammlung_GGIE.xlsx"


@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        # Fallback: falls der Dateiname erneut abweicht, wird jede
        # vorhandene .xlsx im Projektverzeichnis als Datenquelle akzeptiert.
        candidates = sorted(Path(__file__).parent.glob("*.xlsx"))
        if not candidates:
            raise FileNotFoundError(
                f"Keine Excel-Datei gefunden. Erwartet wurde: {DATA_FILE.name}"
            )
        data_file = candidates[0]
    else:
        data_file = DATA_FILE

    df_res = pd.read_excel(data_file, sheet_name="Tabelle1")
    df_raw = pd.read_excel(data_file, sheet_name="Tabelle2")

    # Spaltennamen von versehentlichen Leerzeichen befreien.
    df_res.columns = df_res.columns.str.strip()
    df_raw.columns = df_raw.columns.str.strip()

    return df_res, df_raw


# =============================================================================
# 2. SPALTEN-MAPPINGS (Übungssammlung)
# =============================================================================
#
# WICHTIG: Der Key ist das UI-Label (Filter, Tags), der Value MUSS exakt
# dem Spaltennamen in Tabelle2 entsprechen.

ALTER_COLS = {
    "Kindergarten / frühe GS": "Kindergarten, frühe Grundschule",
    "Späte GS": "Späte Grundschule",
    "Sek I": "Sekundarstufe I",
    "Sek II": "Sekundarstufe II",
    "Hochschule": "Hochschule",
    "Lehrkräfte": "Lehrkräfte",
}

SEL_COLS = {
    "Self-Awareness": "Self-Awareness",
    "Self-Management": "Self-Management",
    "Social Awareness": "Social Awareness",
    "Relationship Skills": "Relationship Skills",
    "Resp. Decision-Making": "Resp. Decision-Making",
}

MIND_COLS = {
    "Open Awareness": "Open Awareness",
    "Non-Judgment": "Non-Judgment",
    "Focused Attention": "Focused Attention",
}

TEXT_COLUMNS = [
    "Übung",
    "Übersetzung",
    "Kurzbeschreibung",
    "Lernziele",
    "Anwendungsfälle",
]

RESOURCE_COLUMNS = [
    "Name",
    "Description",
    "PAGE URL",
]

# =============================================================================
# 3. HELFERFUNKTIONEN (Übungssammlung)
# =============================================================================


def is_marked(value):
    """Robuste Prüfung auf '1'/aktiv, unabhängig vom Excel-Zelltyp
    (int, float, str oder bool)."""

    if pd.isna(value):
        return False

    if isinstance(value, str):
        return value.strip() == "1"

    return value == 1


def safe_text(row, column):
    """Safely retrieve a text value from a row."""

    if column not in row.index:
        return ""

    value = row[column]

    if pd.isna(value):
        return ""

    return str(value).strip()


def get_categories(row):

    alter = [
        label
        for label, column in ALTER_COLS.items()
        if column in row.index and is_marked(row[column])
    ]

    sel = [
        label
        for label, column in SEL_COLS.items()
        if column in row.index and is_marked(row[column])
    ]

    mind = [
        label
        for label, column in MIND_COLS.items()
        if column in row.index and is_marked(row[column])
    ]

    return alter, sel, mind


def filter_data(df_raw, selected_alter, selected_sel, selected_mind, search_term):

    df_raw = df_raw.copy()

    # -------------------------------------------------------------------
    # Altersstufen
    # -------------------------------------------------------------------

    if selected_alter:

        columns = [
            ALTER_COLS[x] for x in selected_alter if ALTER_COLS[x] in df_raw.columns
        ]

        if columns:
            mask = df_raw[columns].map(is_marked).any(axis=1)
            df_raw = df_raw[mask]

    # -------------------------------------------------------------------
    # SEL
    # -------------------------------------------------------------------

    if selected_sel:

        columns = [SEL_COLS[x] for x in selected_sel if SEL_COLS[x] in df_raw.columns]

        if columns:
            mask = df_raw[columns].map(is_marked).any(axis=1)
            df_raw = df_raw[mask]

    # -------------------------------------------------------------------
    # Achtsamkeit
    # -------------------------------------------------------------------

    if selected_mind:

        columns = [
            MIND_COLS[x] for x in selected_mind if MIND_COLS[x] in df_raw.columns
        ]

        if columns:
            mask = df_raw[columns].map(is_marked).any(axis=1)
            df_raw = df_raw[mask]

    # -------------------------------------------------------------------
    # Volltextsuche
    # -------------------------------------------------------------------

    if search_term:

        term = search_term.lower()

        available_columns = [x for x in TEXT_COLUMNS if x in df_raw.columns]

        if available_columns:

            mask = (
                df_raw[available_columns]
                .fillna("")
                .astype(str)
                .apply(
                    lambda s: s.str.lower().str.contains(term, regex=False, na=False)
                )
                .any(axis=1)
            )

            df_raw = df_raw[mask]

    return df_raw.reset_index(drop=True)


def display_tags(labels):

    if not labels:
        return "–"

    return "  ".join([f'<span class="tag">{label}</span>' for label in labels])


# =============================================================================
# 4. INHALTE DER FORTBILDUNG
# =============================================================================
#
# Zentrale, editierbare Inhaltsbasis für die Programmseiten. Modul 6 ist
# gemäß aktuellem Bearbeitungsstand vollständig ausgearbeitet; Module 1–5
# sind hier als kurze Arbeitsstände hinterlegt und sollten durch die
# jeweiligen Sitzungspläne ersetzt werden, sobald diese vorliegen.

MODULES = [
    {
        "nr": 1,
        "bereich": "Personale Kompetenzen",
        "titel": "Emotionen erkennen und verstehen",
        "kurz": "Im ersten Modul legen wir den Grundstein für einen souveränen" 
        "Umgang mit dem eigenen emotionalen Erleben. Wir beschäftigen uns damit," 
        "wie Emotionen entstehen, was sie ausmacht und welchen Sinn und Zweck sie" 
        "erfüllen. Darauf aufbauend betrachten wir, welchen Einfluss Emotionen auf" 
        "unser Verhalten haben und welche uns besonders häufig im Schulalltag begegnen.",
        "status": "in Entwicklung",
    },
    {
        "nr": 2,
        "bereich": "Personale Kompetenzen",
        "titel": "Emotionen regulieren",
        "kurz": "Im zweiten Modul widmen wir uns der Frage, wie es gelingen kann," 
        "auch in fordernden Momenten handlungsfähig zu bleiben. Konkret betrachten wir"
        "auf Basis des bereits angeeigneten Verständnisses zum Thema Emotionen "
        "verschiedene Strategien zur Emotionsregulation im Schulalltag.",
        "status": "in Entwicklung",
    },
    {
        "nr": 3,
        "bereich": "Personale Kompetenzen",
        "titel": "Achtsamkeit und Commitment",
        "kurz": "Im dritten Modul behandeln wir verschiedene Ansätze, um Achtsamkeit"
        "im Schulalltag zu üben und Akzeptanz für belastende Gedanken und Emotionen zu" 
        "erreichen. Darüber hinaus  laden wir die teilnehmenden Lehrkräfte dazu ein," 
        "ihre individuellen berufsbezogenen Werte zu reflektieren und erarbeiten auf"
        "dieser Basis Möglichkeiten, ihr berufliches Handeln (wieder) an ebendiesen" 
        "Werten auszurichten.",
        "status": "in Entwicklung",
    },
    {
        "nr": 4,
        "bereich": "Soziale Kompetenzen",
        "titel": "Perspektivübernahme",
        "kurz": "Im vierten Modul richten wir unseren Blick auf die häufigsten" 
        "Interaktionspartner:innen im schulischen Alltag: die Schüler:innen. Wir" 
        "betrachten Möglichkeiten, ihre Perspektive einzunehmen und ihre Handlungen" 
        "nachzuvollziehen, um Ansatzpunkte für eine gelingende Verständigung im"
        "Unterricht und darüber hinaus zu finden.",
        "status": "in Entwicklung",
    },
    {
        "nr": 5,
        "bereich": "Soziale Kompetenzen",
        "titel": "Beziehungsgestaltung",
        "kurz": "Im fünften Modul stellen wir positive Ausgestaltung der" 
        "Lehrkraft-Schüler:innen-Beziehung in den Mittelpunkt, weil diese eine"
        "Grundlage erfolgreichen Lernens darstellt. Wir besprechen die notwendigen"
        "Voraussetzungen für eine professionelle Wahrnehmung der"
        "Lehrkraft-Schüler:innen-Beziehung und wie der Unterricht so gestaltet" 
        "werden kann, dass er die  psychologischen Grundbedürfnisse nach" 
        "Autonomie, Kompetenz und sozialer Eingebundenheit unterstützt.",
        "status": "in Entwicklung",
    },
    {
        "nr": 6,
        "bereich": "Soziale Kompetenzen",
        "titel": "Konflikte konstruktiv lösen",
        "kurz": "Im fünften Modul stellen wir positive Ausgestaltung der" 
        "Lehrkraft-Schüler:innen-Beziehung in den Mittelpunkt, weil diese eine" 
        "Grundlage erfolgreichen Lernens darstellt. Wir besprechen die notwendigen" 
        "Voraussetzungen für eine professionelle Wahrnehmung der Lehrkraft-Schüler:innen-Beziehung" 
        "und wie der Unterricht so gestaltet werden kann, dass er die  psychologischen" 
        "Grundbedürfnisse nach Autonomie, Kompetenz und sozialer Eingebundenheit unterstützt.",
        "status": "vollständig ausgearbeitet",
    },
]


# =============================================================================
# 5. CSS
# =============================================================================


def inject_css():
    st.markdown(
        """
        <style>

        /* Main content */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 4rem;
            max-width: 1400px;
        }

        /* Farbpalette – konsistent mit den Fortbildungsfolien (Salbeigrün/Schiefer) */
        :root {
            --sek-sage: #7C9885;
            --sek-sage-soft: rgba(124, 152, 133, 0.14);
            --sek-slate: #4B5563;
        }

        /* Exercise cards */
        .exercise-card {
            padding: 1.4rem 1.6rem;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.25);
            margin-bottom: 1rem;
            background-color: rgba(128,128,128,0.04);
        }

        .exercise-title {
            font-size: 1.35rem;
            font-weight: 650;
            margin-bottom: 0.4rem;
        }

        .exercise-subtitle {
            color: rgba(128,128,128,1);
            margin-bottom: 0.8rem;
        }

        /* Tags – rein informativ, bewusst NICHT im Pill-/Button-Stil,
           damit sie sich klar von echten interaktiven Elementen
           unterscheiden. */
        .tag {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            margin-right: 0.3rem;
            margin-bottom: 0.3rem;
            border-radius: 4px;
            font-size: 0.78rem;
            background-color: rgba(128,128,128,0.14);
            cursor: default;
            pointer-events: none;
        }

        /* Random exercise box */
        .random-box {
            padding: 1.8rem;
            border-radius: 14px;
            border: 1px solid rgba(128,128,128,0.3);
            background-color: rgba(128,128,128,0.05);
            margin: 1rem 0 1.5rem 0;
        }

        .random-label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: rgba(128,128,128,1);
        }

        .random-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin: 0.3rem 0 0.7rem 0;
        }

        /* Small metadata */
        .metadata {
            color: rgba(128,128,128,1);
            font-size: 0.9rem;
        }

        /* Modulkarten */
        .module-card {
            padding: 1.2rem 1.4rem;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.25);
            border-left: 4px solid var(--sek-sage);
            margin-bottom: 0.9rem;
            background-color: rgba(128,128,128,0.03);
        }

        .module-nr {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--sek-slate);
        }

        .module-title {
            font-size: 1.15rem;
            font-weight: 650;
            margin: 0.15rem 0 0.5rem 0;
        }

        .status-badge {
            display: inline-block;
            padding: 0.15rem 0.55rem;
            border-radius: 4px;
            font-size: 0.72rem;
            margin-bottom: 0.6rem;
            cursor: default;
            pointer-events: none;
        }

        .status-done {
            background-color: var(--sek-sage-soft);
            color: var(--sek-sage);
        }

        .status-progress {
            background-color: rgba(128,128,128,0.14);
            color: rgba(90,90,90,1);
        }

        /* Info-/Dividend-Karten auf Ansatz-Seite */
        .info-card {
            padding: 1.1rem 1.3rem;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.22);
            background-color: rgba(128,128,128,0.03);
            height: 100%;
        }

        .info-card h4 {
            margin-top: 0;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
