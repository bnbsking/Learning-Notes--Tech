assert False, "Not successful yet"
import requests
import yaml
from pprint import pprint


cfg = yaml.safe_load(open("api_keys.yaml"))['img']
file_path = "dog.jpg"

api_key = cfg["api_key"]


#upload_url = "https://api.dify.com/files/upload"
upload_url = "https://api.dify.ai/v1/files/upload"
with open(file_path, "rb") as f:
    files = {"file": f}
    data = {"user": "abc-123"}   # ← REQUIRED}
    headers = {"Authorization": f"Bearer {api_key}"}
    upload_response = requests.post(upload_url, headers=headers, data=data, files=files)
    #file_id = upload_response.json()["id"]
    print("Upload response:", upload_response.json())

#breakpoint()
url = "https://api.dify.ai/v1/chat-messages"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "inputs": {},
    "query": "What is in the picture?",
    "conversation_id": "",
    "user": "abc-123",
    "files": [
        {
            "type": "image",
            "transfer_method": "local_file",
            "upload_file_id": file_id
        }
    ]
}

# Normal response (non-streaming)
response = requests.post(url, headers=headers, json=data, stream=False)
print(response.status_code)
pprint(response.json())