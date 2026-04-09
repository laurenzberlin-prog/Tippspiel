# Value-Proposition

## Table of contents

-   [Problemstellung](#problemstellung)
-   [Lösung](#lösung)
-   [Zielgruppe](#zielgruppe)
-   [Nutzererlebnis](#nutzererlebnis)
-   [Use-Case-Flow](#use-case-flow)

##  Problemstellung

Der Sport ist in vielen Bereichen und Kreisen ein wichtiger Sammelpunkt für Interessen von Freund:innen und Kolleg:innen. Eine beliebte Art und Weise sein Wissen und Glück auf eine spielerische Art und Weise zu demonstrieren ist das gemeinsame Durchführen von Tippspielen. 

Hier kommt es jedoch oft zu organisatorischen Schwierigkeiten durch fehlende Übersicht, schwierige Auswertung und unklare Ranglisten. 

##  Lösung

Die Anwendung Tippspiel bietet eine simple webbasierte Lösung, um gerade diese Probleme zu beheben und das schnelle und zuverlässige Durchführen von Tippspielen in einem Bekanntenkreis durchführen zu können. 

Umgesetzte Funktionen der Anwendung sind:

-   Registrierung und Login für jeden Nutzenden
-   Erstellen, Durchführen und Verwalten von Tippspielen
-   Beitritt zu bestehenden Tippspielen
-   Tippabgabe zu Ergebnissen
-   Erfassen von Ergebnissen
-   Ranglistenanzeige, verknüpft mit bisherigen Tipps

##  Zielgruppe

Die Zielgruppe sind kleine Gruppen von Arbeitskolleg:innen, die ohne großen organisatorischen Aufwand ein gemeinsames Tippspiel durchführen möchten.

##  Nutzererlebnis

Das Nutzererlebnis beschreibt die typische Nutzung und den Ablauf der Anwndung

### Ablauf

1.  Nutzer öffnet die Anwendung gelangt zur Login-Seite
2.  Hat der Nutzer noch keine Daten, nutzt er den Button "Registrieren" und gelangt zur Registrieren-Seite
3.  Hier kann er einen Namen und ein Passwort festlegen und wird zurück zur Login-Seite geleitet
4.  Nach erfolgreichem Login wird das Dashboard angezeigt
5.  Hier kann der Nutzer:
    -   Eine neue Tipprunde erstellen, nachdem er über den Button "Neues Tippspiel erstellen" auf die entsprechende Seite geleitet wird und hier einen Namen und eine Beschreibung für die Tipprunde eingibt und diese speichtert
    -   Einem bestehendem Tippspiel über das Textfeld unter "Tippspiel beitreten" beitreten
    -   Unter "Meine Tippspiele" sehen, welchen Tippspielen er beigetreten ist und die aufrufen
    -   Sich über den "Abmelden" Button ausloggen. 
6. Wird eine Runde aufgerufen, welcher der Nutzer beigetreten oder diese erstellt hat, kann er hier offene und beendete Spiele einsehen, Tipps dazu abgeben sowie eine Rangliste aller teilnehmer begutachten. Ist der Nutzer der Ersteller der Tipprunde, kann er zudem zukünftige Spiele erstellen, welche im Rahmen der Runde getippt werden können. Zudem kann er die tatsächlichen Ergebnisse eingeben. 

### Schematische Darstellung

Login  
↓  
Dashboard  
↓  
Tipprunde erstellen / beitreten  
↓  
Spiele anzeigen  
↓  
Tipp abgeben  
↓  
Ergebnisse einsehen  
↓  
Rangliste

## Use-Case-Flow

Das Use-Case-Flow Diagram dient dem visualisieren des typischen Nutzererlebnisses

![Use-Case-Flow](screenshot/use_case-flow.png)