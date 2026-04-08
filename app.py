from flask import Flask, render_template, request, redirect, session
from database import init_db, create_user, get_user_by_username, create_round, get_all_rounds, get_round_by_id, add_user_to_round, get_users_by_round_id, remove_user_from_round, get_rounds_by_user_id, get_round_by_name, create_match, get_matches_by_round_id, delete_match, save_prediction, get_prediction_by_user_and_match, get_predictions_by_round_id, save_match_result
app = Flask(__name__)
app.secret_key = 'your_secret_key'
init_db()

def calculate_points(pred_home, pred_away, actual_home, actual_away):
    if pred_home > pred_away and actual_home > actual_away:
        return 1
    if pred_home < pred_away and actual_home < actual_away:
        return 1
    if pred_home == pred_away and actual_home == actual_away:
        return 1
    return 0

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
    if "user_id" not in session:
        return redirect("/login")
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
    if "user_id" not in session:
        return redirect("/login")
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
    if "user_id" not in session:
        return redirect("/login")
    return render_template("create-round.html")

@app.route("/tippspiel/<int:round_id>")
def tippspiel(round_id):
    if "user_id" not in session:
        return redirect("/login")
    round = get_round_by_id(round_id)
    users = get_users_by_round_id(round_id)
    matches = get_matches_by_round_id(round_id)
    predictions = get_predictions_by_round_id(round_id)

    ranking = {}

    for user in users:
        ranking[user["username"]] = 0
    
    match_result = {}
    for match in matches:
        if match["actual_home_score"] is not None and match["actual_away_score"] is not None:
            match_result[match["id"]] =(
                match["actual_home_score"],
                match["actual_away_score"]
            )
    for prediction in predictions:
        match_id = prediction["match_id"]

        if match_id in match_result:
            actual_home, actual_away = match_result[match_id]

            points = calculate_points(
                prediction["predicted_home_score"],
                prediction["predicted_away_score"],
                actual_home,
                actual_away
            )
            user = next((u for u in users if u["id"] == prediction["user_id"]), None)
            if user:
                ranking[user["username"]] += points
    current_user_id = session ["user_id"]
    is_creator = current_user_id == round["creator_user_id"]

    return render_template("tippspiel.html", 
                           round=round, 
                           users=users, 
                           matches=matches, 
                           predictions=predictions, 
                           ranking=ranking,
                           is_creator=is_creator, 
                           current_user_id=current_user_id, 
                           get_prediction_by_user_and_match=get_prediction_by_user_and_match)

@app.route("/create-round", methods=["GET","POST"])
def create_round_page():
    if "user_id" not in session:
        return redirect("/login")
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
    if "user_id" not in session:
        return redirect("/login")
    match_date = request.form["match_date"]
    home_team = request.form["home_team"]
    away_team = request.form["away_team"]

    create_match(round_id, match_date, home_team, away_team)
    return redirect(f"/tippspiel/{round_id}")

@app.route("/save-result/<int:round_id>/<int:match_id>", methods=["POST"])
def save_match_result_route(round_id, match_id):
    round_data = get_round_by_id(round_id)
    
    if session["user_id"] != round_data["creator_user_id"]:
        return redirect(f"/tippspiel/{round_id}")

    actual_home_score = request.form["actual_home_score"]
    actual_away_score = request.form["actual_away_score"]

    save_match_result(match_id, actual_home_score, actual_away_score)
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)