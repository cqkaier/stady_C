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
