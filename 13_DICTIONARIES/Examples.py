# Examples
# Easy — Word frequency counter:
pythonwords = ["apple", "banana", "apple", "mango", "banana", "apple"]

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)    # {'apple': 3, 'banana': 2, 'mango': 1}


# Medium — Common elements in two lists:

pythonlist1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
only_in_1 = set1 - set2
only_in_2 = set2 - set1

print(f"Common: {common}")        # {4, 5, 6}
print(f"Only in list1: {only_in_1}")  # {1, 2, 3}
print(f"Only in list2: {only_in_2}")  # {7, 8, 9}

# Tricky — Invert a dictionary:

pythonoriginal = {"a": 1, "b": 2, "c": 3}

# Swap keys and values
inverted = {value: key for key, value in original.items()}
print(inverted)    # {1: 'a', 2: 'b', 3: 'c'}