from flask import Flask, render_template, request, redirect, session
from database import init_db, create_user, get_user_by_username, create_round, get_all_rounds, get_round_by_id, add_user_to_round, get_users_by_round_id, remove_user_from_round, get_rounds_by_user_id, get_round_by_name, create_match, get_matches_by_round_id, delete_match, save_prediction, get_prediction_by_user_and_match
app = Flask(__name__)
app.secret_key = 'your_secret_key'
init_db()

@app.route("/")
def home():
    return redirect("login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user_by_username(username)
        if user and user["password"] == password:
            session["user_id"] = user["id"]
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Falscher Nutzername oder falsches Passwort. Bitte überprüfe die Eingabe!")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        
        success = create_user(username, password)
        if success:
            return redirect("/login")
        else:
            return render_template("register.html", error="Der Nutzername ist bereits vergeben. Bitte wähle einen anderen Namen!")
    return render_template("register.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    user_id = session["user_id"]

    if request.method == "POST":
        round_name = request.form["round_name"]
        round_data = get_round_by_name(round_name)

        if round_data:
            add_user_to_round(user_id, round_data["id"])

        return redirect("/dashboard")
    rounds = get_rounds_by_user_id(user_id)
    return render_template("dashboard.html", rounds=rounds)

@app.route("/create-round")
def create_round_form():
    return render_template("create-round.html")

@app.route("/tippspiel/<int:round_id>")
def tippspiel(round_id):
    round = get_round_by_id(round_id)
    users = get_users_by_round_id(round_id)
    matches = get_matches_by_round_id(round_id)

    current_user_id = session ["user_id"]
    is_creator = current_user_id == round["creator_user_id"]

    return render_template("tippspiel.html", round=round, users=users, matches=matches, is_creator=is_creator, current_user_id=current_user_id, get_prediction_by_user_and_match=get_prediction_by_user_and_match)

@app.route("/create-round", methods=["GET","POST"])
def create_round_page():
    if request.method == "POST":
        name = request.form["round_name"]
        description = request.form["description"]

        success = create_round(name, description, session["user_id"])

        if success:
            rounds = get_all_rounds()
            new_round = rounds[-1]
            add_user_to_round(session["user_id"], new_round["id"])
            return redirect("/dashboard")
        else:
            return render_template("create-round.html", error="Eine Tipprunde mit diesem Namen existiert bereits.")

    return render_template("create-round.html")

@app.route("/add-match/<int:round_id>", methods=["POST"])
def add_match(round_id):
    match_date = request.form["match_date"]
    home_team = request.form["home_team"]
    away_team = request.form["away_team"]

    create_match(round_id, match_date, home_team, away_team)
    return redirect(f"/tippspiel/{round_id}")

@app.route("/delete-match/<int:match_id>/<int:round_id>", methods=["POST"])
def delete_match_route(match_id, round_id):
    round_data = get_round_by_id(round_id)
    if session["user_id"] != round_data["creator_user_id"]:
        return redirect(f"/tippspiel/{round_id}")
    delete_match(match_id)
    return redirect(f"/tippspiel/{round_id}")

@app.route("/save-prediction/<int:round_id>/<int:match_id>", methods=["POST"])
def save_prediction_route(round_id, match_id):
    user_id = session["user_id"]

    existing_prediction = get_prediction_by_user_and_match(user_id, match_id)
    if existing_prediction:
        return redirect(f"/tippspiel/{round_id}")

    predicted_home_score = request.form["predicted_home_score"]
    predicted_away_score = request.form["predicted_away_score"]

    save_prediction(user_id, match_id, predicted_home_score, predicted_away_score)
    return redirect(f"/tippspiel/{round_id}")

@app.route("/leave-round/<int:round_id>", methods=["POST"])
def leave_round(round_id):
    user_id = session.get("user_id")
    remove_user_from_round(user_id, round_id)
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)