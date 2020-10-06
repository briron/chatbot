import requests
import json

def isValidToken(cur):
    url = "https://kapi.kakao.com/v1/user/access_token_info"
    headers = {"Authorization" : "Bearer " + cur}
    resp = requests.get(url, headers=headers)
    return resp.status_code == 200

def getNewToken(refresh_token, client_id):
    url = "https://kapi.kakao.com/oauth/token"
    headers = {"Authorization" : "Bearer " + cur}
    data = {
        'grant_type' : 'refresh_token',
        'client_id' : client_id,
        'refresh_token' : refresh_token
    }
    resp = requests.post(url, data=json.dumps(data))
    dic = json.loads(resp.text)
    dic['client_id'] = client_id
    with open('../etc/kakao_token.txt', 'w') as lf:
        lf.write(json.dumps(dic))
    return dic['access_token']


def getAccessToken():
    saved = ""
    with open('../etc/kakao_token.txt') as lf:
        tokens = json.loads(lf.read())
    cur = tokens['access_token']
    refresh = tokens['refresh_token']
    client_id = tokens['client_id']
    if isValidToken(cur):
        return cur
    else:
        return getNewToken(refresh_token, client_id)


def sendMessageToMe(message):
    ACCESS_TOKEN = getAccessToken()
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization" : "Bearer " + ACCESS_TOKEN
    }
    template = {
        "object_type": "text",
        "text": message,
        "link": {}
    }
    data = {
        "template_object": json.dumps(template)
    }
    resp = requests.post(url, headers=headers, data=data)
    return resp.text

if __name__ == "__main__":
    sendMessageToMe("hello world!")