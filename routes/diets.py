from flask import Flask, Response, request, Blueprint
import pymongo
import json
from bson.objectid import ObjectId

diets = Blueprint('diets', __name__, )

try:
    mongo = pymongo.MongoClient(
        "mongodb+srv://hasnain:hasnaindb@cluster0.64pmtc9.mongodb.net/?retryWrites=true&w=majority")
    db = mongo.Fitnessfactor
    mongo.server_info()  # trigger exception when connection with db fails
except Exception as e:
    print("Error - Cannot connect to database", e)


@diets.route("/adddiets", methods=["POST"])
def add_diet():
    try:
        diet = {
            "type": request.form["type"],
            "calories": request.form["calories"],
            "dietName": request.form["dietName"],
            "foodName": request.form["foodName"],
            "foodName2": request.form["foodName2"],
            "foodName3": request.form["foodName3"],
        }
        db_response = db.diets.insert_one(diet)
        print(db_response.inserted_id)

        return Response(
            response=json.dumps({"message": "Diet plan added",
                                 "id": f"{db_response.inserted_id}"
                                 }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "diet cannot be viewed"}), status=500, mimetype="application/json"
        )


@diets.route("/getdiets", methods=["GET"])
def get_diet():
    try:
        data = list(db.diets.find({"type": "breakfast"}))
        arr = []
        for diet in data:
            diet["_id"] = str(diet["_id"])
        arr.append(data)

        data = list(db.diets.find({"type": "lunch"}))
        for diet in data:
            diet["_id"] = str(diet["_id"])
        arr.append(data)

        data = list(db.diets.find({"type": "dinner"}))
        for diet in data:
            diet["_id"] = str(diet["_id"])
        arr.append(data)

        data = list(db.diets.find({"type": "snacks"}))
        for diet in data:
            diet["_id"] = str(diet["_id"])
        arr.append(data)
        print(arr)
        return Response(
            response=json.dumps(arr),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        return Response(
            response=json.dumps({"message": "diet cannot be viewed"}), status=500, mimetype="application/json"
        )


@diets.route("/deletediets/<id>", methods=["DELETE"])
def delete_diet(id):
    try:
        db_response = db.diets.delete_one({"_id": ObjectId(id)})
        if db_response.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "diet deleted", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message": "diet not found", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "diet cant be deleted"}), status=500, mimetype="application/json"
        )
