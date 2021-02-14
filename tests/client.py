import sys
import json
import requests

data = {'id': 1, 'img_path': '/home/adity/Desktop/projects/assignment/data/orange.jpeg'}
res = requests.post("http://127.0.0.1:5000/identify-fruit", data=json.dumps(data))
response = json.loads(res.content)
print(response["fruit_type"])

data = {'id': 2, 'img_path': '/home/adity/Desktop/projects/assignment/data/apple10.jpeg'}
res = requests.post("http://127.0.0.1:5000/identify-fruit", data=json.dumps(data))
response = json.loads(res.content)
print(response["fruit_type"])

data = {'id': 3, 'img_path': '/home/adity/Desktop/projects/assignment/data/Banana-Single.jpg'}
res = requests.post("http://127.0.0.1:5000/identify-fruit", data=json.dumps(data))
response = json.loads(res.content)
print(response["fruit_type"])