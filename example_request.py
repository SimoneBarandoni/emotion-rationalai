import requests

url = "http://localhost:8000/predict"
data = {"text": "I am very happy today!"}
response = requests.post(url, json=data)
print(response.json())
# Output: {"text": "I am very happy today!", "emotion": "joy"} 