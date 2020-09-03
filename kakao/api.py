import sys
import argparse
import requests

from os import path

CONFIG_DIR = path.abspath(path.join(path.dirname(__file__),"../etc"))
API_URL = 'https://dapi.kakao.com/v2/translation/translate'
with open(path.join(CONFIG_DIR, 'kakao_key.txt')) as f:
    KAKAO_KEY = f.read().strip()

def kr_to_en(korean):
    headers = {
        'Authorization': 'KakaoAK {}'.format(KAKAO_KEY),
        'Content-type': 'application/x-www-form-urlencoded'
        }

    try:
        data = {
            'src_lang' : 'kr',
            'target_lang' : 'en',
            'query' : korean
            }
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()['translated_text'][0][0]
    except Exception as e:
        print(str(e))
        sys.exit(0)


if __name__ == "__main__":
    print(kr_to_en("안녕하세요"))

