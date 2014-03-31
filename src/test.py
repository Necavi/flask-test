from . import app

from flask import render_template

@app.route("/")
def test_func():
    return render_template("index.html")


@app.route("/num/<num>")
def disp_run(num):
    return render_template("num.html", number=num)