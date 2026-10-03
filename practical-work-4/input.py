from domains.student import Student
from domains.course import Course


def read_int(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter an integer.")


def read_mark(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 10:
                return value
            print("Mark must be between 0 and 10.")
        except ValueError:
            print("Please enter a number.")


def input_students():
    result = []
    number = read_int("Enter number of students: ", 0)

    for i in range(number):
        print(f"\nStudent {i + 1}")
        student_id = input("  ID: ").strip()
        name = input("  Name: ").strip()
        dob = input("  Date of birth: ").strip()
        result.append(Student(student_id, name, dob))

    return result


def input_courses():
    result = []
    number = read_int("\nEnter number of courses: ", 0)

    for i in range(number):
        print(f"\nCourse {i + 1}")
        course_id = input("  ID: ").strip()
        name = input("  Name: ").strip()
        credits = read_int("  Credits: ", 1)
        result.append(Course(course_id, name, credits))

    return result


def input_marks(students, courses):
    if not students or not courses:
        print("Please input students and courses first.")
        return

    course_id = input("Select course ID: ").strip()
    course = next((c for c in courses if c.id == course_id), None)

    if course is None:
        print("Course not found.")
        return

    print(f"\nInput marks for {course.name}")
    for student in students:
        mark = read_mark(f"  {student.id} - {student.name}: ")
        student.set_mark(course_id, mark)
