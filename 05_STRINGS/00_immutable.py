text = "hello"

text[0] = "H"   # trying to change 'h' → 'H'
# TypeError: 'str' object does not support item assignment

# Correct way (create a new string)
text = "hello"

new_text = "H" + text[1:]
print(new_text)

# A string is immutable in Python, which means:

# 👉 Once a string is created, it cannot be changed.

# You can’t modify its characters in place. 
# Any “change” actually creates a new string object.
    
