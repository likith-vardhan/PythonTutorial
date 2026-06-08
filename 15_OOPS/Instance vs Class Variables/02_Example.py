class Student:
    school_name = "Sunrise Academy"   # Class variable
    passing_marks = 40                # Class variable — school-wide rule
    total_students = 0                # Class variable — counter

    def __init__(self, name, roll_no, marks):
        self.name = name              # Instance variable
        self.roll_no = roll_no        # Instance variable
        self.marks = marks            # Instance variable (list)
        Student.total_students += 1

    def average(self):
        return sum(self.marks) / len(self.marks)

    def result(self):
        avg = self.average()
        status = "PASS ✅" if avg >= Student.passing_marks else "FAIL ❌"
        print(f"[{Student.school_name}] {self.name} (Roll: {self.roll_no})")
        print(f"Average: {avg:.1f} → {status}")

    @classmethod
    def update_passing_marks(cls, new_marks):
        # We'll cover classmethods in the next topic
        cls.passing_marks = new_marks
        print(f"Passing marks updated to {new_marks}")


s1 = Student("Rahul", 101, [85, 90, 78, 92])
s2 = Student("Priya", 102, [35, 42, 38, 30])
s3 = Student("Amit", 103, [55, 60, 70, 65])

s1.result()
# [Sunrise Academy] Rahul (Roll: 101)
# Average: 86.2 → PASS ✅

s2.result()
# [Sunrise Academy] Priya (Roll: 102)
# Average: 36.2 → FAIL ❌

print(f"Total Students Enrolled: {Student.total_students}")  # 3