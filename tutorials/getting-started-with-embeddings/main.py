from os import getenv, path
from dotenv import load_dotenv
import requests

BASE_DIR = path.dirname(path.realpath(__file__))
TUTORIALS_DIR = path.dirname(BASE_DIR)
PROJECT_DIR = path.dirname(TUTORIALS_DIR)
ENV_DIR = path.join(PROJECT_DIR, '.env')

# Se opta por un modelo de embeddings pre-entrenado en español
MODEL_ID = "sentence-transformers/distiluse-base-multilingual-cased"
# Asignar las variables de entorno a variables de Python
load_dotenv(ENV_DIR)
HF_TOKEN = getenv('HF_API_KEY')

API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
