# Project: Student Management System

# 1. Student class definition
class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

# 2. StudentManagement class for handling operations
class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.roll_no] = student

    def get_student(self, roll_no):
        return self.students.get(roll_no)

    def list_all_students(self):
        return list(self.students.values())

# 3. Main program with user interface
def main():
    system = StudentManagement()
    
    while True:
        print("\n1. Add Student")
        print("2. Add Grade")
        print("3. View Student")
        print("4. List All Students")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            age = int(input("Enter age: "))
            student = Student(name, roll_no, age)
            system.add_student(student)
            print("Student added successfully!")

        elif choice == "2":
            roll_no = input("Enter roll number: ")
            student = system.get_student(roll_no)
            if student:
                subject = input("Enter subject: ")
                grade = float(input("Enter grade: "))
                student.add_grade(subject, grade)
                print("Grade added successfully!")
            else:
                print("Student not found!")

        elif choice == "3":
            roll_no = input("Enter roll number: ")
            student = system.get_student(roll_no)
            if student:
                print(f"\nName: {student.name}")
                print(f"Roll No: {student.roll_no}")
                print(f"Age: {student.age}")
                print(f"Average Grade: {student.get_average():.2f}")
                print("Grades:", student.grades)
            else:
                print("Student not found!")

        elif choice == "4":
            students = system.list_all_students()
            print("\nAll Students:")
            for student in students:
                print(f"Name: {student.name}, Roll No: {student.roll_no}")

        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()