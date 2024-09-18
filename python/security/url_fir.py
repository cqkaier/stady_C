url='http://mits.whut.edu.cn/'
with open('dir.txt','r') as f:
    for i in f.readlines():
        i=i.strip()
        urls=url+i
        print(urls)
print('done')