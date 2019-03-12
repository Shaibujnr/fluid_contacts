from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello world</h1>"


def create_app():
    return app


__version__ = "0.1.0"
