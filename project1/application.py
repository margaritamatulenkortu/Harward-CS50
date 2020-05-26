from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wmlxmdgmmsptfm:f365be54f30aa410404daf76fb9dfb1920a9bb4a189cbea23e46d8448b61f6e3@ec2-54-217-206-236.eu-west-1.compute.amazonaws.com:5432/dbm7r5jpqkrf9a'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "usersb"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    password= db.Column(db.String(120), nullable=True)

    def add_user_name(self, name):
        p = User(name=name, id=self.id)
        db.session.add(p)
        db.session.commit()

    def add_user_password(self, password):
        pw = User(password=password, id=self.id)
        db.session.add(pw)
        db.session.commit()

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('regestre.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    if request.method == 'POST':
        name = request.form['name']
        regname = User(name)
        db.session.add(regname)
        password = request.form['password']
        regpas = User(password)
        db.session.add(regpas)
        db.session.commit()
        return render_template("success.html")