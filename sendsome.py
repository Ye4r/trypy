# Learning in Python

"""
about send something, by Ye4r
"""

import requests
import time
import random

something = int(input("请输入："))
ci = int(input("请输入次数："))

url1 = "http://www.test1.com"
data1 = {'a':'b'}
data1['c'] = something

url2 = "http://www.test2.com"
data2 = {'a':'b'}
data2['c'] = something

surl1 = {
    url1: data1, url2: data2
}



for i in range(ci):
    url = random.sample(surl1.keys(), 1)[0]
    data = surl1[url]
    print(url)
    send = requests.post(url, data=data)
    print(send.text)
    if "a" in send.text:
        print("POST接口1 success!")
    else:
        print("no!!!")
    time.sleep(1)
