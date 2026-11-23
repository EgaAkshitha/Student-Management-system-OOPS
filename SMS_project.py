from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    @abstractmethod
    def display(self):
        pass


# Student Class (Encapsulation)
class Student(Person):
    def __init__(self, student_id, name, age):
        self.__student_id = student_id
        self.__name = name
        self.__age = age
        self.courses = []
        self.marks = {}

    # Getter Methods
    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def enroll_course(self, course):
        self.courses.append(course)

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def calculate_grade(self):
        if not self.marks:
            return "No Grade"

        avg = sum(self.marks.values()) / len(self.marks)

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    # Polymorphism
    def display(self):
        print("\nStudent Details")
        print("ID:", self.__student_id)
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Courses:", ", ".join(self.courses))
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# Course Class
class Course:
    def __init__(self, course_name):
        self.course_name = course_name


# School Class (Composition)
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def search_student(self, student_id):
        for student in self.students:
            if student.get_id() == student_id:
                return student
        return None


# Main Program
school = School("ABC College")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Enroll in Course")
    print("3. Add Marks")
    print("4. View Student Details")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        student = Student(sid, name, age)
        school.add_student(student)

        print("Student Added Successfully!")

    elif choice == "2":
        sid = input("Enter Student ID: ")
        student = school.search_student(sid)

        if student:
            course = input("Enter Course Name: ")
            student.enroll_course(course)
            print("Course Assigned!")
        else:
            print("Student Not Found!")

    elif choice == "3":
        sid = input("Enter Student ID: ")
        student = school.search_student(sid)

        if student:
            subject = input("Enter Subject: ")
            mark = float(input("Enter Marks: "))
            student.add_marks(subject, mark)
            print("Marks Added!")
        else:
            print("Student Not Found!")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        student = school.search_student(sid)

        if student:
            student.display()
        else:
            print("Student Not Found!")

    elif choice == "5":
        sid = input("Enter Student ID: ")
        student = school.search_student(sid)

        if student:
            print("Student Found!")
            student.display()
        else:
            print("Student Not Found!")

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")