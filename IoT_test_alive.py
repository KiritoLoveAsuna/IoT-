import linecache
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib3
urllib3.disable_warnings()
import requests

proxy = {"https": "127.0.0.1:8080" ,
         "http": "127.0.0.1:8080"}

def scan(url):
    lock.acquire()
    global num
    num += 1
    print("[{}]{}".format(num,url))
    lock.release()

    global ret
    try:
        ret = requests.get(
            url = url,
            verify=False,
            #proxies=proxy,
            allow_redirects=False,
            timeout=20
        )
    except Exception as e:
        return
    if ret.status_code == 200 :
        lock.acquire()
        with open("OK_ip", 'a') as f:
            f.write("{}\n".format(url))
        lock.release()

if __name__ == '__main__':
    num = 0
    lock = threading.Lock()
    text = linecache.getlines("ip.txt")
    pool = ThreadPoolExecutor(max_workers=500)
    for i in text:
        url = i.strip("\n")
        pool.submit(scan, (url))