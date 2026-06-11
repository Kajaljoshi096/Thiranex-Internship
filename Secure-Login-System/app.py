from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import bcrypt
import re
import random

app = Flask(__name__)
app.secret_key = "secure_login_project_secret"

USERS_FILE = "users.json"


def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


def suspicious_input(text):

    patterns = [
        "'",
        '"',
        "--",
        ";",
        "DROP",
        "SELECT",
        "INSERT",
        "DELETE",
        "UPDATE"
    ]

    for p in patterns:
        if p.lower() in text.lower():
            return True

    return False


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if suspicious_input(username):
            flash("Invalid username.")
            return redirect(url_for("register"))

        if password != confirm:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        if not validate_password(password):
            flash(
                "Password must contain uppercase, lowercase, number and special character."
            )
            return redirect(url_for("register"))

        users = load_users()

        for user in users:
            if user["username"] == username:
                flash("Username already exists.")
                return redirect(url_for("register"))

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        users.append({
            "username": username,
            "email": email,
            "password": hashed_password
        })

        save_users(users)

        flash("Registration successful.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        users = load_users()

        for user in users:

            if user["username"] == username:

                if bcrypt.checkpw(
                    password.encode("utf-8"),
                    user["password"].encode("utf-8")
                ):

                    otp = str(random.randint(100000, 999999))

                    session["pending_user"] = username
                    session["otp"] = otp

                    return render_template(
                        "login.html",
                        otp=otp,
                        verify=True
                    )

        flash("Invalid username or password.")

    return render_template("login.html")


@app.route("/verify", methods=["POST"])
def verify():

    entered_otp = request.form["otp"]

    if entered_otp == session.get("otp"):

        session["user"] = session["pending_user"]

        session.pop("otp", None)
        session.pop("pending_user", None)

        return redirect(url_for("dashboard"))

    flash("Invalid OTP.")
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)