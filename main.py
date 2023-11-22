from flask import Flask, redirect
import json

routes = json.load(open("routes.json", "r"))

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://manangandhi.tech/")


@app.route("/<name>")
def resume(name):
    if name in routes:
        return redirect(routes[name])
    return redirect("https://manangandhi.tech/")


if __name__ == "__main__":
    app.run(host="localhost")
