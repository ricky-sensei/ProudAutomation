import requests
import dotenv
import os
import json



dotenv.load_dotenv(override=True)

api_key = os.environ["SESAME_API"]
uuid = os.environ["SESAME_UUID"]
secret_key = os.environ["SESAME_SECRETKEY"]
url = f'https://app.candyhouse.co/api/sesame2/{uuid}'

headers = {'x-api-key': api_key}

def sesameStatusCheck():
    res = requests.get(url,headers=headers)
    print(res.json()["CHSesame2Status"])


if __name__ == '__main__':
    sesameStatusCheck()
