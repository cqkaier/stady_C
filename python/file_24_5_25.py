import time
import random
tl=time.localtime()
print(tl)
print(f'{tl.tm_year}年{tl.tm_mon}月{tl.tm_mday}日')
# random.seed(10)
rd=random.randint(1,100)
print(rd)
#写一个冒泡排序算法
#写一个计算1到10的阶乘的函数
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(10))