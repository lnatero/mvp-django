import requests
from requests.structures import CaseInsensitiveDict

url = "http://localhost:8000/save_stock"


data ={"product": 4, "quantity": 69, "type": "1"}


resp = requests.post(url, data=data) 
# resp = requests.post(url, headers=headers, data=data) 

print(resp.json())

