assert False, "Not successful yet"
import requests
import yaml
from pprint import pprint

cfg = yaml.safe_load(open("C:\\Users\\James\\Desktop\\code\\Learning-Notes--Tech\\RAG\\dify_api\\api_keys.yaml"))['doc_reading']

api_key = cfg["api_key"]

file_path = "C:\\Users\\James\\Desktop\\code\\Learning-Notes--Tech\\RAG\\dify_api\\jd.pdf"


if 1:
    # Step 1: Upload local file
    file_response = requests.post(
        "https://api.dify.ai/v1/files/upload",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"file": ("jd.pdf", open(file_path, "rb"), "application/pdf")},
        data={"user": "abc-123"}
    )
    print(file_response.json())
    file_id = file_response.json()["id"]


# Step 2: Send chat query using uploaded file ID
response = requests.post(
    "https://api.dify.ai/v1/chat-messages",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "inputs": {},
        "query": "Where is the location?",
        "conversation_id": "",
        "user": "abc-123",
        "files": [{"type": "document", "transfer_method": "local_file", "upload_file_id": file_id}]
    }
)
print(response.status_code)
pprint(response.json())
