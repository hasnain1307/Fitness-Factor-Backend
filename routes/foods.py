from flask import Flask, Response, request, Blueprint
import pymongo
import json
from bson.objectid import ObjectId

foods = Blueprint('foods', __name__, )

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


@foods.route("/foods", methods=["POST"])
def add_food():
    try:
        food = {
            "foodname": request.form["foodname"],
            "calories": request.form["calories"]
        }

        db_response = db.foods.insert_one(food)
        print(db_response.inserted_id)
        # for attr in dir(db_response):
        #     print(attr)
        return Response(
            response=json.dumps({"message": "food added",
                                 "id": f"{db_response.inserted_id}"
                                 }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "food cannot be added"}), status=500, mimetype="application/json"
        )


@foods.route("/foods", methods=["GET"])
def get_food():
    try:
        data = list(db.foods.find())
        for food in data:
            food["_id"] = str(food["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "food cannot be viewed"}), status=500, mimetype="application/json"
        )


@foods.route("/foods/<id>", methods=["DELETE"])
def delete_food(id):
    try:
        db_response = db.foods.delete_one({"_id": ObjectId(id)})
        if db_response.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "food deleted", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message": "food not found", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "food cant be deleted"}), status=500, mimetype="application/json"
        )
