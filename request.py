import requests
import sys
import json

url = "http://localhost:5000/predict_api"

response = requests.post(url=url, json={"value1":2, "value2":9, "value3":6}, headers={"Host": "sineestimator"})

print(response.json())
