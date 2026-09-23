import streamlit as st

from common import inject_css

inject_css()

st.title("Ansatz & Zielgruppe")

# =============================================================================
# ZIELGRUPPE
# =============================================================================

st.subheader("Zielgruppe")

st.markdown(
    """
    Die Fortbildung richtet sich an Lehrkräfte an Schulen in benachteiligten
    Lagen bzw. mit Schülerschaft mit hohen Bildungsrisiken und erfolgt im
    Rahmen des Startchancen-Programms.
    """
)

st.divider()

# =============================================================================
# TRAIN-THE-TEACHER-AS-MULTIPLIER
# =============================================================================

st.subheader("Train-the-Teacher-as-Multiplier")

st.markdown(
    """
    Die Fortbildung folgt einem zweistufigen Modell: Lehrkräfte entwickeln
    zunächst ihre eigenen sozial-emotionalen Kompetenzen, bevor passende 
    Materialien direkt mit der Schülerschaft eingesetzt werden.
    """
)

step_col1, step_col2 = st.columns(2)

with step_col1:
    st.markdown(
        """
        <div class="info-card">
        <h4>Schritt 1 · Stärkung der eigenen sozial-emotionalen Kompetenzten</h4>
        Als Grundlage für ihr professionelles Handeln durchlaufen die Lehrkräfte die sechs Module selbst.
        </div>
        """,
        unsafe_allow_html=True,
    )

with step_col2:
    st.markdown(
        """
        <div class="info-card">
        <h4>Schritt 2 · Übertragung in den Unterricht</h4>
        Über die begleitende Übungssammlung werden passende
        Aktivitäten direkt und niedrigschwellig in den laufenden Unterricht
        eingebettet.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# =============================================================================
# THEORETISCHE FUNDIERUNG
# =============================================================================

st.subheader("Theoretische Fundierung")

st.markdown(
    """
    Zentraler theoretischer Anker ist das *Comprehensive Model of Teacher
    Quality* von Rimm-Kaufman und Hamre (2010): Die sozial-emotionale
    Kompetenz der Lehrkraft selbst wird darin als eigenständiger
    Wirkfaktor für Unterrichtsqualität und Schüler:innen-Entwicklung
    verstanden.

    Investitionen in die sozial-emotionalen Kompetenzen von Lehrkräften zahlen sich dabei potenziell
    in mehreren Bereichen zugleich aus: für die Lehrkraft selbst
    (Wohlbefinden, Beanspruchungserleben), für die Schüler:innen
    (Beziehungsqualität, Lernklima) und für die Schule als System
    (Unterrichtsqualität, Bindung von Personal).
    """
)

with st.expander("Ausgewählte Quellen"):
    st.markdown(
        """
        - Boustani et al. (2015)
        - Kininger et al. (2018)
        - Coleman (2018)
        - Algan & Huillery (2025)
        - Glasl (1997) – Eskalationsstufen von Konflikten
        - Frommeyer-Prozessmodell (Modul 6)
        """
    )

st.divider()

# =============================================================================
# EINORDNUNG & GRENZEN
# =============================================================================

st.subheader("Einordnung & Grenzen")

st.markdown(
    """
    Modulare schulbasierte Interventionen werden in der Forschung nicht
    einhellig bewertet. Kininger et al. (2018) weisen auf reale
    Umsetzungsprobleme bei schulbasierten Fachkräften hin, während Coleman
    (2018) optimistischer zur kulturellen Anpassungsfähigkeit modularer
    Ansätze argumentiert. Die vorliegende Fortbildung ordnet sich
    entsprechend als realistische, empirisch fundierte – aber nicht
    allein hinreichende – Maßnahme ein: Sie ersetzt keine intensive,
    therapeutisch begleitete Förderung bei komplexem sozial-emotionalen
    Förderbedarf.
    """
)
