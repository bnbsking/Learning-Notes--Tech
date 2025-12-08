import requests
import yaml
from pprint import pprint


cfg = yaml.safe_load(open("api_keys.yaml"))['rag']

dataset_uuid = cfg["dataset_uuid"]
api_key = cfg["api_key"]

url = f"https://api.dify.ai/v1/datasets/{dataset_uuid}/retrieve"

payload = {
    "query": "What is nunox?",
    "retrieval_model": {
        "search_method": "hybrid_search",
        "reranking_enable": False, #True,
        # "reranking_mode": {
        #     "reranking_provider_name": "cohere", # Example
        #     "reranking_model_name": "rerank-english-v2.0" # Example
        # },
        "top_k": 5,
        "score_threshold_enabled": True,
        "score_threshold": 0.5
    }
}

# 4. Put the API Key here in the Authorization header
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
pprint(response.json())