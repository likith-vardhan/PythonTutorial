age = 25
has_id = True

# AND — both conditions must be True
print(age >= 18 and has_id == True)   # True

# OR — at least one condition must be True
print(age < 18 or has_id == True)     # True

# NOT — flips True to False, False to True
print(not has_id)                     # False
print(not (age < 18))                 # True