# Referenzen

##
In diesem Abschnitt werden zentrale Funktionen der Anwendung beschrieben. 

## Table of contents
- [Core Logic](#core-logic)

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