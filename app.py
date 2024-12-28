from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True



app.config['SECRET_KEY'] = "chickenzarecool1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')

 
if __name__ == "__main__":
    with app.app_context():
        try:
            result = db.create_all()
        except Exception as e:
            print(f"Error querying the databse:{e}")

    app.run