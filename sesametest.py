import os
import dotenv
import requests
import datetime, base64, json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES

def openSesame():
    dotenv.load_dotenv(override=True) 
    # 各種パラメータ
    api_key = os.environ["SESAME_API"]
    uuid = os.environ["SESAME_UUID"]
    secret_key = os.environ["SESAME_SECRETKEY"]
    base_url = "https://app.candyhouse.co/api/sesame2"

    # ヘッダーの設定
    headers = {'x-api-key': api_key}

    # cmd
    cmd = 83 # 施錠する場合は「82」、解錠する場合は「83」

    # history
    history = 'WEB API' # とりあえず「WEB API」と名付ける
    base64_history = base64.b64encode(bytes(history, 'utf-8')).decode()

    # sign
    cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
    ts = int(datetime.datetime.now().timestamp())
    message = ts.to_bytes(4, byteorder='little')
    message = message.hex()[2:8]
    cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
    cmac.update(bytes.fromhex(message))
    sign = cmac.hexdigest()

    # API
    url = f'{base_url}/{uuid}/cmd'
    body = {
        'cmd': cmd,
        'history': base64_history,
        'sign': sign
    }
    res = str(requests.post(url, json.dumps(body), headers=headers))
    return res


if __name__ == '__main__':
    print(openSesame())
 
