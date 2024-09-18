#打印0000-9999的纯数字
for i in range(10000):
    print(f"{i:04}")
    with open("E:\网安\字典\dict.txt","a") as f:
        f.write(f"{i:04}\n")
        f.close()
print("done")
