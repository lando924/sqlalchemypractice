from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connects the database to the Flask app"""
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!
    
class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50),
                   nullable=False,
                   unique=True)
    
    species = db.Column(db.String(30), nullable=True)

    hunger = db.Column(db.Integer, nullable=False, default=20)

