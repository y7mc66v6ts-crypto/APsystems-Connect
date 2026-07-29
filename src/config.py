from dotenv import load_dotenv
import os

# Lees de variabelen uit het .env-bestand
load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
SID = os.getenv("SID")

# The APsystems OpenAPI server. This is not a secret.
API_BASE_URL = "https://api.apsystemsema.com:9282"
