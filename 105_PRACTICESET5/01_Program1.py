# Given name = "Virat Kohli", print only "Kohli" using slicing
name = "Virat Kohli"
print(name[6:])

# Count how many times "a" appears in "Bangalore Karnataka"

text="Bangalore Karnataka"
print(text.count('a'))

# Reverse the string "Python" using slicing

str="Python"
print(str[::-1])

# Clean this messy string: "   HELLO WORLD   " → make it "hello world"

text = "   HELLO WORLD   "

cleaned = text.strip().lower()
print(cleaned)

'''
strip() → removes spaces from beginning and end
lower() → converts all characters to lowercase
'''
# Given sentence = "I love cricket and Python",
#  replace "cricket" with "coding" and print it

sen="I love cricket and Python"
print(sen.replace("cricket","coding"))

# Check if "gmail.com" is present in "user@gmail.com" and print True/False

ee="user@gmail.com"
print("gmail.com"in ee)

text = "Hello, World!"

print(text[7])
print(text[-1])
print(text[0:5])
print(text[::-1])
print(len(text))
print(text.replace("World", "Python").upper())
print(text.split(", "))