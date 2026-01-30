from Student import Student
from models import staff

student = Student(1234567890123, "aa", 20, "s11") 
Staff= staff(11223344556677, "bb", 200, 'st5')
print(f"Student : {Student.name}, age : {Student.age}, student id {Student.student_id}")
print(f"Staff : {Staff.name}, age : {Staff.age}, staff id {Staff.staff_id}")
print(Student)
print(Staff)