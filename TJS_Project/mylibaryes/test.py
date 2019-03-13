import requests
import json


login_url = "http://admin.tjs.com/login.html"
login_post_data = {
    "phone": "18770027573",
    "pssword":"aa111111"
}
session = requests.session()
res = session.post(login_url, login_post_data)
print(session.headers)

with open('session', 'wt') as file:
            file.write(json.dumps(session.cookies.get_dict()))

