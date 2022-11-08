import requests
from requests.structures import CaseInsensitiveDict

url = "https://ptsv2.com/t/j4yzw-1667765764/post"

headers = {
    "X-CSRFToken": "Sm6FxecG5LngXR1qhv0rrXZCUiNIa4cvqw11sQWXSHsmzmjrOEJM84v36haWQ9Ss",
}


data = """
{
"product":4,
"quantity": 15,
"type": 2,
}
"""


resp = requests.post(url, data=data)

print(resp.status_code)