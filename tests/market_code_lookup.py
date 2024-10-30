# to print pretty json
import json
import requests

url = "https://api.upbit.com/v1/market/all?is_details=true"

headers = {"accept": "application/json"}

res = requests.get(url, headers=headers)

data = res.json()

# enlish_name이 Bitcoin이고 market이 KRW로 시작하는 item만 추출 -> 한국 원화로 거래되는 비트코인
bitcoinKRW = [item for item in data if item.get('english_name') == "Bitcoin" and item.get('market').startswith('KRW')]

# enlish_name이 Ripple이고 market이 KRW로 시작하는 item만 추출 -> 한국 원화로 거래되는 리플
rippleKRW = [item for item in data if item.get('english_name') == "Ripple" and item.get('market').startswith('KRW')]

# pretty print
bitcoin_Data = json.dumps(bitcoinKRW, indent=4)
ripple_Data = json.dumps(rippleKRW, indent=4)

print(bitcoin_Data)
print(ripple_Data)