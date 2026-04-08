# Architektur

## Table of contents

-   [Überblick](#überblick)
-   [Frontend](#frontend)
-   [Backend](#backend)
-   [Datenbankanbindung](#datenbankanbindung)
-   [Datenfluss](#datenfluss)

## Überblick

Im Rahmen der Design-Challenge "Tippspiel" wurde eine serverseitge Webanwendung erstellt. 

Zentrale Ebenen bestehen aus dem Frontend mit HTML und CSS, dem Backend mit Flask und der Datenhaltung mit SQLite.

## Frontend

Das Frontend wurde mit HTML-Templates und CSS umgesetzt. Die HTML-Strukturen nutzen hierbei das von Flask unterstütze Jinja2. 

Die implemtierten templates sind
-   `base.html` --> Dieses liefert das Grundlayout aller Screens
-   `login.html` --> Hier kann sich der Nutzende mit den eigen Daten einloggen
-   `register.html`--> Hier kann sich der Nutzende mit einem Namen und Passwort registrieren
-   `dashboard.html`--> Hier kann der Nutzende zwischen den Hauptfunktionen navigieren
-   `create-round.html`--> hier kann der Nutzende eine neue Tipprunde erstellen
-   `tippspiel.html`--> hier kann der Nutzende die ausgewählte Tipprunde sehen und unter anderem Tipps abgeben
-   `404.html`--> Fehlerseite die auf den Login zurückführt

## Backend

Das Backend basiert auf Flask und findet sich in `app.py`wieder. 

Hier werden Aufgaben zum Routing, Verarbeiten von Formularen, Login-Logik, der Session-Verwaltung, der Rechteprüfung und dem Berechnen der Rangliste bearbeitet. 

Die Logik ist dementsprechend von der visuellen Darstellung getrennt. 

## Datenbankanbindung

In der SQLite-Datenbank hinterlegte Daten werden über die Datei `database.py`genutzt. 

Aufgaben die hier verarbeitet werden sind das Anlegen und Abrufen von Nutzenden, das Erstellen und Verwalten von Tipperunden, das Speichern von Spielen, Tipps und Ergebnissen sowie das Abrufen von Daten für die Rangliste und Anzeige.

## Datenfluss

Der typische Ablauf der Anwendung ist:

1.  Ein Formular wird im Browser abgesendet
2.  Flash verarbeitet die Anfrage
3.  Erforderliche Daten werden aus der Datenbank gelesen oder dort gespeichert
4.  Die Ergebnisse werden an ein Template übergeben und
5.  Die HTML-Seite wird gerendert und an den Browser zurückgesendet