from api.upbit_api import *

def main():
    # 예시: UPbit 계좌 정보 출력
    print("Fetching account information...")
    get_account_info()
    my_account = call_upbit_api('/v1/accounts', None)
    print(my_account)

if __name__ == "__main__":
    main()
