import random

import streamlit as st

from common import (
    ALTER_COLS,
    MIND_COLS,
    SEL_COLS,
    display_tags,
    filter_data,
    get_categories,
    inject_css,
    load_data,
    safe_text,
)

inject_css()

df_res, df_raw = load_data()

# =============================================================================
# SESSION STATE
# =============================================================================

if "random_exercise" not in st.session_state:
    st.session_state.random_exercise = None

# =============================================================================
# HEADER
# =============================================================================

st.title("Übungssammlung")

st.markdown(
    """
    **Sozial-emotionale Kompetenzen mit Kernels unkompliziert in den
    Unterricht integrieren.**
    Kernels sind kompakte, evidenzbasierte Strategien (EASEL-Labor, Harvard),
    die aus der gemeinsamen Kernstruktur führender SEL-Programme destilliert
    und als kurze, in den laufenden Unterricht eingebettete Aktivitäten
    (Spiele, Rituale, Erzählungen) konzipiert sind. Sie adressieren
    übergeordnet sowohl personale als auch soziale Kompetenzen – von
    Emotionsregulation und selbstgesteuerter Aufmerksamkeit bis hin zu
    Perspektivenübernahme, Beziehungsgestaltung und konstruktiver
    Konfliktbewältigung –, ohne ein zusätzliches Curriculum zu erfordern.

    **Vorteile**
    Kernels zeichnen sich durch niedrige Implementationshürden aus: Sie sind
    kostenfrei, flexibel adaptierbar und erfordern minimalen Zeitaufwand.
    Lehrkräfte können gezielt jene Strategien auswählen, die dem aktuellen
    Kompetenzprofil ihrer Lerngruppe entsprechen, ohne ein verpflichtendes
    Gesamtpaket abarbeiten zu müssen.

    **Einschränkungen**
    Kernels sind universelle Praktiken für die breite Schülerschaft und
    ersetzen keine intensive, therapeutisch begleitete Förderung bei
    komplexem sozial-emotionalen Förderbedarf. Ihre Evidenzbasis
    konzentriert sich auf jüngere Schüler:innen bis zur 6. Klassenstufe;
    die Übertragbarkeit auf höhere Sekundarstufen ist entsprechend nicht
    gesichert.

    Finden Sie eine passende Übung für einen konkreten Bedarf – oder lassen
    Sie sich einfach eine Übung vorschlagen.
    """
)

# =============================================================================
# FILTER-PANEL (Hauptbereich)
# =============================================================================
#
# Die Filter sitzen bewusst im Hauptbereich direkt über der Auswahl statt in
# der Seitenleiste (die hier für die Seitennavigation der Website reserviert
# ist), damit Filterung und Ergebnis unmittelbar zusammen sichtbar sind.

with st.container(border=True):

    header_col, reset_col = st.columns([5, 1])

    with header_col:
        st.markdown("**🔍 Suche & Filter**")

    with reset_col:

        if st.button("Zurücksetzen", width="stretch"):

            for widget_key in (
                "filter_search",
                "filter_alter",
                "filter_sel",
                "filter_mind",
            ):
                st.session_state.pop(widget_key, None)

            st.rerun()

    search_term = st.text_input(
        "Suchbegriff",
        placeholder="z. B. Emotionsregulation, Beziehungsaufbau",
        help="Durchsucht Übung, Übersetzung, Kurzbeschreibung, Lernziele und Anwendungsfälle.",
        key="filter_search",
    )

    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        selected_alter = st.multiselect(
            "Altersstufe", list(ALTER_COLS.keys()), key="filter_alter"
        )

    with filter_col2:
        selected_sel = st.multiselect(
            "SEL-Komponente", list(SEL_COLS.keys()), key="filter_sel"
        )

    with filter_col3:
        selected_mind = st.multiselect(
            "Achtsamkeit", list(MIND_COLS.keys()), key="filter_mind"
        )

df_filtered = filter_data(
    df_raw, selected_alter, selected_sel, selected_mind, search_term
)

# =============================================================================
# TABS
# =============================================================================

tab_discover, tab_search = st.tabs(["Übung entdecken", "Übungen suchen"])

# -----------------------------------------------------------------------
# Tab: Übung entdecken (Zufallsvorschlag)
# -----------------------------------------------------------------------

