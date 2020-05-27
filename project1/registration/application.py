import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
# print("1")
# try:
#     r = db.execute("INSERT INTO usersb (name, password) VALUES (\'arturito\', \'ehehehe\)")
# except Exception as e:
#     print("Oops!", e.__class__, "occurred.")
#     print("Next entry.")
#     print()
#
# print("2")
# db.commit()
print("3")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registr")
def registr():
    return render_template("registration.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/reg", methods=["POST"])
def reg():
    """Registartion. """
    name = request.form.get("name")
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    print("name - %s, password - %s", name, password)

    try:
        db.execute("INSERT INTO usersb (name_surname, user_name, password) VALUES ('%s', '%s', '%s')" % (name, user_name, password))
        db.commit()
        return render_template('success.html')
    except Exception as e:
        print("Oopsi!", e.__class__, "occurred.")
        return render_template('error.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    """Login"""
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    print("hello")

    sql = "SELECT user_name, password FROM usersb WHERE user_name = '%s' AND password = '%s'" % (user_name, password)
    result = db.execute(sql)
    row = result.first()
    if result.rowcount != 0:
        return render_template('first.html')
    else:
        return render_template('error.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
        """Logout the current user."""
        return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
        """To home page"""
        return render_template('first.html')