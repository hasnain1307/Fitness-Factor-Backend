import sys
import json
import requests

# data = {
#     "name" : "Ali",
#     "lastName" : "ahmed",
#     "bloodType": "b+",
#     "hieght" : "5`11",
#     "weight": "200 pounds",
#     "contact" : "0312412132",
#     "username" : "ali",
#     "password" : "1223",
# }
data  ={
    "type" : "breakfast",
    "calories": "1200",
    "dietName" : "low calories ",
    "foodName": "egss",
    "foodName2" : "bread",
    "foodName3" :"juice",
}
# data = json.dumps(data)
res = requests.get("http://127.0.0.1:5000/diets/getdiets")
print(res.text)
