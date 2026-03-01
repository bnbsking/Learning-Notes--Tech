import requests


url = "http://ocr:8001/easy_ocr"
files = {"file": open("/app/_data/receipt.pdf", "rb")}
response = requests.post(url, files=files)
print(response.text)
