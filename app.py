from flask import Flask, render_template, request, redirect, session
from random import choice
from cs50 import SQL
from flask_session import Session

db = SQL("sqlite:///urls.db")

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "Sairoxs123"
Session(app)

def randomstr():
    main = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string = ""

    for i in range(5):
        string += choice(main)

    results = db.execute("SELECT * FROM urls WHERE short = (?)", string)

    if results:
        randomstr()

    else:
        return string

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        long = request.form.get("url")
        short = randomstr()

        if long:
            db.execute("INSERT INTO urls (short, long) VALUES (?, ?)", short, long)
            session["short"] = short
            return redirect("/success")

        else:
            return render_template("index.html", empty = True)

    session["short"] = None
    return render_template("index.html")

@app.route("/success")
def success():
    if session.get("short"):
        return render_template("success.html", short = session.get("short"))

    return redirect("/")

@app.route("/<short>")
def main(short):
    results = db.execute("SELECT * FROM urls WHERE short = (?)", short)

    if results:
        return redirect(results[0]["long"])

    else:
        return "<center><h1>This URL has not been registered</h1><a href='/'>Click here to register the URL</a></center>"


if __name__ == "__main__":
    app.run(debug=True)