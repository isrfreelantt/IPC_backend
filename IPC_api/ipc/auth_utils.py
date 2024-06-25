import requests
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class TokenManager:
    def __init__(self):
        self.domain = os.getenv('DOMAIN')
        self.base_url = os.getenv('BASE_URL')
        self.identity = os.getenv('IDENTITY')
        self.api_url = f"{self.domain}{self.base_url}?Identity={self.identity}"
        self.headers = {
            "App_ID": os.getenv('APP_ID'),
            "App_Key": os.getenv('APP_KEY'),
            "Resource": os.getenv('RESOURCE'),
            "apiVersion": os.getenv('API_VERSION')
        }
        self.params = {
            "Identity": self.identity
        }
        self.token = None
        self.token_expiry = 0

    def get_bearer_token(self):
        # Make the POST request to get a new token
        response = requests.post(self.api_url, headers=self.headers, params=self.params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            self.token = data.get("access_token")
            expires_on = int(data.get("expires_on"))
            self.token_expiry = expires_on
        else:
            raise Exception(f"Failed to get access token: {response.status_code}, {response.text}")

    def get_token(self):
        # Check if the token is expired or doesn't exist
        current_time = int(time.time())
        if not self.token or current_time >= self.token_expiry:
            self.get_bearer_token()
        return self.token

# Usage
token_manager = TokenManager()

# Whenever you need the token, call this method
try:
    token = token_manager.get_token()
    print(token)
except Exception as e:
    print(f"Error: {e}")
