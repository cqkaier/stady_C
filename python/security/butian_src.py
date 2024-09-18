import requests
import json
import time
url='https://www.butian.net/Reward/pub'
for a in range(1,197):
    # print(a)
    data = [
        ('ajax', '1'),
        ('name', ''),  # 空值
        ('p', a)
    ]
    headers={

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

    }
    res=requests.post(url,headers=headers,data=data)
    #获取响应包
    data1=res.json()
    company_name = data1['data']['list']
    # print(company_name)
    for i in company_name:
        name=i['company_name']
        # print(i)
        print(name)
        # with open('C:\\Users\\Kangyl\\Desktop\\butian.txt','a',encoding='utf-8') as f:
        #     f.write(name+'\n')

print('over')
    # time.sleep(10)
    # print(lst)
    # print(data1)