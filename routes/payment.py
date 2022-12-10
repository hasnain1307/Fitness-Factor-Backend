import pymongo
import json
from bson.objectid import ObjectId
import stripe

from flask import Flask,Response,request,Blueprint, redirect

from cfg import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

payment = Blueprint('payment', __name__,)

try:
    # mongo = pymongo.MongoClient(
    #    host="localhost", 
    #    port=27017, 
    #    serverSelectionTimeoutMS = 1000
    # )
    mongo = pymongo.MongoClient("mongodb+srv://hasnain:hasnaindb@cluster0.64pmtc9.mongodb.net/?retryWrites=true&w=majority")
    db = mongo.Fitnessfactor
    mongo.server_info() #trigger exception when connection with db fails
except Exception as e:
    print("Error - Cannot connect to database", e)

payment.config['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
payment.config['STRIPE_SECRET_KEY'] = STRIPE_SECRET_KEY
stripe.api_key = payment.config['STRIPE_SECRET_KEY']


@payment.route("/")
def session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='/success.html',
            cancel_url='/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)