import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from fastapi import FastAPI

app = FastAPI()

# Read the Key Vault URL from an environment variable
KEY_VAULT_URL = os.environ.get("KEY_VAULT_URL", "")
secret_value = None


@app.on_event("startup")
def load_secrets():
    # Load secrets from Key Vault when the app starts
    global secret_value
    if KEY_VAULT_URL:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
        secret_value = client.get_secret("my-api-key").value


@app.get("/")
def health_check():
    return {"status": "healthy", "service": "my-fastapi-app"}


@app.get("/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Mouse", "price": 29.99},
            {"id": 3, "name": "Keyboard", "price": 79.99},
            {"id": 4, "name": "Monitor", "price": 299.99},
        ]
    }


@app.get("/secret-status")
def secret_status():
    # Confirm the secret was loaded without exposing the actual value
    return {
        "secret_loaded": secret_value is not None,
        "key_vault_configured": bool(KEY_VAULT_URL),
    }