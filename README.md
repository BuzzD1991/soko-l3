# SOKO-L³ – Website zur Lehrkräftefortbildung

## Struktur

```
app.py                         Einstiegspunkt: Seitenkonfiguration + Navigation
common.py                      Gemeinsame Daten-/Filter-/CSS-Logik & Modulinhalte
views/
  start.py                     Startseite: Programmüberblick
  module.py                    Module im Überblick (6 Module, 2 Kompetenzbereiche)
  ansatz.py                    Ansatz, Zielgruppe, theoretische Fundierung, Grenzen
  uebungssammlung.py           Übungsdatenbank (Übung entdecken / Übungen suchen)
  hinweise.py                  Zwei allgemeine, übungsübergreifende Hinweise für Lehrkräfte
Website_Übungssammlung.xlsx    Datenquelle (muss neben app.py liegen)
requirements.txt
```

## Lokal starten

```bash
pip install -r requirements.txt
streamlit run app.py
```

Die Excel-Datei muss im selben Verzeichnis wie `app.py` liegen (nicht in
`views/`) – `common.py` löst den Pfad relativ zu sich selbst auf, daher
funktioniert das unabhängig davon, welche Unterseite gerade aktiv ist.
Ändert sich die Datei auf dem Server (gleicher Name, neuer Inhalt), wird
der Streamlit-Cache automatisch anhand ihres Änderungsdatums invalidiert –
ein manuelles "Clear cache" ist nicht nötig.

## Datenstruktur der Übungssammlung

Die Excel-Datei besteht aus zwei Tabellenblättern, die über die Spalte
"Übung" 1:1 zusammengehören (`common.py` führt sie beim Laden zusammen):

- **Übersicht** (Kopfzeile in Zeile 3, Daten ab Zeile 4): Übung,
  Kurzbeschreibung der Übung, Dauer (ca.), Zielgruppe, Grundschule,
  Sekundarstufe I, Sekundarstufe II, Anwendungsfälle, Benötigtes
  Material, Lernziele, Emotionswissen, Emotionsregulation, Soziales
  Wissen, Beziehungsfertigkeiten, Verantwortungsvolle
  Entscheidungsfindung, Internetquelle, Originalquelle.
- **Übungsabläufe** (gleiches Kopfzeilen-Schema): Übung, Vor der Übung,
  Während der Übung, Nach der Übung (ggf. Reflexion).

Die drei Altersstufen-Spalten (Grundschule / Sekundarstufe I /
Sekundarstufe II) sowie die fünf SEL-Komponenten-Spalten
(Emotionswissen / Emotionsregulation / Soziales Wissen /
Beziehungsfertigkeiten / Verantwortungsvolle Entscheidungsfindung) sind
0/1-markiert und steuern sowohl die Tags auf den Übungskarten als auch
die beiden Filter im Hauptbereich der Übungssammlung-Seite (`ALTER_COLS`
bzw. `SEL_COLS` in `common.py`). Neue Übungen lassen sich ohne
Codeänderung ergänzen, solange beide Blätter dieselben Spalten in
derselben Reihenfolge verwenden und die Übungsbezeichnung in beiden
Blättern exakt übereinstimmt.

## Inhalte anpassen

- **Module 1–5** (Kurztexte auf der Startseite und Status auf der
  Modul-Übersicht): `PERSONALE_MODULE`/`SOZIALE_MODULE` in
  `views/start.py` bzw. `MODULES` in `common.py`. Sobald die
  ausführlichen Sitzungspläne vorliegen, hier ersetzen und den Status auf
  `"vollständig ausgearbeitet"` setzen.
- **Ansatz/Theorie-Platzhalter**: In `views/ansatz.py` ist der Absatz zur
  "Triple Dividend"/Effektstärken-Formulierung als Platzhalter markiert –
  bitte durch den bereits vorliegenden Fortbildungstext ersetzen.
- **Übungen**: weiterhin über `Website_Übungssammlung.xlsx`, keine
  Codeänderung nötig (siehe Datenstruktur oben).
- **Allgemeine Hinweise für Lehrkräfte**: Text direkt in
  `views/hinweise.py` (zwei Abschnitte, nicht an die Excel-Datei
  gekoppelt).
- **Neue Seite hinzufügen**: Datei unter `views/` anlegen und in der
  `pages`-Struktur in `app.py` ergänzen.

## Hinweis zur Seitenleiste

Die Seitenleiste zeigt ausschließlich die Navigation zwischen den
Website-Bereichen (Programm / Praxis). Die Übungs-Filter bleiben bewusst im
Hauptbereich der Übungssammlung-Seite, damit Filterung und Ergebnis direkt
zusammen sichtbar sind.

## Änderungen gegenüber der vorherigen Version

- Die Übungssammlung wurde auf die überarbeitete Excel-Struktur
  (`Übersicht` + `Übungsabläufe`, drei statt sechs Altersstufen) sowie
  um die neuen, deutschsprachigen SEL-Komponenten-Spalten umgestellt –
  dafür gibt es jetzt wieder einen "SEL-Komponente"-Filter, zusätzlich
  einen freien "Zielgruppe"-Text sowie "Internetquelle"/"Originalquelle"
  je Übung.
- Die Seite "Ressourcen" wurde entfernt, da die zugrunde liegende
  Tabelle (ehemals `Tabelle1`) in der neuen Datei nicht mehr existiert.
  Die Quellenangaben erscheinen stattdessen direkt bei jeder Übung
  (Abschnitt "Quelle").
- Neue Seite "Hinweise für Lehrkräfte" mit zwei übungsübergreifenden
  Impulsen: Eine Übung nachbesprechen (als vier Reflexionsphasen
  aufbereitet) und SEL-Kompetenzen im Schulalltag verankern (als
  Strategiekarten, gruppiert nach "Im Unterricht" und "In der
  Schulgemeinschaft"). Die Inhalte sind redaktionell aufbereitet statt
  wörtlich aus der Vorlage übernommen.
