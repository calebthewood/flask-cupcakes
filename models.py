"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = 'https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg'


def connect_db(app):
    """Connect DB to Flask App. """
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Creates Cupcake Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

