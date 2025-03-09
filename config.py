# config.py

import os

# MongoDB settings
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "content_db")

# Flask settings
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))

# Celery settings (if asynchronous tasks are used)
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# LLM settings
LLM_TYPE = os.getenv("LLM_TYPE", "openai")  # Options: "openai" or "llama"
# For OpenAI (GPT-3.5-turbo)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# For Llama (if using a local model; specify a model name if needed)
LLAMA_MODEL_NAME = os.getenv("LLAMA_MODEL_NAME", "meta-llama/Llama-2-7b-chat-hf")
