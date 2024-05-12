class student():
    school='大学'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'这是一个实例属性,name is {self.name},age is {self.age}')
stu=student('u0sec','21')
stu2=student('tanx',30)
print(stu.name,stu.age)
print(stu2.name,stu2.age)
stu.show()
print(student.school)
stu.age=18

print(stu.name,stu.age)
