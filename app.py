"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request
from itsdangerous import Serializer
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

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Returns specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake)

@app.post("/api/cupcakes")
def create_cupcake():
    """Adds cupcake to database"""

    flavor = request.json["flavor"]
    rating = request.json["rating"]
    size = request.json["size"]
    image = request.json["image"] or None

    cupcake = Cupcake(
        flavor=flavor,
        rating=rating,
        size=size,
        image=image)
    db.session.add(cupcake)
    db.session.commit()

    serialized_cupcake = cupcake.serialize()
    return (jsonify(cupcake=serialized_cupcake), 201)
