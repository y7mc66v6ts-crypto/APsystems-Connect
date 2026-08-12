from dotenv import load_dotenv
import os

# Lees de variabelen uit het .env-bestand
load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
SID = os.getenv("SID")

ECU_IP = os.getenv("ECU_IP")
ECU_PORT = int(os.getenv("ECU_PORT", "8899"))

# The APsystems OpenAPI server. This is not a secret.
BASE_URL = "https://api.apsystemsema.com:9282"
