import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretkey")
    NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY", "numverify_api_key")
