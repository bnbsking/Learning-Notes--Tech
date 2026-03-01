import requests


def test_easy_ocr():
    url = "http://localhost:8001/easy_ocr"
    files = {"file": open("/app/_data/receipt.pdf", "rb")}
    response = requests.post(url, files=files)
    print(response.text)


if __name__ == "__main__":
    test_easy_ocr()
    