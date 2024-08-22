
class Student:
    student_name = "Ahmed"
    student_class = "four"
    student_section = "A"
    def showStd(self):
        print(f"The student {self.student_name} is studying in {self.student_class} at section {self.student_section} ")

class Teacher:
    teacher_name = "Ali"
    teacher_subject = "Maths"
    def showTeacher(self):
        print(f"The teacher {self.teacher_name} is teaching {self.teacher_subject}")

class schoolData(Student , Teacher):
    school_name = "MnM"
    def school(self):
        print(f"The school is {self.school_name}")

Data = schoolData()
Data.showStd()
Data.showTeacher()
Data.school()

