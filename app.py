from flask import Flask, render_template, request
from password_logic import check_strength, calculate_entropy, estimate_crack_time, format_time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form["password"]

        score, feedback = check_strength(password)
        entropy = calculate_entropy(password)
        crack_time = format_time(estimate_crack_time(password))

        if score <= 2:
            strength = "Weak"
        elif score == 3:
            strength = "Medium"
        elif score == 4:
            strength = "Strong"
        else:
            strength = "Very Strong"

        result = {
            "score": score,
            "strength": strength,
            "entropy": entropy,
            "crack_time": crack_time,
            "feedback": feedback
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)