"""
Gemeinsame Daten-, Filter- und Style-Logik der Fortbildungs-Website.

Wird von allen Seiten unter views/ importiert. So existiert jede Funktion
(Datenladen, Filterung, Tag-Rendering, CSS) nur an einer Stelle und
Änderungen (z. B. an ALTER_COLS) wirken automatisch überall.

Datengrundlage (Stand: überarbeitete Übungssammlung): Die Excel-Datei
besteht aus zwei Tabellenblättern, die über die Spalte "Übung" 1:1
zusammengehören:

- "Übersicht"      – eine Zeile je Übung mit Kurzbeschreibung, Dauer,
                      Zielgruppe, Altersstufen-Markierungen (0/1),
                      Anwendungsfällen, Material, Lernzielen sowie den
                      Quellenangaben (Internetquelle/Originalquelle).
- "Übungsabläufe"  – die ausführliche Anleitung je Übung in drei Phasen
                      (Vor der Übung / Während der Übung / Nach der
                      Übung).

load_data() führt beide Blätter zu einer einzigen Tabelle zusammen, damit
der Rest des Codes (Filter, Kartenanzeige) mit genau einer Zeile pro
Übung arbeiten kann.
"""

import html
from pathlib import Path

import pandas as pd
import streamlit as st

# =============================================================================
# 1. DATENQUELLE
# =============================================================================

DATA_FILE = Path(__file__).parent / "Website_Übungssammlung.xlsx"


