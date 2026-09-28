<div align="center">

<img src="../assets/icon.png" alt="Business Idea Stress Test Logo" width="110">

# Business Idea Stress Test

**Prüfe deine Geschäftsidee kritisch, bevor du viel Zeit und Geld investierst**

Ein quelloffener Agent Skill für eine **einmalige, evidenzbasierte Prüfung** neuer Geschäfts- und Gründungsideen

[English](../README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Português (Brasil)](README.pt-BR.md) · [日本語](README.ja.md)

[Installation](../docs/installation.md) · [Schnellstart](../docs/quickstart.md) · [Aktuelle Version](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest)
</div>

> **Sprache:** Diese Einführung liegt auf Deutsch vor. Die eigentlichen Anweisungen in `SKILL.md` sind auf Englisch verfasst, der Skill soll jedoch in der Sprache der nutzenden Person antworten. Die vollständige technische Installationsanleitung ist derzeit auf Englisch verfügbar

## Was bringt dieser Skill?

Eine Geschäftsidee kann überzeugend klingen, obwohl niemand ihre Zahlungsbereitschaft geprüft hat, die Kunden bereits andere Lösungen verwenden oder wesentliche Kosten fehlen. Der Skill schreibt nicht einfach einen optimistischen Businessplan. Er stellt kritische Fragen, überprüft vorhandene Belege mit den Werkzeugen des jeweiligen KI-Systems und sucht systematisch nach Gegenargumenten

Das Ziel: **herausfinden, was nachgewiesen ist, welche Annahmen offenbleiben und welcher kostengünstige Praxistest zuerst sinnvoll ist**

## Die sechs Phasen

1. **Gründerinterview:** schrittweise Klärung von Problem, zahlender Kundschaft, Region, Budget, Ressourcen und Einschränkungen
2. **Frühe Validierung:** Prüfung der Kernhypothese, bereits genutzter Alternativen und möglicher grundlegender Hindernisse
3. **Marktforschung:** sofern aktuelle Recherchewerkzeuge verfügbar sind, Analyse von Nachfrage, Zielgruppe und direkter wie indirekter Konkurrenz mit überprüfbaren Quellen
4. **Finanz- und Betriebsanalyse:** Kosten, Erlösmodell, Deckungsbeiträge, Liquiditätsbedarf und ausdrücklich hypothetische Szenarien
5. **Kritische Gegenprüfung:** die stärksten Einwände aus Kunden-, Wettbewerbs-, Finanz- und Betriebsperspektive
6. **Bedingte Schlussfolgerung:** offene Beweisfragen und ein kleiner Praxistest mit Budgetgrenze sowie Erfolgs- und Abbruchkriterien

Der Skill ersetzt keine echten Kundeninterviews, Fachberatung oder unabhängig arbeitende KI-Modelle. Unbestätigte Marktzahlen oder Preise dürfen nicht als Fakten ausgegeben werden

## Installation

**ChatGPT:** Lade die [offizielle ZIP-Datei der neuesten Version](https://github.com/alexeybarinov/business-idea-stress-test/releases/latest) herunter. Wenn dein Konto eigene Skills unterstützt, gehe zu **Plugins → Skills → Create → Upload from your computer**. Verwende den ZIP-Anhang der Veröffentlichung, nicht das automatisch erzeugte GitHub-Quellcodearchiv. Die Funktion ist nicht in jedem Tarif oder Arbeitsbereich verfügbar

**Codex:**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a codex
```

**Claude Code:**

```bash
npx skills add alexeybarinov/business-idea-stress-test -g -a claude-code
```

**Gemini CLI:**

```bash
gemini skills install https://github.com/alexeybarinov/business-idea-stress-test.git
```

Informationen zu Cursor, Copilot, OpenCode, Claude.ai, manueller Einrichtung und Updates stehen in der [vollständigen Installationsanleitung](../docs/installation.md). `-g` installiert für alle deine Projekte. Node.js wird nur für die Installationsmethode mit `npx` benötigt, nicht zur Ausführung des Skills

## So startest du

Öffne für jede eigenständige Geschäftsidee einen neuen Chat. Wähle den installierten Skill, soweit der KI-Client dies ermöglicht, und schreibe:

```text
Nutze Business Idea Stress Test. Meine Geschäftsidee lautet: [Beschreibung].
Beginne mit einem Gründerinterview und stelle jeweils nur eine wichtige Frage.
Hinterfrage meine Annahmen und kennzeichne fehlende Nachweise,
statt mir automatisch zuzustimmen
```

„Ich weiß es nicht“ ist eine zulässige Antwort. Du kannst später Wettbewerber-Links, eigene Kundengespräche oder Kostenvoranschläge ergänzen. Lass dir am Ende die entscheidenden Quellen und Rechnungen sowie einen messbaren Versuchsplan zeigen

**Datenschutz:** Übermittle keine Passwörter oder unnötigen personenbezogenen bzw. vertraulichen Daten. Bei erheblichen finanziellen oder rechtlichen Entscheidungen ist möglicherweise professionelle Beratung erforderlich

## Versionen und Danksagung

[Änderungsprotokoll](../CHANGELOG.md) · [Veröffentlichungen](https://github.com/alexeybarinov/business-idea-stress-test/releases). Globale Installationen über `npx` lassen sich mit `npx skills update business-idea-stress-test -g` aktualisieren. Manuell hochgeladene Skills müssen gegebenenfalls erneut hochgeladen werden

Vielen Dank an [Matt Pocock](https://github.com/mattpocock/skills), [BuildGreatProducts](https://github.com/BuildGreatProducts/builder-os), [xcrrr](https://github.com/xcrrr/claude-skills), [Corey Haines](https://github.com/coreyhaines31/marketingskills), [sickn33](https://github.com/sickn33/agentic-awesome-skills) und [jukeyman](https://github.com/jukeyman/jukeyman-skills). Dieses unabhängig entwickelte Projekt ist weder mit ihnen verbunden noch von ihnen offiziell unterstützt. [Vollständige Danksagung](../README.md#-standing-on-the-shoulders-of-the-community)

Lizenz der hier neu erstellten Dateien: [MIT](../LICENSE)
