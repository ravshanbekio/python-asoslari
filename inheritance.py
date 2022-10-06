class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getname(self):
        print(self.first_name, self.last_name)
        

class Student(Person):

    def __init__(self, first_name, last_name, grade):
        super().__init__(first_name, last_name)
        self.grade = grade

    def getinfo(self):
        print("Welcome, ",self.first_name, self.last_name,". Your grade is",self.grade)


x = Student("John","Doe", 4)
x.getinfo()