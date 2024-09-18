import random
a=[10,20,30,40,50,60,70,50,90,100]
print(a.index(50,3,8))
print(a.count(50))
print(20 not in a)
print(a[0:5])
print(a[5::2])
print(a[::-1])
for i in a:
    print(i,end=" ")
    print()
# 打乱列表a中的元素顺序
random.shuffle(a)
print(a)

# 对列表a进行升序排序
a.sort()
print(a)

# 对列表a进行降序排序
a.sort(reverse=True)
print(a)
b=sorted(a)
print(id(a))
print(id(b))
c=sorted(a,reverse=True)
print(c)
print(b)
d=sorted(a,key=lambda x:x%2)