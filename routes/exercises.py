from flask import Flask, Response, request, Blueprint
import pymongo
import json
from bson.objectid import ObjectId

exercises = Blueprint('exercises', __name__, )

try:
    # mongo = pymongo.MongoClient(
    #    host="localhost", 
    #    port=27017, 
    #    serverSelectionTimeoutMS = 1000
    # )
    mongo = pymongo.MongoClient(
        "mongodb+srv://hasnain:hasnaindb@cluster0.64pmtc9.mongodb.net/?retryWrites=true&w=majority")
    db = mongo.Fitnessfactor
    mongo.server_info()  # trigger exception when connection with db fails
except Exception as e:
    print("Error - Cannot connect to database", e)


@exercises.route("/exercises", methods=["POST"])
def add_exercise():
    try:
        exercise = {
            "exerciseName": request.form["exerciseName"],
            "reps": request.form["reps"],
            "type": request.form["type"]

        }

        db_response = db.exercises.insert_one(exercise)
        print(db_response.inserted_id)

        return Response(
            response=json.dumps({"message": "Exercise added",
                                 "id": f"{db_response.inserted_id}"
                                 }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "exercise cannot be added"}), status=500, mimetype="application/json"
        )


@exercises.route("/exercises", methods=["GET"])
def get_exercise():
    try:
        data = list(db.exercises.find())
        for exercise in data:
            exercise["_id"] = str(exercise["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
        )

    except Exception as ex:
        return Response(
            response=json.dumps({"message": "exercise cannot be viewed"}), status=500, mimetype="application/json"
        )


@exercises.route("/exercises/<id>", methods=["DELETE"])
def delete_exercise(id):
    try:
        db_response = db.exercises.delete_one({"_id": ObjectId(id)})
        if db_response.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "exercise deleted", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message": "exercise not found", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "exercise cant be deleted"}), status=500, mimetype="application/json"
        )
