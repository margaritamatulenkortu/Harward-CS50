import os

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import timedelta
import psycopg2

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)


class Book:
    def __init__(self, id, isbn, title, author, year):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


@app.route("/")
def index():
    if not session.get("logged_in"):
        return render_template("first.html")
    else:
        return render_template("index.html", username=session["user_name"])


@app.route("/registr")
def registr():
    return render_template("registration.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/reg", methods=["POST"])
def reg():
    """Registartion. """
    # if request.method == "GET":
    #     if session.get("logged_in"):
    #         flash("You are already logged in")
    #         return render_template('first.html')
    #     else:
    #         return render_template("register.html")
    name = request.form.get("name")
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    print("name - %s, password - %s", name, password)
    try:
        db.execute("INSERT INTO usersb (name_surname, user_name, password) VALUES ('%s', '%s', '%s')" % (
        name, user_name, password))
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
        return render_template('first.html', user_name=user_name)
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


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

# @app.route('/search', methods=["GET"])
# def search():
#     if request.method == "GET":
#         res = db.execute(
#                 "SELECT * FROM books WHERE LOWER(title) LIKE :title OR LOWER(author) LIKE :author OR year LIKE :year ORDER BY id LIMIT 10 OFFSET :offset",
#                 {"title": text, "author": text, "year": text, "offset": off}).fetchall()
#         for isbn, title, author, year in res:
#                 new_book = Book(isbn, title, author.split(', '), year)
#                 print(new_book)
#
#         return render_template('search.html')
