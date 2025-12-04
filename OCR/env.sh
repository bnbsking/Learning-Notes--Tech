#!/bin/bash

pip install --no-cache-dir \
    opencv-python-headless \
    pdf2image \
    azure-cognitiveservices-vision-computervision \
    easyocr \
    paddlepaddle \
    paddleocr

apt update && apt install -y libgl1 libglib2.0-0 poppler-utils
