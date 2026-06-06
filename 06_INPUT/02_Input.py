# age = input("Enter your age: ")
# # User types: 22

# print(age)          # 22
# print(type(age))    # <class 'str'>  ← NOT int! It's a string "22"

age = input("Enter your age: ")
# User types: 22

print(age + 1)      # ❌ Error! Can't add string and int
print(age + age)    # "2222" ← string repetition, not math!

