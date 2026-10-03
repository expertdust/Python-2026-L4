"""
Practical Work 3
Student Mark Management:
- OOP
- math.floor() for round-down to one decimal
- NumPy weighted GPA
- sort students by GPA descending
- curses-based UI decoration
"""

import curses
import math
import numpy as np


class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # course_id -> mark

    def set_mark(self, course_id, mark):
        # Round down to one decimal place.
        mark = math.floor(mark * 10) / 10
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id)

    def gpa(self, courses):
        weighted_marks = []
        credits = []

        for course in courses:
            mark = self.get_mark(course.id)
            if mark is not None:
                weighted_marks.append(mark)
                credits.append(course.credits)

        if not weighted_marks:
            return 0.0

        marks_array = np.array(weighted_marks, dtype=float)
        credits_array = np.array(credits, dtype=float)

        return float(np.average(marks_array, weights=credits_array))

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
    return next((s for s in students if s.id == student_id), None)


def find_course(course_id):
    return next((c for c in courses if c.id == course_id), None)


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
    students.clear()
    number = read_int("Enter number of students: ", 0)

    for i in range(number):
        print(f"\nStudent {i + 1}")
        student_id = input("  ID: ").strip()
        name = input("  Name: ").strip()
        dob = input("  Date of birth: ").strip()
        students.append(Student(student_id, name, dob))


def input_courses():
    courses.clear()
    number = read_int("\nEnter number of courses: ", 0)

    for i in range(number):
        print(f"\nCourse {i + 1}")
        course_id = input("  ID: ").strip()
        name = input("  Name: ").strip()
        credits = read_int("  Credits: ", 1)
        courses.append(Course(course_id, name, credits))


def input_marks():
    if not students or not courses:
        print("Please input students and courses first.")
        return

    list_courses()
    course_id = input("\nSelect course ID: ").strip()
    course = find_course(course_id)

    if course is None:
        print("Course not found.")
        return

    print(f"\nInput marks for {course.name}")
    for student in students:
        mark = read_mark(f"  {student.id} - {student.name}: ")
        student.set_mark(course_id, mark)

    print("Marks saved and rounded down to one decimal place.")


def list_courses():
    print("\nCOURSES")
    print("-" * 60)
    print(f"{'ID':<12} {'Name':<32} {'Credits':>7}")
    print("-" * 60)
    for course in courses:
        print(course)


def list_students():
    print("\nSTUDENTS")
    print("-" * 65)
    print(f"{'ID':<12} {'Name':<25} {'DoB':<15} GPA")
    print("-" * 65)

    for student in students:
        print(
            f"{student.id:<12} {student.name:<25} "
            f"{student.dob:<15} {student.gpa(courses):.1f}"
        )


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
        text = "N/A" if mark is None else f"{mark:.1f}"
        print(f"{student.id:<12} {student.name:<25} {text}")


def show_gpa():
    print("\nSTUDENT GPA")
    print("-" * 55)
    for student in students:
        print(f"{student.id:<12} {student.name:<25} {student.gpa(courses):.2f}")


def sort_students_by_gpa():
    students.sort(key=lambda student: student.gpa(courses), reverse=True)


def normal_menu():
    while True:
        print("""
================ STUDENT MARK MANAGEMENT ================
1. Input marks
2. List courses
3. List students (with GPA)
4. Show marks for a course
5. Show GPA
6. Sort students by GPA descending
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
        elif choice == "5":
            show_gpa()
        elif choice == "6":
            sort_students_by_gpa()
            print("Students sorted by GPA descending.")
            list_students()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")


def curses_menu(stdscr):
    curses.curs_set(0)
    selected = 0
    items = [
        "Input marks",
        "List courses",
        "List students",
        "Show marks",
        "Show GPA",
        "Sort by GPA descending",
        "Exit",
    ]

    while True:
        stdscr.clear()
        stdscr.addstr(1, 4, "STUDENT MARK MANAGEMENT - PRACTICAL WORK 3",
                      curses.A_BOLD)

        for i, item in enumerate(items):
            prefix = ">> " if i == selected else "   "
            attr = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(3 + i, 4, prefix + item, attr)

        stdscr.addstr(
            12, 4,
            "Use UP/DOWN and ENTER. Press q to quit.",
            curses.A_DIM,
        )
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(items)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(items)
        elif key in (10, 13):
            if selected == 0:
                curses.endwin()
                input_marks()
                stdscr.clear()
            elif selected == 1:
                curses.endwin()
                list_courses()
                input("Press Enter...")
                stdscr.clear()
            elif selected == 2:
                curses.endwin()
                list_students()
                input("Press Enter...")
                stdscr.clear()
            elif selected == 3:
                curses.endwin()
                show_student_marks()
                input("Press Enter...")
                stdscr.clear()
            elif selected == 4:
                curses.endwin()
                show_gpa()
                input("Press Enter...")
                stdscr.clear()
            elif selected == 5:
                sort_students_by_gpa()
                curses.endwin()
                print("Students sorted by GPA descending.")
                list_students()
                input("Press Enter...")
                stdscr.clear()
            elif selected == 6:
                break
        elif key in (ord("q"), ord("Q")):
            break


def main():
    input_students()
    input_courses()

    # The course explicitly asks for curses decoration.
    try:
        curses.wrapper(curses_menu)
    except curses.error:
        # Fallback for terminals that do not provide a usable curses screen.
        print("\nCurses UI is unavailable; using normal terminal UI.")
        normal_menu()


if __name__ == "__main__":
    main()
