import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

# Fetch environment variables
access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

# Create JWT token payload
payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

# Encode the JWT token
jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
authorization = 'Bearer {}'.format(jwt_token)

# Set the headers
headers = {
  'Authorization': authorization,
}

# Make the GET request to the /v1/accounts endpoint
res = requests.get(server_url + '/v1/accounts', headers=headers)

# Print the response in JSON format
print(res.json())