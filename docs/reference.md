# Referenzen

## In diesem Abschnitt werden zentrale Funktionen der Anwendung beschrieben. 

## Table of contents
- [Core Logic](#core-logic)
  - [calculate_points()](#calculate_points)

- [Authentifizierung](#authentifizierung)
  - [home()](#home)
  - [login()](#login)
  - [register()](#register)
  - [logout()](#logout)

- [Dashboard und Tipprunden](#dashboard-und-tipprunden)
  - [dashboard()](#dashboard)
  - [create_round_page()](#create_round_page)
  - [tippspiel(round_id)](#tippspielround_id)
  - [leave_round(round_id)](#leave_roundround_id)

- [Spiele und Tipps](#spiele-und-tipps)
  - [add_match(round_id)](#add_matchround_id)
  - [save_match_result_route(round_id, match_id)](#save_match_result_routeround_id-match_id)
  - [delete_match_route(match_id, round_id)](#delete_match_routematch_id-round_id)
  - [save_prediction_route(round_id, match_id)](#save_prediction_routeround_id-match_id)

- [Fehlerbehandlung](#fehlerbehandlung)
  - [page_not_found(e)](#page_not_founde)

## Core Logic

### calculate_points()

Route: keine

Methode: keine

Zweck:
calculate_points() berechnet Punkte für abgegebene Tipps indem sie das getippte Ergebnis mit dem tatsächlichen Spielergebnis vergleicht. Dabei wird nur beachtet, ob auf das siegreiche Team oder Unentschieden getippt wurde. Die Höhe des Ergebnisses wird nicht berücksichtigt. 

Ausgabe: 
Gibt `1`zurück, wenn das korrekte Ergebnis getippt wurde, `0`wenn nicht. 

## Authentifizierung

### home()

Route: `/`

Methoden: GET

Zweck:
home() ist der Einstiegspunkt der Anwendung und leitet den Nutzenden auf die Login-Seite. 

Ausgabe:
Weiterleitung auf `login`.

---
### login()

Route: `/login``

Methoden: GET, POST

Zweck:
login() verarbeitet den Login des Nutzenden. Bei einer POST-Request werden Benutzernamen und Passwort geprüft. Bei korrekten Daten wird eine Session für den Nutzer gestartet. 

Ausgabe:
Bei erfolgreichem Login erfolgt die Weiterleitung auf das Dashboard.
Bei fehlgeschlagen Login wird die Login-Seite erneut mit einer Fehlermeldung angezeigt.

---
### register()

Route: `/register`

Methoden: GET, POST

Zweck:
register() ermöglicht das Registrieren für neue Nutzer. Gewählter Benutzername und Passwort werden aus dem Formular übernommen und in der Datenbank gespeichert. Außerdem wird geprüft, ob der gewählte Benutzername bereits vergeben ist.

Ausgabe:
Bei erfolgreichem Registrieren erfolgt die Weiterleitung zur Login-Seite. 
Wenn der Benutzername bereits in Benutzung ist, wird die Registrierungsseite mit einer Fehlermeldung erneut angezeigt. 

---
### logout()

Route: `/logout`

Methoden: GET

Zweck:
Die Funktion meldet den aktuellen Nutzer ab, indem die Session gelöscht wird. 

Ausgabe:
Der Nutzende wird auf die Login-Seite weitergeleitet.

## Dashboard und Tipprunden

### dashboard()

Route: `/dashboard`

Methoden: GET, POST

Zweck:
dashboard() stellt das Dashboard, das Hauptmenü der Anwendung dar. Nacherfolgreicher Prüfung ob der Nutzende eingeloggt ist werden alle Tipprunden geladen, die der Nutzende beigetreten ist. 
Zudem ermöglicht eine POST-Request das Beitreten zu bestehenden Tippspielen über den Namen des Spiels.

Ausgabe:
Anzeige aller Tipprunden des Nutzers
Eine erneute Weiterleitung zum Dashboard erfolgt nach dem Beitreten zu einer neuen Runde.

---
### create_round_page()

Route: `/create-round`

Methoden: GET, POST

Zweck:
create_round_page() ermöglicht das Erstellen neuer Tippspiele, wobei der gewählte Name und Beschreibung gespeichtert werden.
Der aktuelle Nutzer wird automatisch als Ersteller der Runde gesetzt und der neuen Runde hinzugefügt. 

Ausgabe:
Bei erfolgreicher Erstellung wird der Nutzende zum Dashboard weitergeleitet.
Falls der gewählte Name der Tipprunde bereits vergeben ist, wird die Seite mit einer Fehlermeldung erneut angezeigt. 

---
### tippspiel(round_id)

Route: `/tippspiel/<round_id>`

Methoden: GET

Zweck:
tippspiel(round_id) zeigt eine spezifische Tipprunde an, wobei alle dazugehörigen Nutzer, Spiele und bereits abgegebene Tipps geladen werden. 
Außerdem wird die Rangliste aus allen bisher korrekten Tipps berechnet.
Zudem wird geprüft, ob der aktuelle Nutzer der Ersteller der Runde ist, um zusätzliche administrative Funktionen preiszugeben. 

Ausgabe:
Anzeige der Tipprunde inklusive Spiele, Tipps, Rangliste und, sofern Ersteller, die Möglichkeit zum Erstellen und Löschen neuer Spiele.

---
### leave_round(round_id)

Route: `/leave-round/<round_id>``

Methoden: POST

Zweck:
Die Funktion entfernt den aktuellen Nutzer aus einer Tipprunde.

Ausgabe:
Weiterleitung zum Dashboard
