from flask import Flask, render_template, request, redirect, session
from database import init_db, create_user, get_user_by_username, create_round, get_all_rounds, get_round_by_id, add_user_to_round, get_users_by_round_id, remove_user_from_round, get_rounds_by_user_id, get_round_by_name
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
        create_user(username, password)
        return redirect("/login")
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
    return render_template("tippspiel.html", round=round, users=users)

@app.route("/create-round", methods=["GET","POST"])
def create_round_page():
    if request.method == "POST":
        name = request.form["round_name"]
        description = request.form["description"]
        create_round(name, description)
        rounds = get_all_rounds()
        new_round = rounds[-1]
        add_user_to_round(session["user_id"], new_round["id"])
        return redirect("/dashboard")
    return render_template("create-round.html")

@app.route("/leave-round/<int:round_id>", methods=["POST"])
def leave_round(round_id):
    user_id = session.get("user_id")
    remove_user_from_round(user_id, round_id)
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)