class Person:
    def __init__(self, first_name, last_name, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.gpa = gpa
    
    def display_info(self):
        
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.gpa}")

class Teacher(Person):
    def __init__(self, first_name, last_name, age, teacher_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.teacher_id = teacher_id
        self.salary = salary
    
    def display_info(self):
        
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Salary: {self.salary}")
print("___student's details___")
student = Student("peter", "parker", 20, "S12345", 3.8)
student.display_info()

print("___teacher's details___")

teacher = Teacher("tony", "stark", 45, "T98765", 9999999)
teacher.display_info()
