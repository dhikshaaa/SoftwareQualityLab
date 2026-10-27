
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

    def get_result(self):
        """Return the student's result."""
        if self.mark >= 50:
            return "Pass"
        return "Fail"


student = Student("John", 20, 85)
student.display_details()
print(f"Result: {student.get_result()}")
