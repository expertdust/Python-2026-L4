students = []
courses = []
marks = {}


def input_students():
    number = int(input("Enter number of students: "))

    for i in range(number):
        print(f"\nStudent {i + 1}")
        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)


def input_courses():
    number = int(input("\nEnter number of courses: "))

    for i in range(number):
        print(f"\nCourse {i + 1}")
        course_id = input("ID: ")
        name = input("Name: ")

        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)


def input_marks():
    if len(courses) == 0:
        print("No courses available.")
        return

    if len(students) == 0:
        print("No students available.")
        return

    print("\nCourses:")
    list_courses()

    course_id = input("Select course ID: ")

    course_exists = False

    for course in courses:
        if course["id"] == course_id:
            course_exists = True
            break

    if not course_exists:
        print("Course not found.")
        return

    marks[course_id] = {}

    for student in students:
        mark = float(
            input(f"Enter mark for {student['name']} ({student['id']}): ")
        )

        marks[course_id][student["id"]] = mark


def list_courses():
    print("\n=== Courses ===")

    for course in courses:
        print(
            f"ID: {course['id']}, "
            f"Name: {course['name']}"
        )


def list_students():
    print("\n=== Students ===")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"DoB: {student['dob']}"
        )


def show_student_marks():
    if len(marks) == 0:
        print("No marks available.")
        return

    list_courses()

    course_id = input("Enter course ID: ")

    if course_id not in marks:
        print("No marks found for this course.")
        return

    print("\n=== Student Marks ===")

    for student in students:
        student_id = student["id"]

        if student_id in marks[course_id]:
            print(
                f"ID: {student_id}, "
                f"Name: {student['name']}, "
                f"Mark: {marks[course_id][student_id]}"
            )


def main():
    input_students()
    input_courses()

    while True:
        print("\n========== MENU ==========")
        print("1. Input marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            input_marks()

        elif choice == "2":
            list_courses()

        elif choice == "3":
            list_students()

        elif choice == "4":
            show_student_marks()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()