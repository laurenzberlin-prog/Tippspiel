# Design-Decisions

## Probleme und Entscheidungen die im Laufe des Projekts auftraten und wie sie gelöst/umgesetzt wurden. 

## Table of contents

-   [Einfache Rechteverteilung über den Creator](#einfache-rechteverteilung-über-den-creator)
-   [Ausblenden von Spielen statt Löschen](#ausblenden-von-spielen-statt-löschen)

---
## Einfache Rechteverteilung über den Creator

### Meta

Status: Decided

Updated: 09-04-2026

### Problem

Es musste definiert werden, welche Nutzer innerhalb einer Tipprunde bestimmte Aktionen durchführen dürfen. Dazu gehören:

-   Spiele erstellen
-   Ergebnisse eintrage
-   Spiele ausblenden

### Entscheidung

Pro Tipprunde wird ein **Ersteller (creator)** gespeichert. Dieser wird über das Feld `creator_user_id`in der Datenbank definiert. 

Nur der Ersteller darf:
-   Spiele hinzufügen
-   Ergebnisse eintrage
-   Spiele ausblenden

Andere Nutzer sind nornale Teilnehmende ohne administrative Rechte. 

### Rationale

Die Entscheidung wurde getroffen, um die Rollelogik bewusst simpel zu halten: 

-   klare und eindeutige Zuständigkeit
-   leichte verständlichkeit bei Nutzenden

### Konsequenzen

**Vorteile:**
-   keine erweiterten Rollen (z. B. mehrere Admins)
-   keine komplexe Rollenverteilung nötig

**Nachteile:**
-   Abhängigkeit vom Administrator zur korrekten Pflege der Tipprunde

---
## Ausblenden von Spielen statt Löschen

### Meta

Status: Decided
Updated: 09-04-2026

### Problem

Beim Löschen eines Spiels durch den Ersteller wurden die Daten für Tipps und Punkte entfernt und aus der Datenbank gelöscht. Dies führte dazu, dass:
-   bereits vergebene Punkte verloren gingen
-   die Rangliste nachträglich verändert wurde
-   Die Nachvollziehbarkeit der Ergebnisse eingeschränkt war

Gleichzeit  war es jedoch für den überblick und die Nutzererfahrung wichtig, dass nicht sämtliche Spiele dauerhaft sichtbar bleiben und die Tipprunde ausfüllen.

### Entscheidung

Spiele werden nicht mehr gelöscht, sonder über ein Feld `is_hidden`ausgeblendet.

Das bedeutet:
-   Spiel bleibt in der Datenbank erhalten
-   Vergebene Punkte fließen weiterhin in die Rangliste ein
-   es wird in der Benutzeroberfläche nicht mehr angezeigt.

### Rationale

Die Lösung ermöglicht eine Trennung zwischen Datenhaltung und der Darstellung, wobei Daten konsistent , Ranglisten erhalten und die Oberfläche übersichtlich bleiben. 

### Konsequenzen

**Vorteile:**
-   stablie und nachvollziehbare Rangliste
-   bessere Übersicht

**Nachteile**
-   zusätzlich Bedinung (`is_hidden`) erforderlich
