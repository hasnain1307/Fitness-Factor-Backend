from flask import Flask, Response, request, Blueprint
from flask_cors import CORS
import pymongo
import json
from bson.objectid import ObjectId

workouts = Blueprint('workouts', __name__, )
# workouts = app
# CORS(workouts)

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


@workouts.route("/addworkouts", methods=["POST"])
def add_workout():
    try:
        print(request.data)
        workout = {
            "workoutName": request.form["workoutName"],
            "exerciseName": request.form["exerciseName"],
            "exerciseName2": request.form["exerciseName2"],
            "exerciseName3": request.form["exerciseName3"]
        }
        db_response = db.workouts.insert_one(workout)
        print(db_response.inserted_id)
        # for attr in dir(db_response):
        #     print(attr)
        return Response(
            response=json.dumps({"message": "Workout added",
                                 "id": f"{db_response.inserted_id}"
                                 }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "workout cannot be viewed"}), status=500, mimetype="application/json"
        )


@workouts.route("/getworkouts", methods=["GET"])
def get_workout():
    try:

        arr = ["chest","legs","back","shoulder","tricep","bicep"]
        arr2 = []
        for i in range (len(arr)):
            data = list(db.workouts.find({"workoutName": arr[i]}))
            for workout in data:
                workout["_id"] = str(workout["_id"])
            arr2.append(data)

        # data = list(db.workouts.find({"workoutName": "chest"}))
        # # arr = []
        # for workout in data:
        #     workout["_id"] = str(workout["_id"])
        # arr.append(data)

        # data = list(db.workouts.find({"workoutName": "legs"}))
        # for workout in data:
        #     workout["_id"] = str(workout["_id"])
        # arr.append(data)

        # data = list(db.workouts.find({"workoutName": "back"}))
        # for workout in data:
        #     workout["_id"] = str(workout["_id"])
        # arr.append(data)

        # data = list(db.workouts.find({"workoutName": "shoulder"}))
        # for workout in data:
        #     workout["_id"] = str(workout["_id"])
        # arr.append(data)

        # data = list(db.workouts.find({"workoutName": "tricep"}))
        # for workout in data:
        #     workout["_id"] = str(workout["_id"])
        # arr.append(data)

        # data = list(db.workouts.find({"workoutName": "biceps"}))
        # for workout in data:
        #     workout["_id"] = str(workout["_id"])
        # arr.append(data)
        print(arr)

        return Response(
            response=json.dumps(arr2),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        return Response(
            response=json.dumps({"message": "workout cannot be viewed"}), status=500, mimetype="application/json"
        )


@workouts.route("/deleteworkouts/<id>", methods=["DELETE"])
def delete_workout(id):
    try:
        db_response = db.workouts.delete_one({"_id": ObjectId(id)})
        if db_response.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "workout deleted", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message": "workout not found", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        return Response(
            response=json.dumps({"message": "workout cant be deleted"}), status=500, mimetype="application/json"
        )
