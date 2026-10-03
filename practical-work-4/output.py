import curses


def list_courses(courses):
    print("\nCOURSES")
    print("-" * 60)
    print(f"{'ID':<12} {'Name':<32} {'Credits':>7}")
    print("-" * 60)
    for course in courses:
        print(course)


def list_students(students, courses):
    print("\nSTUDENTS")
    print("-" * 70)
    print(f"{'ID':<12} {'Name':<25} {'DoB':<15} GPA")
    print("-" * 70)

    for student in students:
        print(
            f"{student.id:<12} {student.name:<25} "
            f"{student.dob:<15} {student.gpa(courses):.2f}"
        )


def show_marks(students, courses):
    list_courses(courses)
    course_id = input("\nSelect course ID: ").strip()
    course = next((c for c in courses if c.id == course_id), None)

    if course is None:
        print("Course not found.")
        return

    print(f"\nMARKS - {course.name}")
    print("-" * 55)

    for student in students:
        mark = student.get_mark(course_id)
        mark_text = "N/A" if mark is None else f"{mark:.1f}"
        print(f"{student.id:<12} {student.name:<25} {mark_text}")


def show_gpa(students, courses):
    print("\nGPA")
    print("-" * 50)
    for student in students:
        print(f"{student.id:<12} {student.name:<25} {student.gpa(courses):.2f}")


def curses_menu(stdscr, items):
    curses.curs_set(0)
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr(1, 4, "STUDENT MARK MANAGEMENT - PW4", curses.A_BOLD)

        for i, item in enumerate(items):
            prefix = ">> " if i == selected else "   "
            attr = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(3 + i, 4, prefix + item, attr)

        stdscr.addstr(
            3 + len(items) + 1,
            4,
            "UP/DOWN + ENTER, q to quit",
            curses.A_DIM,
        )
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(items)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(items)
        elif key in (10, 13):
            return selected
        elif key in (ord("q"), ord("Q")):
            return len(items) - 1


def run_curses_menu(items, callback):
    try:
        while True:
            choice = curses.wrapper(curses_menu, items)

            if choice == len(items) - 1:
                break

            should_exit = callback(choice)
            if should_exit:
                break
    except curses.error:
        print("Curses is unavailable in this terminal.")
