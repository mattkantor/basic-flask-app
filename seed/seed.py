import requests
import json
from faker import Faker

faker = Faker()
valid_email = "matthewkantor@gmail.com"
valid_password = "password"
def seed():
    prefix = "http://localhost:5000/api/v1/"
    payload = {"email": valid_email, "password": valid_password}
    register = requests.post(prefix + "register", json=payload)

    get_data = requests.post(url=prefix + "get_auth_token", json=payload)
    valid_token = get_data.json()["token"]

    header = {"Authorization":"Bearer " + valid_token}
    me = requests.get(url=prefix + "me", headers=header)
    print(me.content())

    for i in range(1,5):
        payload = {"email":faker.email(),"password":"password"}
        register = requests.post(prefix + "register", json=payload)
        token = register.json()["token"]


        #now create some groups, make sure you gave a valid non-random email in there


        #get the token


        #each user gets saome groups


seed()
