#写一个从1加到x的函数
def add(x):
    if x == 1:
        return 1
    else:
        return x + add(x-1)
class Test:
    def __init__(self):
        self.a = 1
        print(self.a)
if __name__ == '__main__':
    print(add(100))
    n=Test()