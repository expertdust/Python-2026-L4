import math
import numpy as np


class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def set_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10

    def get_mark(self, course_id):
        return self.marks.get(course_id)

    def gpa(self, courses):
        marks = []
        credits = []

        for course in courses:
            mark = self.get_mark(course.id)
            if mark is not None:
                marks.append(mark)
                credits.append(course.credits)

        if not marks:
            return 0.0

        return float(
            np.average(
                np.array(marks, dtype=float),
                weights=np.array(credits, dtype=float),
            )
        )

    def __str__(self):
        return f"{self.id:<12} {self.name:<25} {self.dob}"
