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

  