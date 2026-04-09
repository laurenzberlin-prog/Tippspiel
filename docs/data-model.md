# Datenmodell

## Überblick

Sämtliche relevante Informationen der Anwendung werden mit Verwendung einer SQLite-Datenbank gespeichtert. 

## Table of contents
-   [Tabellenbeschreibung](#tabellenbeschreibung)
-   [Beziehungen](#beziehungen)
-   [Schematische Darstellung](#schematische-darstellung)

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
-   `is_hidden`: Kennzeichnet, ob ein Spiel ausgeblendet ist

***Besonderheit:***
-   Spiele werden nicht komplett gelöscht, sonder über `is_hidden`asgeblendet, damit die Tipprunde aufgeräumt werden kann, ohne die Rangliste zu beeinflussen

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

Die Datenbank basiert auf mehreren miteinander verknüpften Tabellen, die die Struktur des Tippspiels abbilden.

- **users ↔ rounds (m:n Beziehung)**  
  Ein Nutzer kann an mehreren Tipprunden teilnehmen und eine Tipprunde kann mehrere Nutzer enthalten.  
  Diese Beziehung wird über die Zwischentabelle `round_members` realisiert.

- **rounds → matches (1:n Beziehung)**  
  Eine Tipprunde kann mehrere Spiele enthalten, jedes Spiel gehört jedoch genau zu einer Tipprunde.

- **matches → predictions (1:n Beziehung)**  
  Ein Spiel kann mehrere Tipps enthalten, da jeder Nutzer einen Tipp zu einem Spiel abgeben kann.

- **users → predictions (1:n Beziehung)**  
  Ein Nutzer kann mehrere Tipps abgeben, jedoch höchstens einen Tipp pro Spiel (durch `UNIQUE(user_id, match_id)` sichergestellt).

- **users → rounds (1:n Beziehung über creator_user_id)**  
  Ein Nutzer kann mehrere Tipprunden erstellen, jede Tipprunde hat jedoch genau einen Ersteller (Creator).

## Schematische Darstellung

users
- id
- username
- password

round_members
- id
- user_id
- round_id

rounds
- id
- name
- description
- creator_user_id

matches
- id
- round_id
- match_date
- home_team
- away_team
- actual_home_score
- actual_away_score
- is_hidden

predictions
- id
- user_id
- match_id
- predicted_home_score
- predicted_away_score