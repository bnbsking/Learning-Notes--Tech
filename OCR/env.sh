#!/bin/bash

poetry run pip install -e . --no-deps

poetry run uvicorn serve:app --reload --host 0.0.0.0 --port 8001

tail -f /dev/null
