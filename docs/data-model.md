# Datenmodell

## Überblick

Sämtliche relevante Informationen der Anwendung werden mit Verwendung einer SQLite-Datenbank gespeichtert. 

## Table of contents
-   [Tabellenbeschreibung](#tabellenbeschreibung)
-   [Beziehungen](#beziehungen)
-   [Schematische Darstellung](#schematische-darstellung)
-   [Datenbankanbindung](#datenbankanbindung)
-   [Datenfluss](#datenfluss)

## Tabellenbeschreibung

### users
In der Tabelle `users`werden alle registrierten Nutzer gespeichtert. 

**Felder:**
-   `id`: Primärschlüssel
-   `username`: eindeutiger Nutzername
-   `password`: individuelles Passwort

***Besonderheit:***
-    Der Nutzername `username`ist eindeutig (`UNIQUE`)

### rounds
In der Tabelle `rounds`werden die Tippspiele gespeichert.

**Felder**
-   `id`: Primärschlüssel
-   `name`: Name des Tippspiels
-   `description`: Beschreibung der Runde
-   `creator_user_id`: ID des Erstellers der Runde

***Besonderheiten***
-    Der Name des Tippspiels ist eindeutig (`UNIQUE`)
-   `creator_user_id`legt fest, wer Spiele und Ergebnisse verwalten kann- dieser handelt dementsprechend als Admin des spezifischen Tippspiels

### round_members
In der Tabelle `round_members` werden Nutzer mit den einzelnen Tippspielen verbunden. Hier werden somit die Mitglieder einer Runde abgebildet.

**Felder**
-   `id`: Primärschlüssel
-   `user_id`: Verweis auf Nutzer
-   `round_id`: Verweis auf Tippspiel

***Besonderheit***
-    `user_id`und `round_id`ist eindeutig (`UNIQUE`), damit ein Nutzer nur einmal in einer Runde vertreten sein kann.

### matches
In der Tabelle `matches` werden die Spiele einer Tipprunde gespeichert. Hier werden Spiele mit einzelnen Tippspielen verknüpft. Tatsächliche Ergebnisse werden später für die Rangliste genutzt.

**Felder**
-   `id`: Primärschlüssel
-   `round_id`: Verweis auf Tippspiel
-   `match_date`: Datum des Spiels
-   `home_team`: Heimmannschaft
-   `away_team`: Auswärtsmannschaft
-   `actual_home_score`: Erzielte Tore der Heimmannschaft 
-   `actual_away_score`: Erzielte Tore der Auswärtsmannschaft

### predictions
In der Tabelle `predictions` werden die Tipps der Mitspieler gespeichtert.  Hierbei gehört jeder Tipp zu genau einem Nutzer und einem Spiel in genau einem Tippspiel.

**Felder**
-   `id`: Primärschlüssel
-   `user_id`: Verweis auf Nutzer
-   `match_id`: Verweis auf Spiel
-   `predicted_home_score`: getippte Tore der Heimmannschaft
-   `predicted_away_score`: getippte Torde der Auswärtsmannschaft

***Besonderheit***
-    `user_id``user_id` und `match_id` ist eindeutig (`UNIQUE`), damit pro Nutzer und pro Spiel nur ein Tipp abgegeben werden kann. 

## Beziehungen

Zentrale Beziehungen sind enthalten::
- Ein Nutzer kann an mehreren Tipprunden teilnehmen
- Eine Tipprunde kann mehrere Nutzer enthalten 
→ Beziehung über `round_members`
- Eine Tipprunde kann mehrere Spiele enthalten
→ Beziehung: `rounds → matches`
- Ein Spiel kann mehrere Tipps besitzen
→ Beziehung: `matches → predictions`
- Ein Nutzer kann pro Spiel genau einen Tipp abgeben
→ Beziehung: `users → predictions`

## Schematische Darstellung

```mermaid
erDiagram
    USERS ||--o{ ROUND_MEMBERS : "participates in"
    ROUNDS ||--o{ ROUND_MEMBERS : "contains members"
    ROUNDS ||--o{ MATCHES : "contains"
    MATCHES ||--o{ PREDICTIONS : "has"
    USERS ||--o{ PREDICTIONS : "submits"

    USERS {
        INTEGER id
        TEXT username
        TEXT password
    }

    ROUNDS {
        INTEGER id
        TEXT name
        TEXT description
        INTEGER creator_user_id
    }

    ROUND_MEMBERS {
        INTEGER id
        INTEGER user_id
        INTEGER round_id
    }

    MATCHES {
        INTEGER id
        INTEGER round_id
        TEXT match_date
        TEXT home_team
        TEXT away_team
        INTEGER actual_home_score
        INTEGER actual_away_score
    }

    PREDICTIONS {
        INTEGER id
        INTEGER user_id
        INTEGER match_id
        INTEGER predicted_home_score
        INTEGER predicted_away_score
    }