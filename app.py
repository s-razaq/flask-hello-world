from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/add")
def hello_world(a, b):
    return a + b
