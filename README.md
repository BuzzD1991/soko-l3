# SOKO-L³ – Website zur Lehrkräftefortbildung

## Struktur

```
app.py                      Einstiegspunkt: Seitenkonfiguration + Navigation
common.py                   Gemeinsame Daten-/Filter-/CSS-Logik & Modulinhalte
views/
  start.py                  Startseite: Programmüberblick
  module.py                 Module im Überblick (6 Module, 2 Kompetenzbereiche)
  ansatz.py                 Ansatz, Zielgruppe, theoretische Fundierung, Grenzen
  uebungssammlung.py        Übungsdatenbank (Übung entdecken / Übungen suchen)
  ressourcen.py             Externe Ressourcen (Tabelle1 der Excel-Datei)
Übungssammlung_GGIE.xlsx    Datenquelle (muss neben app.py liegen)
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

## Inhalte anpassen

- **Module 1–5** (Kurztexte, Status): `MODULES` in `common.py`. Sobald die
  ausführlichen Sitzungspläne vorliegen, hier die `kurz`-Texte ersetzen und
  `status` auf `"vollständig ausgearbeitet"` setzen.
- **Ansatz/Theorie-Platzhalter**: In `views/ansatz.py` ist der Absatz zur
  "Triple Dividend"/Effektstärken-Formulierung als Platzhalter markiert –
  bitte durch den bereits vorliegenden Fortbildungstext ersetzen.
- **Übungen**: weiterhin über `Übungssammlung_GGIE.xlsx` (Tabelle1 =
  Ressourcen, Tabelle2 = Übungen), keine Codeänderung nötig.
- **Neue Seite hinzufügen**: Datei unter `views/` anlegen und in der
  `pages`-Struktur in `app.py` ergänzen.

## Hinweis zur Seitenleiste

Die Seitenleiste zeigt ausschließlich die Navigation zwischen den
Website-Bereichen (Programm / Praxis). Die Übungs-Filter bleiben bewusst im
Hauptbereich der Übungssammlung-Seite, damit Filterung und Ergebnis direkt
zusammen sichtbar sind.
