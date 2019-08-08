from flask import Flask, render_template, url_for, session, redirect
from flask_session import Session
from tempfile import mkdtemp
app = Flask(__name__)

app.secret_key = "iorhqoiwrh1ior2r1rni1rno1inr"
app.config["SESSION_FILE_DIR"] =mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("index.html", game=session["board"], turn=session["turn"])



@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"
    session["board"][row][col] = session["turn"]

    return redirect(url_for("index", row=row, col=col))

@app.route("/reset")
def reset():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    return redirect(url_for("index"))


if __name__ == '__main__':

    app.run(debug=True)
