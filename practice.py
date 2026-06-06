class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Creating objects
r1 = Rectangle(2, 3)
r2 = Rectangle(4, 5)

# Calling methods
print("Area of r1:", r1.area())
print("Area of r2:", r2.area())

print("Perimeter of r1:", r1.perimeter())
print("Perimeter of r2:", r2.perimeter())


# Problem 2:
# Create a Student class with name, roll_number, and marks (a list). 
# Add a method average_marks() that returns the average. 
# Add a method is_passed() that returns True if average ≥ 40.


class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks   # list of marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def is_passed(self):
        return self.average_marks() >= 40


# Creating objects
s1 = Student("Likith", 101, [50, 60, 70])
s2 = Student("Ravi", 102, [30, 35, 25])

# Testing
print(s1.name, "Average:", s1.average_marks(), "Passed:", s1.is_passed())
print(s2.name, "Average:", s2.average_marks(), "Passed:", s2.is_passed())


# Problem 3:
# Create a Library class with a books list. 
# Add methods: add_book(title), remove_book(title), show_books(). 
# Create an object and test all three methods.

class Library:
    def __init__(self):
        self.books = []   # empty list initially

    def add_book(self, title):
        self.books.append(title)
        print(f'"{title}" added to library')

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f'"{title}" removed from library')
        else:
            print(f'"{title}" not found')

    def show_books(self):
        if not self.books:
            print("Library is empty")
        else:
            print("Books in library:")
            for book in self.books:
                print("-", book)


# Creating object
lib = Library()

# Testing methods
lib.add_book("Python Basics")
lib.add_book("Data Structures")

lib.show_books()

lib.remove_book("Python Basics")

lib.show_books()

