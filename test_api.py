import requests

url = 'http://127.0.0.1:5000/predict'
files = {'image': open('../data/synthetic_images/circle/circle_0.png', 'rb')}  # update path if needed

response = requests.post(url, files=files)
print(response.json())
