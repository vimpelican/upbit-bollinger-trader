# to print pretty json
import json
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

# Response 객체에서 JSON 데이터를 추출
data = res.json()

# 추출한 데이터를 JSON으로 직렬화 (예: 파일로 저장하거나, 보기 좋게 포맷팅할 때)
#! print(json.dumps(data, indent=4, ensure_ascii=False)) - 오류 발생
json_data = json.dumps(data, indent=4)
print(json_data)