#求n!
n=eval(input("请输入要求的数字:"))
i=1
sum=1
while n>=i:
    # 5>i
    sum=sum*i #3 6
    i = i + 1
print(sum)
#求1!+2!+...+10!
num=0
# a=eval(input("请输入要求的数字:"))
num1=0
while num1<10:
    num1=num1+1#获取1-10的数字
    # print(num1)
    i=1
    sum=1
    while num1>=i:
        # 5>i
        sum=sum*i #3 6
        i = i + 1
    # print(sum)
    num=sum+num
print("1!+2!+3!+...+10!:",num)
#查找数字的下标

#猜数字游戏