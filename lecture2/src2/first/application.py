from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Margarita!"

@app.route("/daivid")
def daivid():
    return "Hello, Daivid!"

@app.route("/Maria")
def maria():
    return "Hello, Maria!"