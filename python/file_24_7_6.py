a=[]
for _ in range(10):
    a.append(int(input('请输入数字:')))
for j in range(9):
    for i in range(9-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)
# for b in range(10):
#     print(a[b])