from flask import Flask, render_template, request, redirect
from database import init_db, create_user, get_user_by_username

app = Flask(__name__)
app.secret_key = 'your_secret_key'
init_db()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user_by_username(username)

        if user and user["password"] == password:
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


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/create-round")
def create_round():
    return render_template("create-round.html")

@app.route("/tippspiel")
def tippspiel():
    return render_template("tippspiel.html")

if __name__ == "__main__":
    app.run(debug=True)