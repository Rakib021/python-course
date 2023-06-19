class Student :
    def __init__(self,name,id,current_class):
        self.name = name
        self.id = id
        self.current_class = current_class
    def __repr__(self)->str:
        return f'student with name {self.name} her id is :{self.id} and she reads in {self.current_class}'

class Teacher :
    def __init__(self,name,subject,id,phone):
        self.name=name
        self.subject = subject
        self.id=id
        self.phone = phone
    def __repr__(self):
        return f'Teacher name : {self.name} teacher teaching us {self.subject} and his id is {self.id} and his phone number is : {self.phone}'
class School :
    def __init__(self,name):
        self.name=name
        self.teachers =[]
        self.students=[]

    def add_to_teacher(self,id,name,subject):
        id = len(self.teachers) +101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    
    def enroll(self,name,id,fee):
        if fee <6500:
            return 'not enough fee'
        else:
            id = len(self.students) +1
            student = Student(name, id, 'c++')
            self.students.append(student)
            return f'{name} is enrolled this course with id :{id} and have extra money :{fee-6500}'



    
# alia = Student('alia', 45, 9)
# print(alia)

# teacher = Teacher('Rahim', 'Computer graphics', 121, 123456)
# print(teacher)

phitron = School('Phitron')
phitron.enroll('firoj khan', 1, 5400)