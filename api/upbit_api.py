import os
import uuid
import jwt
import requests
import json
from urllib.parse import urlencode

# 환경 변수 불러오기
access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

# JWT 토큰 생성
def create_jwt_token():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }
    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
    return jwt_token

# UPbit API 호출 함수
def call_upbit_api(endpoint, params=None):
    # 기본 URL에 엔드포인트 추가
    url = server_url + endpoint
    
    # JWT 토큰 생성 및 Authorization 헤더 설정
    jwt_token = create_jwt_token()
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }

    # GET 요청 시 파라미터가 있으면 URL 인코딩하여 추가
    if params:
        url = f"{url}?{urlencode(params)}"
    
    try:
        # API 호출
        print(f"Making request to URL: {url}")  # 요청 URL을 출력하여 확인
        response = requests.get(url, headers=headers)
        
        # 응답 상태 확인
        print(f"Response Status Code: {response.status_code}")  # 상태 코드 확인
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")  # 오류 메시지 출력
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")  # 예외 메시지 출력
        return None

# 예시로 /v1/accounts API 호출
def get_account_info():
    endpoint = '/v1/accounts'
    data = call_upbit_api(endpoint)
    
    # 응답 데이터 출력 (보기 좋게 JSON 형식으로 출력)
    if data:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        print(json_data)
    else:
        print("Failed to retrieve account info")

# 실제 실행 예시
if __name__ == "__main__":
    get_account_info()
