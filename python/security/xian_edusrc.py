import requests
import json
url="https://my.xijing.edu.cn/cas/login?service=https://yjszh.xijing.edu.cn/index"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
data={
    'username':'220859010',
    'password':'4297f44b13955235245b2497399d7a93',
    'execution':'e14s2',
    'lx':'',
    'loginflag':'_update',
    '_eventId':'submit',
    'geolocation':'',
    'flags':0
}
r=requests.post(url,data=data,headers=headers)
print(r.text)
su_num=220859010