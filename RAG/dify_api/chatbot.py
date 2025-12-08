import requests
import yaml
from pprint import pprint


cfg = yaml.safe_load(open("api_keys.yaml"))['chatbot']

api_key = cfg["api_key"]

url = "https://api.dify.ai/v1/chat-messages"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "inputs": {},
    "query": "What is Apple's smart phone? Iphone or Pixel?",
    #"response_mode": "streaming",
    "conversation_id": "",
    "user": "abc-123",
    # "files": [
    #     {
    #         "type": "image",
    #         "transfer_method": "remote_url",
    #         "url": "https://cloud.dify.ai/logo/logo-site.png"
    #     }
    # ]
}

# Normal response (non-streaming)
response = requests.post(url, headers=headers, json=data, stream=False)
print(response.status_code)
pprint(response.json())
