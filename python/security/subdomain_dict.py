import requests
url="ys7.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
with open("E:/网安/字典/subdomain_dict/subdomain_dict.txt", "r", encoding="utf-8") as file:
    f=file.readlines()
    for i in f:
        dict=i.strip()
        dict=str(dict)
        # print(i.strip())
        # try:
        url1="http://"+dict+'.'+url
        # print(url1)
        try:
            res = requests.get(url1, headers=headers, timeout=5)
            if res.status_code == 200 and len(res.text)>100:
                print(url1)

        except:
            continue
        # #
        # except:
        #     url2="https://"+dict+'.'+url
        #     print(url2)
        #     res = requests.get(url2, headers=headers, timeout=5)
        #     if res.status_code == 200:
        #         print(url2)

