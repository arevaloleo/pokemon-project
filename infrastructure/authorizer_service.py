import requests
import os

AUTHORIZER_URL = os.getenv("AUTHORIZER_URL")

def verify_token(token):
    try:
        response = requests.post(AUTHORIZER_URL, json={"token": token})
        
        # Si el token es válido
        if response.status_code == 200:
            return response.json()  # Devolver información del token válido
        else:
            return None
    except Exception as e:
        print(f"Error verificando el token: {e}")
        return None
