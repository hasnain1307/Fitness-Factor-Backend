from flask import Flask, Response, request, Blueprint
import pymongo
import json
from bson.objectid import ObjectId

members = Blueprint('members', __name__, )

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


@members.route("/viewusers", methods=["GET"])
def get_user():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "user cant be read"}), status=500, mimetype="application/json"
        )


@members.route("/addusers", methods=["POST"])
def create_user():
    try:
        print(request.data)
        user = {
            "name": request.form["name"],
            "lastName": request.form["lastName"],
            "bloodType": request.form["bloodType"],
            "hieght": request.form["hieght"],
            "weight": request.form["weight"],
            "contact": request.form["contact"],
            "username": request.form["username"],
            "password": request.form["password"]
        }

        db_response = db.users.insert_one(user)
        # print(db_response.inserted_id)

        return Response(
            response=json.dumps({"message": "user created",
                                 "id": f"{db_response.inserted_id}"
                                 }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "user cant be created"}), status=500, mimetype="application/json"
        )


@members.route("/deleteusers/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        db_response = db.users.delete_one({"_id": ObjectId(id)})
        if db_response.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "user deleted", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message": "user not found", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        return Response(
            response=json.dumps({"message": "user cant be deleted"}), status=500, mimetype="application/json"
        )
