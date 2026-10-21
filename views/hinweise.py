import streamlit as st

from common import inject_css

inject_css()

st.title("Hinweise für Lehrkräfte")

st.markdown(
    """
    Die einzelnen Übungen aus der Übungssammlung wirken am besten, wenn sie
    in einen größeren Rahmen eingebettet sind. Die folgenden beiden
    Impulse sind deshalb nicht an eine konkrete Übung gebunden, sondern
    beschreiben übergreifend, wie das Gelernte nachbereitet und dauerhaft
    im Schulalltag verankert werden kann.
    """
)

st.divider()

# =============================================================================
# 1. REFLEXION NACH DER ÜBUNG
# =============================================================================

st.subheader("1. Reflexion nach der Übung anleiten")

st.markdown(
    """
    Um Schülerinnen und Schülern dabei zu helfen, einen Zusammenhang
    zwischen bestimmten sozial-emotionalen Kompetenzen (SEL) und
    Aktivitäten herzustellen, wird empfohlen, dass pädagogische
    Fachkräfte nach Abschluss einer Aktivität ein Gespräch anhand einiger
    der folgenden Impulse und Fragen moderieren. Die Aktivität sollte sich
    auf eine bestimmte SEL-Kompetenz beziehen, die zuvor ausdrücklich
    vermittelt wurde. Die Fragen und Impulse sind für Gespräche in der
    Gruppe gedacht.
    """
)

st.info(
    "Hinweis: Je nach den unterschiedlichen Lernvoraussetzungen innerhalb "
    "einer Gruppe müssen möglicherweise Anpassungen vorgenommen werden, "
    "damit alle teilnehmen können."
)

st.markdown("**Impulse und Fragen zur Reflexion**")

st.markdown(
    """
    - Nimm dir einen Moment Zeit, halte inne und spüre in dich hinein.
      Achte auf deine Atmung und auf alle Gefühle und Gedanken, die du
      gerade wahrnimmst.
    - Wie hast du dich bei dieser Aktivität gefühlt? Was ist passiert, das
      dazu geführt hat, dass du dich so gefühlt hast?
    - Wem ging es ähnlich? Wer hat sich möglicherweise anders gefühlt?
    - Was hast du während der Aktivität an dir selbst bemerkt?
    - Was hast du während der Aktivität in unserer Gruppe beobachtet, das
      hilfreich war?
    - Welche sozial-emotionalen Kompetenzen (SEL) haben wir bei dieser
      Aktivität eingesetzt?
    - In welchen Situationen während des Schultages könnte es ebenfalls
      nötig sein, diese Kompetenzen einzusetzen?
    - Was hast du während der Aktivität in unserer Gruppe beobachtet, das
      möglicherweise schwierig war?
    - Was könnten wir beim nächsten Mal anders machen, damit es besser
      gelingt?
    """
)

st.markdown(
    "*Wie haben die Schülerinnen und Schüler auf diese Reflexionsübung "
    "reagiert? Zeigen sie dadurch sowohl im Unterricht als auch außerhalb "
    "des Unterrichts ein größeres Bewusstsein für sozial-emotionale "
    "Kompetenzen (SEL) und wenden sie diese häufiger an?*"
)

st.divider()

# =============================================================================
# 2. SEL IM SCHULALLTAG VERANKERN
# =============================================================================

st.subheader("2. Sozial-emotionale Kompetenzen im Schulalltag verankern")

st.markdown(
    """
    Das Vermitteln konkreter sozial-emotionaler Kompetenzen ist nur der
    erste Schritt auf dem Weg zum Ziel, dass Schülerinnen und Schüler
    diese Kompetenzen auch im Alltag anwenden und verinnerlichen. Die
    folgenden Strategien bieten Orientierung und Unterstützung, damit die
    Schülerinnen und Schüler ihre erlernten SEL-Kompetenzen in allen
    Lebensbereichen einsetzen können.
    """
)

st.info(
    "Option: Erstelle einen konkreten Plan mit Zeiten, Terminen und "
    "Unterrichtseinheiten, die du einsetzen möchtest, um die Anwendung "
    "sozial-emotionaler Kompetenzen im Klassenzimmer und in der gesamten "
    "Schule zu fördern."
)

strategy_col1, strategy_col2 = st.columns(2)

