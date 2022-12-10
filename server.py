from flask import Flask, Response,request
import pymongo
import json
from bson.objectid import ObjectId
from flask_cors import CORS
from flask_sockets import Sockets
from routes.members import members
from routes.foods import foods
from routes.exercises import exercises
from routes.workouts import workouts
from routes.diets import diets
from routes.virtualtrainer import virtualtrainer
# from routes.payment import payment


app = Flask(__name__)
CORS(app)
app.register_blueprint(members,url_prefix="/users")
app.register_blueprint(foods,url_prefix="/foods")
app.register_blueprint(exercises,url_prefix="/exercises")
app.register_blueprint(workouts,url_prefix="/workouts")
app.register_blueprint(diets,url_prefix="/diets")
app.register_blueprint(virtualtrainer,url_prefix="/virtualtrainer")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
