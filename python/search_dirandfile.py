import os
import os.path
import re
print('当前路径为:',os.getcwd())
lst=os.listdir()
print('当前目录下的文件有:',)
for item in lst:
    print(item,)
# import pickle
# import urllib
# class pyload(object):
#     def __reduce__(self):
#         print('hacker!!!')
#         return (eval,("open('/flag.txt','r').read(),"))
# pl=pickle.dumps(pyload())
# ll=urllib.quote(pl)
# print(ll)
print('获取目录或文件的绝对路径:',os.path.abspath('./len.py'))
print('提取文件名：',os.path.basename('./file_12_4.py'))
name=os.path.splitext('./file_12_4.py')
# print(name[0])
st=str(name)
# print(st[2:6])
# st="hello file name is abc"
pattern = r'file'
match = re.search(pattern, st)
if match:
    with open('a. txt', 'w') as file:
        file.write(match.group())
    print("Match found:", match.group())

else:

    print("No match found.")
# with open('a. txt','w') as file:
#     file.write('name')