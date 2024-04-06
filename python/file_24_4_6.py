import keyword
import random
luck_number=8
my_name='cqkaier'
print('幸运树枝是:',luck_number)
print('我的名字是:',my_name)
print('luck_number的类型是',type(luck_number))
print('my_name的类型是',type(my_name))
no=number=9
print(id(no))
print(id(number))
print(ord('康'))
print(ord('友'))
print(ord('林'))
print(chr(24247))
print(3**3)
print(3*3*3)
#求100-999之间的水仙花数
for i in range(100,1000):
    sd=i%10
    ten=i//10%10
    hundred=i//100
    if sd**3+ten**3+hundred**3==i:
        print('100-999之间的水仙花数为:',i)
lst=["hello","world","python","sql"]
print(lst[2],"内存地址:",id(lst))
#增加元素
lst.append("docker")
print("增加元素之后:",lst,"内存地址:",id(lst))

lst2=[4,56,3,78,40,56,89]
print('原列表:',lst2)
lst2.sort()
print('升序:',lst2)
lst2.sort(reverse=True)
print('降序:',lst2)
print(keyword.kwlist)
lst3=[itme for itme in range(1,11)]
print(lst3)
lst3=[itme*itme for itme in range(1,11)]
print(lst3)
lst3=[random.randint(1,100) for _ in range(10)]
print(lst3)
lst4=[i for i in range(10) if i%2==0]
print(lst4)
#二维列表的遍历与列表生成
lst5=[
    ["城市","环比","同比"],
    ["北京",102,103],
    ["上海",104,504],
    ["深圳",100,39]
]
print(lst5)
#二维列表遍历使用双层for循环
for row in lst5:#行
    for rew2 in row:#列
        print(rew2,end="\t")
    print()
#列表生成式
lst6=[[j for j in range(5)]for i in range(4)]
print(lst6)
for row1 in lst6:
    for sow1 in row1:
        print(sow1,end="\t")
    print()
#元组
