import curses

from input import input_students, input_courses, input_marks
from output import list_courses, list_students, show_marks, show_gpa


def normal_menu(students, courses):
    while True:
        print("""
================ PW4 STUDENT MARK MANAGEMENT ================
1. Input marks
2. List courses
3. List students
4. Show marks
5. Show GPA
6. Sort students by GPA descending
0. Exit
==============================================================
""")
        choice = input("Choose: ").strip()

        if choice == "1":
            input_marks(students, courses)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students, courses)
        elif choice == "4":
            show_marks(students, courses)
        elif choice == "5":
            show_gpa(students, courses)
        elif choice == "6":
            students.sort(
                key=lambda student: student.gpa(courses),
                reverse=True,
            )
            print("Students sorted by GPA descending.")
            list_students(students, courses)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def curses_app(stdscr, students, courses):
    curses.curs_set(0)
    selected = 0
    items = [
        "Input marks",
        "List courses",
        "List students",
        "Show marks",
        "Show GPA",
        "Sort students by GPA descending",
        "Exit",
    ]

    while True:
        stdscr.clear()
        stdscr.addstr(1, 4, "STUDENT MARK MANAGEMENT - PW4", curses.A_BOLD)

        for i, item in enumerate(items):
            prefix = ">> " if i == selected else "   "
            attr = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(3 + i, 4, prefix + item, attr)

        stdscr.addstr(12, 4, "UP/DOWN + ENTER, q to quit", curses.A_DIM)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(items)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(items)
        elif key in (10, 13):
            if selected == 0:
                curses.endwin()
                input_marks(students, courses)
                input("Press Enter...")
            elif selected == 1:
                curses.endwin()
                list_courses(courses)
                input("Press Enter...")
            elif selected == 2:
                curses.endwin()
                list_students(students, courses)
                input("Press Enter...")
            elif selected == 3:
                curses.endwin()
                show_marks(students, courses)
                input("Press Enter...")
            elif selected == 4:
                curses.endwin()
                show_gpa(students, courses)
                input("Press Enter...")
            elif selected == 5:
                students.sort(
                    key=lambda student: student.gpa(courses),
                    reverse=True,
                )
                curses.endwin()
                print("Students sorted by GPA descending.")
                list_students(students, courses)
                input("Press Enter...")
            else:
                break
        elif key in (ord("q"), ord("Q")):
            break


def main():
    students = input_students()
    courses = input_courses()

    try:
        curses.wrapper(curses_app, students, courses)
    except curses.error:
        print("\nCurses UI unavailable; using normal terminal UI.")
        normal_menu(students, courses)


if __name__ == "__main__":
    main()
