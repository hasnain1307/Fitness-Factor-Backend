from flask import Flask, Response, request, Blueprint
import pymongo
import json
from fileinput import filename
from bson.objectid import ObjectId

virtualtrainer = Blueprint('virtualtrainer', __name__, )

try:
    mongo = pymongo.MongoClient(
        "mongodb+srv://hasnain:hasnaindb@cluster0.64pmtc9.mongodb.net/?retryWrites=true&w=majority")
    db = mongo.Fitnessfactor
    mongo.server_info()  # trigger exception when connection with db fails
except Exception as e:
    print("Error - Cannot connect to database", e)
#write an api to receive video 
@virtualtrainer.route("/video", methods=["POST"])
def video():
    try:
        # print(request.files["video"].read())
        f = request.files['video']
        f.save(f.filename)
        test = f.filename

        print(f)
        return Response(
            # return video in response from folder output
            
            response=json.dumps({"message": "video added"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "video cannot be added"}), status=500, mimetype="application/json"
        )
