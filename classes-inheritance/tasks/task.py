# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'"Name: {self.name}, Age: {self.age}"'

class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int = None):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        if self.salary == None:
            return f'Name: {self.name}, Age: {self.age}'
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int = None):
        self.name = name
        self.age = age
        self.grades = grades

    def show(self):
        if self.grades == None:
            return f'Name: {self.name}, Age: {self.age}'
        return f'Name: {self.name}, Age: {self.age}, Grades: {self.grades}'

if __name__ == "__main__":
    # check if this code is working
    persons = [Teacher("Mr.Snape", 40), Student("Harry", 16, [5, 6, 7, 3])]

    for person in persons:
        print(person.show())