import random
#实战一
def get_max(lst):
    x=lst[0]
    for i in range(1,len(lst)):
        if x<lst[i]:
            x=lst[i]
    return x
lst=[random.randint(1,100) for item in range(10)]
print(lst)
max=get_max(lst)
print(max)
print('-'*30)
#实战二
def get_digit(x):
    s=0
    lst=[]
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    s=sum(lst)
    return lst,s
s=input('请输入一个加有数字的字符串:')
lst,x=get_digit(s)
print(f'获取的数字列表为:{lst}')
print(f'累加和为:{x}')
print('-'*30)

#实战三大小写转换
def swap(s):
    lst1=[]
    for item in s:
        if 'A'<=item<='Z':
            lst1.append(chr(ord(item)+32))#ord将字符转成unicode码，加上32转为小写，char转为字符
        elif 'a'<=item<='z':
            lst1.append(chr(ord(item)-32))
        else:
            lst1.append(item)
    return ''.join(lst1)#  ''.join将列表进行拼接
a=input('please enter some string:')
news=swap(a)
print(news)
print('-'*30)
#实战四
