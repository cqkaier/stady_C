class preson():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'name is {self.name},age is {self.age}')
class student(preson):
    def __init__(self,name,age,gender):
        super().__init__(name,age) 
        self.gender=gender
stu=student('u0sec',21,'man')
stu.show()
