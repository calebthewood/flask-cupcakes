"""Flask app for Cupcakes"""
from flask import Flask, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://davidjeffers:1234@localhost:5432/cupcakes" # added: davidjeffers:1234@localhost:5432
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.get("/api/cupcakes")
def get_cupcakes():
    """Returns list of all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=serialized_cupcakes)