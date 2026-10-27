"""
Student management program.
Demonstrates coding standards and refactoring.
"""


class Student:
    """Represents student information."""

    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def display_details(self):
        """Display student details."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Mark: {self.mark}")


student = Student("John", 20, 85)
student.display_details()
