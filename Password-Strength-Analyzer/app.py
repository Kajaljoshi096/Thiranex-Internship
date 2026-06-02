from flask import Flask, render_template, request
from password_checker import check_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form["password"]
        score, strength, feedback = check_password(password)

        result = {
            "score": score,
            "strength": strength,
            "feedback": feedback
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
