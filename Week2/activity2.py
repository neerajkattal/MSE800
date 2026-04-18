

#  variable to (stores all students)
students_list = []


# Class definition
class Student:
    def __init__(self, studentName, age, student_id):
        self.studentName = studentName
        self.age = age
        self.student_id = student_id


# Function to collect student data
def collect_students():
    global students_list  # accessing global variable

    for i in range(3):  # minimum of 3 students
      print(f"\nEnter details for student {i + 1}")

      studentName = input("Name: ")
      age = int(input("Age: "))
      student_id = int(input("Student ID: "))

      # create Student object (local variable)
      student = Student(studentName, age, student_id)

      students_list.append(student)


# Function to display sorted students
def display_students():
    # local variable (sorted list)
    sorted_students = sorted(students_list, key=lambda s: s.age)

    print("\nStudents sorted by age:")
    for student in sorted_students:
        print(f"Name: {student.studentName}, Age: {student.age}")


# Entry point
if __name__ == "__main__":
    collect_students()
    display_students()

    