with tab_discover:

    st.subheader("Was passt heute?")

    st.markdown(
        """
        Sie möchten eine Übung einsetzen, wissen aber noch nicht genau,
        welche? Lassen Sie sich eine Übung aus der Sammlung vorschlagen.
        """
    )

    if st.button("Zufällige Übung auswählen", type="primary"):

        if len(df_filtered) == 0:
            st.warning("Mit den aktuellen Filtern wurden keine Übungen gefunden.")
        else:
            st.session_state.random_exercise = random.randrange(len(df_filtered))

    if st.session_state.random_exercise is not None:

        idx = st.session_state.random_exercise

        if idx < len(df_filtered):

            row = df_filtered.iloc[idx]
            alter, sel, mind = get_categories(row)

            st.markdown(
                f"""
                <div class="random-box">
                <div class="random-label">Vorschlag aus der Übungssammlung</div>
                <div class="random-title">{safe_text(row, "Übung")}</div>
                <div class="exercise-subtitle">{safe_text(row, "Übersetzung")}</div>
                <div class="metadata">Dauer: {safe_text(row, "Dauer") or "–"}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Altersstufen**")
                st.markdown(display_tags(alter), unsafe_allow_html=True)

            with col2:
                st.markdown("**SEL-Komponenten**")
                st.markdown(display_tags(sel), unsafe_allow_html=True)

            if mind:
                st.markdown("**Achtsamkeit**")
                st.markdown(display_tags(mind), unsafe_allow_html=True)

            st.divider()

            st.markdown("### Kurzbeschreibung")
            st.markdown(safe_text(row, "Kurzbeschreibung") or "Keine Beschreibung vorhanden.")

            with st.expander("Lernziele", expanded=True):
                st.markdown(safe_text(row, "Lernziele") or "Keine Angaben vorhanden.")

            with st.expander("Material"):
                st.markdown(safe_text(row, "Material") or "Keine Angaben vorhanden.")

            with st.expander("Anwendungsfälle"):
                st.markdown(safe_text(row, "Anwendungsfälle") or "Keine Angaben vorhanden.")

            with st.expander("Durchführung"):

                before = safe_text(row, "Vorher")
                during = safe_text(row, "Währenddessen")
                after = safe_text(row, "Nachher")

                if before:
                    st.markdown("**Vorher – Vorbereitung**")
                    st.markdown(before)

                if during:
                    st.markdown("**Währenddessen – Durchführung**")
                    st.markdown(during)

                if after:
                    st.markdown("**Nachher – Abschluss**")
                    st.markdown(after)

# -----------------------------------------------------------------------
# Tab: Übungen suchen
# -----------------------------------------------------------------------

with tab_search:

    st.subheader("Übungen suchen")

    st.caption(f"{len(df_filtered)} Übung(en) entsprechen den aktuellen Kriterien.")

    if len(df_filtered) == 0:
        st.info("Keine Übungen entsprechen den aktuellen Filtereinstellungen.")

    else:

        exercise_options = list(range(len(df_filtered)))

        selected_idx = st.selectbox(
            "Übung auswählen",
            exercise_options,
            index=0,
            format_func=lambda i: safe_text(df_filtered.iloc[i], "Übung") or "Ohne Titel",
        )

        row = df_filtered.iloc[selected_idx]
        alter, sel, mind = get_categories(row)

        st.markdown(
            f"""
            <div class="exercise-card">
            <div class="exercise-title">{safe_text(row, "Übung")}</div>
            <div class="exercise-subtitle">{safe_text(row, "Übersetzung")}</div>
            <div class="metadata">Dauer: {safe_text(row, "Dauer") or "–"}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Altersstufen**")
            st.markdown(display_tags(alter), unsafe_allow_html=True)

        with col2:
            st.markdown("**SEL-Komponenten**")
            st.markdown(display_tags(sel), unsafe_allow_html=True)

        with col3:
            st.markdown("**Achtsamkeit**")
            st.markdown(display_tags(mind), unsafe_allow_html=True)

        st.divider()

        st.markdown("### Kurzbeschreibung")
        st.markdown(safe_text(row, "Kurzbeschreibung") or "Keine Beschreibung vorhanden.")

        with st.expander("Lernziele", expanded=True):
            st.markdown(safe_text(row, "Lernziele") or "Keine Angaben vorhanden.")

        with st.expander("Material"):
            st.markdown(safe_text(row, "Material") or "Keine Angaben vorhanden.")

        with st.expander("Anwendungsfälle"):
            st.markdown(safe_text(row, "Anwendungsfälle") or "Keine Angaben vorhanden.")

        with st.expander("Durchführung"):

            before = safe_text(row, "Vorher")
            during = safe_text(row, "Währenddessen")
            after = safe_text(row, "Nachher")

            if before:
                st.markdown("**Vorher – Vorbereitung**")
                st.markdown(before)

            if during:
                st.markdown("**Währenddessen – Durchführung**")
                st.markdown(during)

            if after:
                st.markdown("**Nachher – Abschluss**")
                st.markdown(after)