def resolve_data_file():
    """Ermittelt die zu ladende Excel-Datei.

    Weicht der tatsächliche Dateiname ab (z. B. durch eine abweichende
    Unicode-Normalisierung des "Ü" beim Hochladen auf manchen Servern),
    wird ersatzweise die zuletzt geänderte .xlsx im Verzeichnis
    verwendet – nicht die alphabetisch erste. Das verhindert, dass eine
    ältere, liegen gebliebene Excel-Datei stillschweigend Vorrang vor der
    aktuellen bekommt.
    """

    if DATA_FILE.exists():
        return DATA_FILE

    candidates = sorted(
        Path(__file__).parent.glob("*.xlsx"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    if not candidates:
        raise FileNotFoundError(
            f"Keine Excel-Datei gefunden. Erwartet wurde: {DATA_FILE.name}"
        )

    return candidates[0]


@st.cache_data
def load_data_cached(file_path, file_mtime):
    # file_mtime fließt NUR in den Cache-Key ein (st.cache_data cached nach
    # Funktionsargumenten). Wird die Excel-Datei auf dem Server ausgetauscht,
    # ändert sich ihr Änderungsdatum automatisch mit – Streamlit erkennt
    # dadurch von selbst, dass neu geladen werden muss, auch ohne manuelles
    # "Clear cache" / Neustart der App.

    # Kopfzeile steht in Zeile 3 (0-indexiert: header=2), Daten ab Zeile 4 –
    # beide Blätter beginnen mit zwei einleitenden Zeilen (Titel, Hinweis).
    df_overview = pd.read_excel(file_path, sheet_name="Übersicht", header=2)
    df_steps = pd.read_excel(file_path, sheet_name="Übungsabläufe", header=2)

    df_overview.columns = df_overview.columns.str.strip()
    df_steps.columns = df_steps.columns.str.strip()

    df_overview["Übung"] = df_overview["Übung"].astype(str).str.strip()
    df_steps["Übung"] = df_steps["Übung"].astype(str).str.strip()

    # Zusammenführen auf Basis der Übungsbezeichnung. "left", damit eine
    # Übung auch ohne hinterlegten Ablauf in der Sammlung erscheint (mit
    # leeren Durchführungs-Feldern) statt stillschweigend zu verschwinden.
    df_uebungen = df_overview.merge(
        df_steps, on="Übung", how="left", validate="one_to_one"
    )

    return df_uebungen.reset_index(drop=True)


def load_data():
    data_file = resolve_data_file()
    return load_data_cached(str(data_file), data_file.stat().st_mtime)


# =============================================================================
# 2. SPALTEN-MAPPINGS (Übungssammlung)
# =============================================================================
#
# WICHTIG: Der Key ist das UI-Label (Filter, Tags), der Value MUSS exakt
# dem Spaltennamen im Tabellenblatt "Übersicht" entsprechen.

ALTER_COLS = {
    "Grundschule": "Grundschule",
    "Sekundarstufe I": "Sekundarstufe I",
    "Sekundarstufe II": "Sekundarstufe II",
}

# SEL-Komponenten nach dem CASEL-Modell, in der überarbeiteten Datei bereits
# deutschsprachig benannt (Spaltenname = Anzeigename).
SEL_COLS = {
    "Emotionswissen": "Emotionswissen",
    "Emotionsregulation": "Emotionsregulation",
    "Soziales Wissen": "Soziales Wissen",
    "Beziehungsfertigkeiten": "Beziehungsfertigkeiten",
    "Verantwortungsvolle Entscheidungsfindung": "Verantwortungsvolle Entscheidungsfindung",
}

TEXT_COLUMNS = [
    "Übung",
    "Kurzbeschreibung der Übung",
    "Zielgruppe",
    "Lernziele",
    "Anwendungsfälle",
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


def safe_html(row, column):
    """Wie safe_text, aber HTML-escaped – für die Verwendung in
    unsafe_allow_html=True-Blöcken, damit z. B. ein "<" oder "&" in einer
    künftigen Dateneingabe das Karten-Markup nicht zerstört."""

    return html.escape(safe_text(row, column))


def get_tags(row, cols_dict):
    """Liefert die Liste der für diese Übung markierten Labels aus einem
    Spalten-Mapping (z. B. ALTER_COLS oder SEL_COLS)."""

    return [
        label
        for label, column in cols_dict.items()
        if column in row.index and is_marked(row[column])
    ]


def get_altersstufen(row):
    """Liefert die Liste der für diese Übung markierten Altersstufen."""

    return get_tags(row, ALTER_COLS)


def get_sel_komponenten(row):
    """Liefert die Liste der für diese Übung markierten SEL-Komponenten."""

    return get_tags(row, SEL_COLS)


def _filter_by_tags(df_uebungen, selected_labels, cols_dict):
    """Filtert df_uebungen auf Zeilen, bei denen mindestens eine der
    ausgewählten Spalten aus cols_dict markiert ist (ODER-Verknüpfung
    innerhalb einer Filterdimension)."""

    if not selected_labels:
        return df_uebungen

    columns = [
        cols_dict[x] for x in selected_labels if cols_dict[x] in df_uebungen.columns
    ]

    if not columns:
        return df_uebungen

    mask = df_uebungen[columns].map(is_marked).any(axis=1)
    return df_uebungen[mask]


def filter_data(df_uebungen, selected_alter, selected_sel, search_term):

    df_uebungen = df_uebungen.copy()

    # -------------------------------------------------------------------
    # Altersstufen
    # -------------------------------------------------------------------

    df_uebungen = _filter_by_tags(df_uebungen, selected_alter, ALTER_COLS)

    # -------------------------------------------------------------------
    # SEL-Komponenten
    # -------------------------------------------------------------------

    df_uebungen = _filter_by_tags(df_uebungen, selected_sel, SEL_COLS)

    # -------------------------------------------------------------------
    # Volltextsuche
    # -------------------------------------------------------------------

    if search_term:

        term = search_term.lower()

        available_columns = [x for x in TEXT_COLUMNS if x in df_uebungen.columns]

        if available_columns:

            mask = (
                df_uebungen[available_columns]
                .fillna("")
                .astype(str)
                .apply(
                    lambda s: s.str.lower().str.contains(term, regex=False, na=False)
                )
                .any(axis=1)
            )

            df_uebungen = df_uebungen[mask]

    return df_uebungen.reset_index(drop=True)


def display_tags(labels):

    if not labels:
        return "–"

    return "  ".join([f'<span class="tag">{label}</span>' for label in labels])


def render_quelle(row):
    """Baut die Quellenangabe einer Übung (Link + Originalquelle) als
    Markdown. Fehlt eine der beiden Angaben, wird nur die vorhandene
    gezeigt; fehlen beide, ein neutraler Hinweistext."""

    url = safe_text(row, "Internetquelle")
    original = safe_text(row, "Originalquelle")

    parts = []

    if url:
        parts.append(f"🔗 [{url}]({url})")

    if original:
        parts.append(f"📖 {original}")

    if not parts:
        return "Keine Angaben vorhanden."

    return "  \n".join(parts)


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
        "titel": "Emotionswahrnehmung und -verstehen",
        "kurz": "Eigene Emotionen differenziert wahrnehmen, benennen und "
        "einordnen können – als Grundlage für Ko-Regulation im Klassenraum.",
        "status": "in Entwicklung",
    },
    {
        "nr": 2,
        "bereich": "Personale Kompetenzen",
        "titel": "Emotionsregulation",
        "kurz": "Handhabbare Strategien zur Regulation eigener Emotionen in "
        "belastenden Unterrichtssituationen – ressourcenorientiert statt "
        "reiner Stressvermeidung.",
        "status": "in Entwicklung",
    },
    {
        "nr": 3,
        "bereich": "Personale Kompetenzen",
        "titel": "Achtsamkeit und Wertorientierung",
        "kurz": "Achtsamkeitsbasierte Übungen und Werteklärung nach dem "
        "Ansatz der Akzeptanz- und Commitment-Therapie (ACT), um "
        "professionelles Handeln nachhaltig zu verankern.",
        "status": "in Entwicklung",
    },
    {
        "nr": 4,
        "bereich": "Soziale Kompetenzen",
        "titel": "Perspektivübernahme und Empathie",
        "kurz": "Empathische Perspektivübernahme gegenüber Schüler:innen als "
        "Grundlage für responsives, entwicklungsförderndes pädagogisches "
        "Handeln.",
        "status": "in Entwicklung",
    },
    {
        "nr": 5,
        "bereich": "Soziale Kompetenzen",
        "titel": "Beziehungsorientierter Unterricht",
        "kurz": "Aufbau tragfähiger Lehrkraft-Schüler:innen-Beziehungen als "
        "Schutzfaktor – mit besonderer Relevanz für Schüler:innen mit "
        "hohen Bildungsrisiken.",
        "status": "in Entwicklung",
    },
    {
        "nr": 6,
        "bereich": "Soziale Kompetenzen",
        "titel": "Konstruktive Konfliktbewältigung",
        "kurz": "Haltungs- und beziehungsorientierter Ansatz (Deeskalation "
        "vor Klärung) statt Technikzentrierung, mit durchgehendem "
        "Fallbeispiel. 120-minütiges Online-Modul in vier Blöcken: "
        "Konfliktdefinition, akute Konfliktsituation, Notfall-Deeskalation, "
        "ruhige Klärung.",
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
            --sek-slate-soft: rgba(75, 85, 99, 0.14);
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

        /* Info-/Dividend-Karten auf Ansatz-Seite, auch für die Hinweise-Seite
           genutzt */
        .info-card {
            padding: 1.1rem 1.3rem;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.22);
            background-color: rgba(128,128,128,0.03);
            height: 100%;
            margin-bottom: 0.9rem;
        }

        .info-card h4 {
            margin-top: 0;
        }

        /* Kompetenzbereich-Banner (Startseite) – deutliche Trennung der
           beiden Inhaltsbereiche über kräftige Farbflächen statt nur Text. */
        .pillar-header {
            padding: 1.1rem 1.4rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: #ffffff;
        }

        .pillar-header.personale {
            background-color: var(--sek-sage);
        }

        .pillar-header.soziale {
            background-color: var(--sek-slate);
        }

        .pillar-header-title {
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .pillar-header-sub {
            font-size: 0.9rem;
            opacity: 0.92;
            line-height: 1.4;
        }

        /* Modulkarten mit ausführlichem Fließtext (Startseite) */
        .module-card-wide {
            padding: 1.2rem 1.4rem;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.2);
            background-color: rgba(128,128,128,0.025);
            margin-bottom: 0.9rem;
        }

        .module-card-wide.accent-personale {
            border-left: 5px solid var(--sek-sage);
        }

        .module-card-wide.accent-soziale {
            border-left: 5px solid var(--sek-slate);
        }

        .module-card-head {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin-bottom: 0.55rem;
        }

        .module-card-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 1.9rem;
            height: 1.9rem;
            min-width: 1.9rem;
            border-radius: 50%;
            font-size: 0.85rem;
            font-weight: 700;
            color: #ffffff;
        }

        .module-card-badge.personale {
            background-color: var(--sek-sage);
        }

        .module-card-badge.soziale {
            background-color: var(--sek-slate);
        }

        .module-card-title {
            font-size: 1.05rem;
            font-weight: 650;
        }

        .module-card-text {
            color: rgba(55,55,55,0.92);
            line-height: 1.55;
            font-size: 0.94rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
