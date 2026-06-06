fruits = ["apple", "banana", "mango", "grape", "kiwi"]
#          0         1         2        3        4
#         -5        -4        -3       -2       -1

# Indexing
print(fruits[0])      # apple
print(fruits[2])      # mango
print(fruits[-1])     # kiwi   — last item
print(fruits[-2])     # grape  — second from last

# Slicing
print(fruits[1:4])    # ['banana', 'mango', 'grape']
print(fruits[:3])     # ['apple', 'banana', 'mango']
print(fruits[2:])     # ['mango', 'grape', 'kiwi']
print(fruits[::-1])   # ['kiwi', 'grape', 'mango', 'banana', 'apple']