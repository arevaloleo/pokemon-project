# authorizer.py
from functools import wraps
from flask import request, jsonify
import requests
import json

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        print("Request Method:", request.method)
        print(request.url)
        path = request.method + request.path
        if not token or not validate_token(token, request):
            return jsonify({
                "code": "access_denied",
                "message": "Unauthorized",
                "severity": "HIGH"
            }), 401
        return f(*args, **kwargs)
    
    return decorated_function

def validate_token(token, request):
    url = 'http://authorizer-central:4200/authorizer'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'token': token,
        'method': request.method,
        'path': request.path,
        'path_params': request.view_args
    }
    response = requests.post(url, headers=headers, json=data)
    if(response.status_code == 200):
        return True
    return False
