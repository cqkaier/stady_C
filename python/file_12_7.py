i = 0#初始化变量
while i < 3:
    p = eval(input('请输入密码：'))#获取用户输入
    if p == 1433223:
        print("登陆成功")
        break
    i = i +1
else:
    print("登陆失败")