with strategy_col1:

    st.markdown(
        """
        <div class="info-card">
        <h4>Beständigkeit</h4>
        Vermittle sozial-emotionale Kompetenzen regelmäßig und
        konsequent. Plane sie fest in deinen Wochenablauf ein und
        reserviere dafür bestimmte Zeiten.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
        <h4>Die Kompetenz vorleben und benennen</h4>
        Nutze Gelegenheiten, um SEL-Kompetenzen vor deinen Schülerinnen
        und Schülern vorzuleben und ausdrücklich zu benennen. Wenn du
        beispielsweise selbst verärgert oder aufgewühlt bist, übe vor den
        Schülerinnen und Schülern bewusst ruhiges Atmen und erkläre, was
        du gerade tust. Du könntest etwa sagen: „Ich bin gerade verärgert
        und muss erst ein paar Mal ruhig durchatmen, bevor wir
        weitermachen.“
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
        <h4>Während der Gruppenarbeit fachliche und soziale Kompetenzen üben</h4>
        Gib den Schülerinnen und Schülern bei Gruppenarbeiten neben einer
        fachlichen Aufgabe auch eine SEL-Kompetenz, die sie gezielt üben
        sollen und die das gemeinsame Arbeiten verbessern kann, zum
        Beispiel Zusammenarbeit, aktives Zuhören oder Problemlösung.
        </div>
        """,
        unsafe_allow_html=True,
    )

with strategy_col2:

    st.markdown(
        """
        <div class="info-card">
        <h4>Die positiven Auswirkungen der Anwendung von SEL-Kompetenzen anerkennen</h4>
        Du könntest beispielsweise sagen: „Mir ist aufgefallen, dass du
        gerade die Kompetenz [Name der SEL-Kompetenz] einsetzt. Dieses
        Verhalten wird dir dabei helfen, …“ Oder: „Ich habe beobachtet,
        dass du … getan hast. Dank deiner Bemühungen werden deine
        Mitschülerinnen und Mitschüler in der Lage sein, …“
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
        <h4>Bei Buchbesprechungen Verbindungen zu SEL-Kompetenzen herstellen</h4>
        Greife Gefühle im Unterricht auf. Wenn du deinen Schülerinnen und
        Schülern beispielsweise das Buch <em>When Sophie Gets Angry,
        Really, Really Angry</em> von Molly Bang vorliest, könntest du
        fragen: „Wie fühlt sich Sophie wohl gerade? Hast du dich auch
        schon einmal so gefühlt?“ Stelle Fragen, die dazu anregen,
        Verbindungen zu SEL-Kompetenzen herzustellen. Beim Lesen von
        <em>Lilly's Purple Plastic Purse</em> von Kevin Henkes könntest
        du beispielsweise fragen: „Wie hat Lilly den Prozess der
        Problemlösung genutzt, um mit der Situation in ihrem
        Klassenzimmer umzugehen, die sie verärgert hat?“
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="info-card">
    <h4>SEL-Unterricht über das Klassenzimmer hinaus auf die gesamte Schulgemeinschaft ausweiten</h4>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    - Stelle SEL-Begriffe und -Kompetenzen in der Cafeteria, im
      Eingangsbereich, im Sekretariat, im Krankenzimmer und auf den
      Fluren sichtbar dar.
    - Beziehe Fachkräfte aus verschiedenen Bereichen und weiteres
      Unterstützungspersonal in Fortbildungen ein. So können sie ihre
      besonderen Beziehungen zu den Schülerinnen und Schülern nutzen, um
      die Kompetenzen zu stärken und Gelegenheiten zu schaffen, diese zu
      üben. Wenn die Kinder beispielsweise in den Schulbus steigen,
      können sie dem Busfahrer oder der Busfahrerin mit einem nach oben
      oder unten gerichteten Daumen zeigen, wie sie sich an diesem Tag
      fühlen. Mitarbeitende der Cafeteria können darauf achten, wenn
      Schülerinnen und Schüler freundlich zueinander sind, und sie dafür
      loben.
    - Nutze gemeinschaftsfördernde Aktivitäten und Spiele während der
      Pausen, zum Beispiel Magic Tag oder Crooked Circle.
    - Stelle SEL-Kompetenzen bei den morgendlichen Durchsagen in den
      Mittelpunkt. Ermutige die Schülerinnen und Schüler beispielsweise,
      im Laufe des Tages Empathie füreinander zu zeigen.
    - Ermutige die Schülerinnen und Schüler, auf dem Schulhof oder in der
      Cafeteria ihre Fähigkeiten zur Problemlösung einzusetzen.
    - Nutze schulweite Zusammenkünfte, Schulversammlungen und
      Familientreffen als Gelegenheiten, bei denen die Schülerinnen und
      Schüler teilen können, was sie gelernt haben.
    """
)

st.markdown(
    "*Bemerkst du Verbesserungen im Klassen- und/oder Schulklima, seit "
    "die Schülerinnen und Schüler ihre sozial-emotionalen Kompetenzen "
    "(SEL) häufiger anwenden?*"
)
