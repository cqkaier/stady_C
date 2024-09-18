import requests
import re
# import logging

# 设置日志
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 开始读取文件
proxy='127.0.0.1:10809'
try:
    with open('whlg.txt', 'r') as f:
        lines = [line.strip() for line in f]  # 一次性处理所有行
except FileNotFoundError:
    # logging.error("文件未找到")
    exit(1)

for line in lines:
    url = line if line.startswith('http') else 'http://' + line
    try:
        # 发送请求并验证SSL证书
        response = requests.get(url, proxies={'http': proxy}, timeout=5, verify=True)
        if response.status_code == 200:
            # logging.info(f"成功访问: {url}")
            # print(f"成功访问: {url}")
            print(url)
            # with open ('hosts.txt','w') as f:
            #     f.write(url+'\n')
        else:
            # logging.warning(f"访问失败 (状态码 {response.status_code}): {url}")
            # print(f"访问失败 (状态码 {response.status_code}): {url}")
            pass
    except requests.exceptions.RequestException as e:
        # logging.error(f"请求异常: {e} - {url}")
        # print(f"请求异常: {e} - {url}")
        pass
print('done')
