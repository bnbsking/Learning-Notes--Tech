## Introduction

A container with EASYOCR API served by FastAPI

+ Does not support paddle OCR and Azure OCR currently

## Quick start
1. Build docker (host)
```bash
docker build -t ocr:v0 .
```

2. Launch service (host)
```bash
docker compose up -d
```

3. Login ocr client (host)
```bash
docker exec -it ocr_client bash
```

4. Test (In client container)
```bash
bash test.sh
```
