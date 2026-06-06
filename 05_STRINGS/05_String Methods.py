text = "  hello, world!  "

# Case methods
print(text.upper())       # "  HELLO, WORLD!  "
print(text.lower())       # "  hello, world!  "
print(text.title())       # "  Hello, World!  "
print(text.capitalize())  # "  hello, world!  " (only first char)

# Cleaning methods
print(text.strip())       # "hello, world!"  (removes spaces from both ends)
print(text.lstrip())      # "hello, world!  " (left side only)
print(text.rstrip())      # "  hello, world!" (right side only)

# Search methods
print(text.find("world"))    # 9  (index where "world" starts)
print(text.count("l"))       # 3  (how many times "l" appears)
print(text.startswith("  h")) # True
print(text.endswith("!  "))   # True

# Replace method
print(text.replace("world", "Python"))  # "  hello, Python!  "

# Split method — breaks string into a list
sentence = "I love Python"
print(sentence.split())        # ['I', 'love', 'Python']
print(sentence.split("o"))     # ['I l', 've Pyth', 'n']


# Checking String Content

text = "Python3"

print(text.isalpha())    # False — has a number
print(text.isdigit())    # False — has letters
print(text.isalnum())    # True  — letters AND numbers only
print("  ".isspace())    # True  — only spaces
print("HELLO".isupper()) # True
print("hello".islower()) # True