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
        self.token_headers = {
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
        response = requests.post(f"{self.domain}/enterprise.operations.authorization/", headers=self.token_headers, params=self.params)

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

    def get_vehicle_specs(self, brand_code, model_code, model_year):
        token = self.get_token()

        # Define the endpoint and parameters
        endpoint = f"{self.domain}{self.base_url}vehicle/specs"

        headers = {
            "Authorization": f"Bearer {token}",
            "X-Authorization": os.getenv('X_Authorization'),
            "Ocp-Apim-Subscription-Key": os.getenv('Ocp_Apim_Subscription_Key'),
            "apiVersion": os.getenv('API_VERSION')
        }
        
        params = {
            "BrandCode": brand_code,
            "ModelCode": model_code,
            "ModelYear": model_year
        }

        print()
        # Make the GET request
        response = requests.get(endpoint, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            response_data = response.json().get("CarSpecs", [])
            return response_data
        else:
            raise Exception(f"Failed to get vehicle specs: {response.status_code}, {response.text}")
        
    def get_package(self, package_type, voluntary_code, vehicle_key, province):
            token = self.get_token()

            # Define the endpoint and parameters
            endpoint = f"{self.domain}{self.base_url}/package/search"

            headers = {
                "Authorization": f"Bearer {token}",
                "X-Authorization": os.getenv('X_Authorization'),
                "Ocp-Apim-Subscription-Key": os.getenv('Ocp_Apim_Subscription_Key'),
                "apiVersion": os.getenv('API_VERSION')
            }
            
            params = {
                "PackageType": package_type,
                "VoluntaryCode": voluntary_code,
                "VehicleKey": vehicle_key,
                "LicenseProvinceName":province
            }

            print()
            # Make the GET request
            response = requests.get(endpoint, headers=headers, params=params)

            # Check if the request was successful
            if response.status_code == 200:
                response_data = response.json().get("Packages", [])
                return response_data
            else:
                raise Exception(f"Failed to get package: {response.status_code}, {response.text}")