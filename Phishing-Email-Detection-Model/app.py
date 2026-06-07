from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

MODEL_ACCURACY = "100%"
CONFUSION_MATRIX = "[[1,0],[0,1]]"


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        email_text = request.form["email"]

        transformed = vectorizer.transform([email_text])

        prediction = model.predict(transformed)[0]

        urls = re.findall(r'https?://\S+', email_text)

        suspicious_keywords = [
            "urgent",
            "verify",
            "password",
            "bank",
            "winner",
            "click",
            "account",
            "login",
            "suspended",
            "free"
        ]

        found_keywords = []

        for keyword in suspicious_keywords:
            if keyword.lower() in email_text.lower():
                found_keywords.append(keyword)

        score = len(urls) + len(found_keywords)

        if score >= 5:
            risk = "HIGH"
        elif score >= 2:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        result = {
            "prediction": prediction.upper(),
            "risk": risk,
            "urls": len(urls),
            "keywords": found_keywords
        }

    return render_template(
        "index.html",
        result=result,
        accuracy=MODEL_ACCURACY,
        confusion_matrix=CONFUSION_MATRIX
    )


if __name__ == "__main__":
    app.run(debug=True)