"""
Practical Work 2
Student Mark Management - Object-Oriented version.

This version is based on Practical Work 1b and changes the
student/course/mark data from dictionaries into classes.
"""

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # course_id -> mark

    def set_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id)

    def __str__(self):
        return f"{self.id:<12} {self.name:<25} {self.dob}"


class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.id:<12} {self.name:<30} {self.credits:>3}"


students = []
courses = []


def find_student(student_id):
    for student in students:
        if student.id == student_id:
            return student
    return None


def find_course(course_id):
    for course in courses:
        if course.id == course_id:
            return course
    return None


def input_students():
    students.clear()
    number = int(input("Enter number of students: "))

    for i in range(number):
        print(f"\nStudent {i + 1}")
        student_id = input("  ID: ").strip()
        name = input("  Name: ").strip()
        dob = input("  Date of birth: ").strip()
        students.append(Student(student_id, name, dob))


def input_courses():
    courses.clear()
    number = int(input("\nEnter number of courses: "))

    for i in range(number):
        print(f"\nCourse {i + 1}")
        course_id = input("  ID: ").strip()
        name = input("  Name: ").strip()
        credits = int(input("  Credits: "))
        courses.append(Course(course_id, name, credits))


def input_marks():
    if not students:
        print("No students.")
        return

    if not courses:
        print("No courses.")
        return

    list_courses()
    course_id = input("\nSelect course ID: ").strip()

    course = find_course(course_id)
    if course is None:
        print("Course not found.")
        return

    print(f"\nInput marks for {course.name}")
    for student in students:
        while True:
            try:
                mark = float(input(f"  {student.id} - {student.name}: "))
                if 0 <= mark <= 10:
                    student.set_mark(course_id, mark)
                    break
                print("  Mark must be between 0 and 10.")
            except ValueError:
                print("  Please enter a number.")


def list_courses():
    print("\nCOURSES")
    print("-" * 55)
    print(f"{'ID':<12} {'Name':<30} {'Credits':>7}")
    print("-" * 55)
    for course in courses:
        print(course)


def list_students():
    print("\nSTUDENTS")
    print("-" * 55)
    print(f"{'ID':<12} {'Name':<25} DoB")
    print("-" * 55)
    for student in students:
        print(student)


def show_student_marks():
    if not courses:
        print("No courses.")
        return

    list_courses()
    course_id = input("\nSelect course ID: ").strip()

    course = find_course(course_id)
    if course is None:
        print("Course not found.")
        return

    print(f"\nMARKS - {course.name}")
    print("-" * 50)
    for student in students:
        mark = student.get_mark(course_id)
        mark_text = "N/A" if mark is None else f"{mark:.1f}"
        print(f"{student.id:<12} {student.name:<25} {mark_text}")


def menu():
    while True:
        print("""
================ STUDENT MARK MANAGEMENT ================
1. Input marks
2. List courses
3. List students
4. Show student marks for a course
0. Exit
==========================================================
""")
        choice = input("Choose: ").strip()

        if choice == "1":
            input_marks()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_student_marks()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


def main():
    try:
        input_students()
        input_courses()
        menu()
    except ValueError:
        print("Invalid numeric input.")


if __name__ == "__main__":
    main()
