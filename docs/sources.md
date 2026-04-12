# Quellen

## Table of contents

Übersicht über genutztes Material zur Wissensaneignung und dem Erstellen des Projekts sowie der Dokumentation

## Table of contents
-   [HTML & Templates](#html--templates)
-   [Backend & Flask](#backend--flask)
-   [CSS & Design](#css--design)
-   [Akademische Quellen](#akademische-quellen-bereitsgestellt-im-rahmen-der-modul-lehre)
-   [Nutzung von künstlicher Intelligenz](#nutzung-von-künstlicher-intelligenz)
    -   [Verwendete KI Tools](#verwendete-ki-tools)
    -   [Art und Umfang der Nutzung](#art-und-umfang-der-nutzung)
    -   [Promts zur KI-Nutzung](#prompts-zur-ki-nutzung)
        -   [404-Error](#404)
        -   [Modularisierte Templates](#modularisierte-templates)
        -   [Datenbanken Struktur](#datenbanken-struktur)
        -   [Ausblenden im Template](#ausblenden-im-template)

## HTML & Templates

-   Youtube - HTML Basics: https://www.youtube.com/watch?v=HD13eq_Pmp8&ab_channel=BroCode
-   Flask - Tutorial Templates: https://flask.palletsprojects.com/en/latest/tutorial/templates/
-   Flask - Rendern und Verknüpfen: https://flask.palletsprojects.com/en/stable/templating/
-   Jinja2 - Syntax (Bedingungen, Schleifen etc.):https://jinja.palletsprojects.com/en/stable/templates/
-   Flask - CSS-Einbindung: https://flask.palletsprojects.com/en/stable/tutorial/static/
-   MDN- Grundlagen HTML-Strukturen: https://developer.mozilla.org/en-US/docs/Web/HTML


## Backend & Flask

-   Flask - Grundlegende Struktur: https://flask.palletsprojects.com/en/stable/quickstart/
-   Flask - Funktionen wie `render_template`, `request`, `session` und weitere: https://flask.palletsprojects.com/en/stable/api/
-   Flask - Error-Handler für 404-Fehlerseite: https://flask.palletsprojects.com/en/stable/errorhandling/
-   Flask - Anbindung SQLite-Datenbank: https://flask.palletsprojects.com/en/stable/patterns/sqlite3/
-   Python - Datenbankverbindung, SQL-Abfragen: https://docs.python.org/3/library/sqlite3.html
-   SQLite- SQL-Befehle: https://www.sqlite.org/lang.html
-   Flask - Tutorial Flask, Routing, Templates, Youtube: https://www.youtube.com/watch?v=1r-dFbPQ7Z8 und https://www.youtube.com/watch?v=oQ5UfJqW5Jo
-   Youtube- POST, Forms: https://www.youtube.com/watch?v=nP23R37lMxc

## CSS & Design

-   MDN - CSS Grundlagen: https://developer.mozilla.org/en-US/docs/Web/CSS
-   MDN - CSS Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference


## Akademische Quellen (bereitsgestellt im Rahmen der Modul-Lehre) 

-   https://github.com/hwrberlin/fswd-app
    -   https://hwrberlin.github.io/fswd/fswd-intro.html
    -   https://hwrberlin.github.io/fswd/flask.html
    -   https://hwrberlin.github.io/fswd/html-css.html
    -   https://hwrberlin.github.io/fswd/user-interfaces.html
    -   https://hwrberlin.github.io/fswd/sqlalchemy.html

## Nutzung von Künstlicher Intelligenz

### Verwendete KI-Tools

-   ChatGPT (OpenAI): https://chatgpt.com
-   Claude (Anthropic): https://claude.ai/
-   Grammarly: https://www.grammarly.com

### Art und Umfang der Nutzung

KI-Tools wurden grundlegend in weiten Teilen der Projektarbeit unterstützend genutzt. Herauszuhebende Schwerpunkte, für welche diese genutz wurden waren Vertändnisfragen bezüglich der Logik, Flask, Routen, Requests, Debugging und strukturellen Fragen. Eine finale Prüfung zur möglichen Kürzung und Optimierung wurde vor dem finalen Stand durchgeführt. Darüber hinaus wurde zu Beginn der Projektarbeit ein Roter Faden erarbeiten, welcher dazu diente, einen geordneten Verlauf zum Erstellen des Quellcodes sowie zur späteren Dokumentation zu visualisieren. Entlang dieser Anleitungen wurden logische Schritte durchgeführt. Der Plan wurde jedoch im Laufe des Projekts erweitert, da nötige Änderungen oder Verbesserungen bei der Umsetzung bemerkt wurde. Eine Beispiel ist das Ändern des Löschens eines Spiels aus der Datenbank zu einem Ausblenden (siehe [Design Decisions](design-decisions.html#ausblenden-von-spielen-statt-löschen)) 

Zu keinem Zeitpunkt wurden KI-Tools als Copy & Paste Tool. Ausgenommen ist reine Code-Completion.


### Prompts zur KI-Nutzung:

#### 404
 Error  Wie kann ich eine 404-Error Seite in Flask mit HTMl erstellen und einbinden?

Ausgabe:
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Startseite</h1><p>Diese Seite existiert.</p>"

# Eigene 404-Seite
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
___

<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Seite nicht gefunden</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #222;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
            max-width: 500px;
        }

        h1 {
            font-size: 72px;
            margin: 0 0 10px 0;
            color: #d9534f;
        }

        h2 {
            margin: 0 0 15px 0;
            font-size: 28px;
        }

        p {
            margin-bottom: 25px;
            font-size: 16px;
            color: #555;
        }

        a {
            display: inline-block;
            text-decoration: none;
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            transition: background-color 0.2s ease;
        }

        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <h2>Seite nicht gefunden</h2>
        <p>Die von dir aufgerufene Seite existiert leider nicht.</p>
        <a href="/">Zurück zur Startseite</a>
    </div>
</body>
</html>

___
#### Modularisierte Templates
Wie baue ich ein Grundgerüst zur Modularisierung meiner HTML-Templates?

Ausgabe:

Beispiel des Grundgerüsts, was auf jedem Template einheitlich sein soll:
<!DOCTYPE html>
```<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meine Website{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
```
    <header class="site-header">
        <h1>Mein Projekt</h1>
        <nav class="site-nav">
            <a href="/">Home</a>
            <a href="/dashboard">Dashboard</a>
            <a href="/login">Login</a>
        </nav>
    </header>

    <main class="content">
        {% block content %}{% endblock %}
    </main>

    <footer class="site-footer">
        <p>© 2026 Mein Projekt</p>
    </footer>

</body>
</html>
___

Beispiel eines von base.html erbenen Templates:
{% extends "base.html" %}

{% block title %}Login{% endblock %}

{% block content %}
    <h2>Login</h2>
    <form method="POST">
        <label for="username">Benutzername</label>
        <input type="text" id="username" name="username">

        <label for="password">Passwort</label>
        <input type="password" id="password" name="password">

        <button type="submit">Einloggen</button>
    </form>
{% endblock %}
___

#### Github Dokumentation:
Wie erstelle ich ein Table of contents und verlinke bzw. füge Screenshots sichtbar ein?

Ausgabe:
Ein „Table of Contents“ ist einfach eine Liste mit Links zu deinen Überschriften.

Wenn du in deiner Datei zum Beispiel solche Überschriften hast:

.# Projektdokumentation

.## Inhaltsverzeichnis

- [Einführung](#einführung)
- [Ziel des Projekts](#ziel-des-projekts)
- [Aufbau der Anwendung](#aufbau-der-anwendung)
- [Screenshots](#screenshots)

.## Einführung

Text...

.## Ziel des Projekts

Text...

.## Aufbau der Anwendung

Text...

.## Screenshots

Text...
___
Fotos einfügen:
![Beschreibung](screenshots/Beschreibung.png)
___
#### Datenbanken Struktur
Ich benötige eine Databenbanke Modul Struktur für ein Tippspiel. Dieses beinhalten Login, Registrieren, Runden erstellen, Spiele in die Runden einfügen, Nutzer der Runden, Tipps und eine rangliste für Punkte

Ausgabe:
 Core User System
class User(db.Model):
    """
    Manages registered users of the Tippspiel application

    - Basic login and registration data
    - Stores username and password
    - Can join multiple game rounds
    - Can submit predictions for multiple matches
    """


 Game Round System
class Round(db.Model):
    """
    Represents a tipprunde created inside the application

    - Stores the name of the round
    - Stores which user created the round
    - Contains multiple matches
    - Contains multiple users through memberships
    - Used as the base for the leaderboard
    """


 Round Membership System
class RoundMember(db.Model):
    """
    Connects users and rounds

    - A user can join multiple rounds
    - A round can have multiple users
    - Stores membership information
    - Resolves the many-to-many relationship between User and Round
    """


 Match System
class Match(db.Model):
    """
    Stores matches inside a specific game round

    - Each match belongs to one round
    - Contains home team and away team
    - Stores match date
    - Stores final result
    - Can be used for prediction evaluation
    """


 Prediction System
class Prediction(db.Model):
    """
    Stores a user's prediction for a specific match

    - Each prediction belongs to one user
    - Each prediction belongs to one match
    - Stores predicted home and away goals
    - Stores awarded points after evaluation
    - Used to calculate the ranking inside a round
    """


 Leaderboard Logic
class Leaderboard:
    """
    Represents the ranking logic of a round

    - No separate table is strictly required
    - Ranking can be calculated from prediction points
    - Sums all awarded points of a user in one round
    - Sorts users by total points
    """
___
#### IntegritiyError:
Wie funktioniert sqlite3.IntegrityError zum abfangen von Fehlern einer Datenbank-Regel?

Ausgabe:
except sqlite3.IntegrityError: fängt einen bestimmten Fehler ab, der von SQLite kommt, wenn eine Datenbank-Regel verletzt wird.

Einfach gesagt:
	•	try: = versuche den Code auszuführen
	•	except sqlite3.IntegrityError: = falls genau dieser Datenbankfehler passiert, führe stattdessen diesen Block aus

Beispiel:
try:
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )
    conn.commit()
except sqlite3.IntegrityError:
    print("Benutzername existiert bereits.")
___
#### Ausblenden im Template
Statt etwas über einen Button aus der Datenbank zu löschen, möchte ich, dass der Eintrag lediglich aus dem Template ausgeblendet wird.

Ausgabe:
Du änderst dabei nicht die Datenbank, sonder die Anzeige im Template. Bisher wird dein Button vermutlich mit einer Route aufgebaut sein, welche den Eintrag tatsächlich löscht. 

Statt DELETE FROM ... setzt du den Wert auf 1. Die Abfrage muss so angepasst werden, dass nur Einträge mit is_hidden = 0 erfasst werden. Wichtig: die Route kann weiterhin /delete heißen, sauber wäre aber später /hide.

Das heißt:
	•	neue Spiele sind standardmäßig sichtbar, weil DEFAULT 0
	•	beim „Löschen“ werden sie auf 1 gesetzt
	•	damit hast du ein Soft Delete bzw. logisches Löschen
___
