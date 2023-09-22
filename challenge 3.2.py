class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Function to get student details from user input
def get_student_details():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    cgpa = float(input("Enter CGPA: "))
    return Student(name, roll_number, cgpa)

# Get a list of students from user input
num_students = int(input("Enter the number of students: "))
students = [get_student_details() for _ in range(num_students)]

# Sort the students based on CGPA
sorted_students = sort_students(students)

# Display sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
