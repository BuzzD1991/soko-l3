import random

import streamlit as st

from common import (
    ALTER_COLS,
    display_tags,
    filter_data,
    get_altersstufen,
    inject_css,
    load_data,
    render_quelle,
    safe_html,
    safe_text,
)

inject_css()

df_uebungen = load_data()

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
    **Sozial-emotionale und achtsame Praxis unkompliziert in den Unterricht
    integrieren.**
    Die Sammlung vereint zwei sich ergänzende Quellen: kompakte,
    evidenzbasierte SEL-Kernels (EASEL-Labor, Harvard/Berkeley) sowie
    Achtsamkeits- und Reflexionsübungen aus der Schulpraxis und
    einschlägiger Fachliteratur. Beide Übungstypen sind als kurze, in den
    laufenden Unterricht eingebettete Aktivitäten konzipiert, ohne ein
    zusätzliches Curriculum zu erfordern.

    **Vorteile**
    Die Übungen zeichnen sich durch niedrige Implementationshürden aus:
    Sie sind kostenfrei, flexibel adaptierbar und erfordern minimalen
    Zeitaufwand. Lehrkräfte können gezielt jene Übung auswählen, die der
    Zielgruppe und dem aktuellen Bedarf ihrer Lerngruppe entspricht, ohne
    ein verpflichtendes Gesamtpaket abarbeiten zu müssen.

    **Einschränkungen**
    Die Übungen sind universelle Praktiken für die breite Schülerschaft
    bzw. für Lehrkräfte selbst und ersetzen keine intensive, therapeutisch
    begleitete Förderung bei komplexem sozial-emotionalen Förderbedarf.
    Für welche Altersstufe und Zielgruppe eine Übung geeignet ist, ist
    jeweils direkt bei der Übung vermerkt.

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

            for widget_key in ("filter_search", "filter_alter"):
                st.session_state.pop(widget_key, None)

            st.rerun()

    search_col, alter_col = st.columns([3, 2])

    with search_col:
        search_term = st.text_input(
            "Suchbegriff",
            placeholder="z. B. Achtsamkeit, Beziehungsaufbau",
            help="Durchsucht Übung, Kurzbeschreibung, Zielgruppe, Lernziele und Anwendungsfälle.",
            key="filter_search",
        )

    with alter_col:
        selected_alter = st.multiselect(
            "Altersstufe", list(ALTER_COLS.keys()), key="filter_alter"
        )

df_filtered = filter_data(df_uebungen, selected_alter, search_term)

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
            alter = get_altersstufen(row)

            st.markdown(
                f"""
                <div class="random-box">
                <div class="random-label">Vorschlag aus der Übungssammlung</div>
                <div class="random-title">{safe_html(row, "Übung")}</div>
                <div class="metadata">Dauer: {safe_html(row, "Dauer (ca.)") or "–"}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns([1, 2])

            with col1:
                st.markdown("**Altersstufen**")
                st.markdown(display_tags(alter), unsafe_allow_html=True)

            with col2:
                st.markdown("**Zielgruppe**")
                st.markdown(safe_text(row, "Zielgruppe") or "–")

            st.divider()

            st.markdown("### Kurzbeschreibung")
            st.markdown(
                safe_text(row, "Kurzbeschreibung der Übung")
                or "Keine Beschreibung vorhanden."
            )

            with st.expander("Lernziele", expanded=True):
                st.markdown(safe_text(row, "Lernziele") or "Keine Angaben vorhanden.")

            with st.expander("Material"):
                st.markdown(
                    safe_text(row, "Benötigtes Material") or "Keine Angaben vorhanden."
                )

            with st.expander("Anwendungsfälle"):
                st.markdown(safe_text(row, "Anwendungsfälle") or "Keine Angaben vorhanden.")

            with st.expander("Durchführung"):

                before = safe_text(row, "Vor der Übung")
                during = safe_text(row, "Während der Übung")
                after = safe_text(row, "Nach der Übung (ggf. Reflexion)")

                if before:
                    st.markdown("**Vorher – Vorbereitung**")
                    st.markdown(before)

                if during:
                    st.markdown("**Während der Übung**")
                    st.markdown(during)

                if after:
                    st.markdown("**Nachher – Reflexion**")
                    st.markdown(after)

            with st.expander("Quelle"):
                st.markdown(render_quelle(row))

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
        alter = get_altersstufen(row)

        st.markdown(
            f"""
            <div class="exercise-card">
            <div class="exercise-title">{safe_html(row, "Übung")}</div>
            <div class="metadata">Dauer: {safe_html(row, "Dauer (ca.)") or "–"}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("**Altersstufen**")
            st.markdown(display_tags(alter), unsafe_allow_html=True)

        with col2:
            st.markdown("**Zielgruppe**")
            st.markdown(safe_text(row, "Zielgruppe") or "–")

        st.divider()

        st.markdown("### Kurzbeschreibung")
        st.markdown(
            safe_text(row, "Kurzbeschreibung der Übung")
            or "Keine Beschreibung vorhanden."
        )

        with st.expander("Lernziele", expanded=True):
            st.markdown(safe_text(row, "Lernziele") or "Keine Angaben vorhanden.")

        with st.expander("Material"):
            st.markdown(
                safe_text(row, "Benötigtes Material") or "Keine Angaben vorhanden."
            )

        with st.expander("Anwendungsfälle"):
            st.markdown(safe_text(row, "Anwendungsfälle") or "Keine Angaben vorhanden.")

        with st.expander("Durchführung"):

            before = safe_text(row, "Vor der Übung")
            during = safe_text(row, "Während der Übung")
            after = safe_text(row, "Nach der Übung (ggf. Reflexion)")

            if before:
                st.markdown("**Vorher – Vorbereitung**")
                st.markdown(before)

            if during:
                st.markdown("**Während der Übung**")
                st.markdown(during)

            if after:
                st.markdown("**Nachher – Reflexion**")
                st.markdown(after)

        with st.expander("Quelle"):
            st.markdown(render_quelle(row))
