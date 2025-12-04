$projectPath = "C:\Users\James\Desktop\code\Learning-Notes--Tech\OCR"

docker run -it --rm `
  -v "${projectPath}:/app" `
  -w /app `
  --name oapp `
  pytorch/pytorch:2.9.0-cuda12.8-cudnn9-runtime `
  /bin/bash
