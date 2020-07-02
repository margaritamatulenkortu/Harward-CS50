from flask import Flask
import psycopg2  # for database connectivity
from flask import render_template  # to render the error page

print("dd")
app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
        """To home page"""
        return render_template('first.html')

@app.route("/")
def search():
    print("dd1")
    host = "ec2-54-217-206-236.eu-west-1.compute.amazonaws.com"  # either "localhost", a domain name, or an IP address.
    port = "5432"  # default postgres port
    dbname = "dbm7r5jpqkrf9a"
    user = "wmlxmdgmmsptfm"
    pw = "f365be54f30aa410404daf76fb9dfb1920a9bb4a189cbea23e46d8448b61f6e3"
    dbconn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
    dbcursor = dbconn.cursor()
    """To search default """
    tinput = "0380795272"
    s = ""
    s += "SELECT id, isbn, title, author, year FROM books "
    s += "WHERE "
    s += "("
    s += "isbn LIKE (%t_input)"
    s += ")"
    try:
        print("dd2")
        dbcursor.execute(s, [tinput])
        dbRow = cur.fetchall()
        print(dbRow)
        # Next (not shown here): Show the data in dbRow to your user(s)
    except psycopg2.Error as e:
        t_message = "Postgres Database error: " + e + "/n SQL: " + s
        print("stulba spele")
        return render_template("error.html",)
    dbcursor.closemessage


def main():
    search()

    # Call main application


