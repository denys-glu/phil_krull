from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    print("Index method was triggered")
    return "In index method"

@app.route("/name", defaults={"user_name": "phil", "number": 0})
def say_name(user_name, number):
    print(f"In say_name method, hi {user_name}")
    return render_template("index.html", name_for_template = user_name, num_for_template = number)

app.run(debug=True)

