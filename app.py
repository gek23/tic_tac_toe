"""The following code modifies the url and directs the user to the desired page accordingly."""

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():

    def draw():
        game_state = [[None, None, None], [None, None, None], [None, None, None]]

    return render_template("tic_tac.html", game_state=game_state)



@app.route("/register")
def register():
    return "hello"

@app.route("/00")
def zerozero():
    return render_template("zerozero.html")

