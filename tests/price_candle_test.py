import requests
import json

# KRW-BTC 마켓에 2024년 10월 1일(UTC) 이전 일봉 1개를 요청
url_days = "https://api.upbit.com/v1/candles/days"
params = {  
    'market': 'KRW-XRP',  
    'count': 1,
    # 'to' 비우면 최근 1일
    # 'to': '2024-10-01 00:00:00'
}  
headers = {"accept": "application/json"}

res_days = requests.get(url_days, params=params, headers=headers)
data_days = res_days.json()

printData = json.dumps(data_days, indent=4)

print(printData)