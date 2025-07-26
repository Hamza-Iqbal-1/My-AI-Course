# String Manipulation 
'''1. Write a program to create a new string made of an input string’s first, 
middle, and last character.'''

str = input("Enter a string: ")
length = len(str)
first = str[0]
last = str[-1]
middle_index = length // 2
middle = str[middle_index]
new_str = first + middle + last
print("New string:", new_str)

'''2. Write a program to count occurrences of all characters within a string 
Given.'''

text = input("Enter a string: ")
# Check each character only once
for char in set(text):
    print(f"{char} : {text.count(char)}")

'''3. Reverse a given string'''

str = input('Enter a string: ')
rev_str = str[::-1]
print(rev_str)

'''4. Split a string on hyphens'''

str = input("Enter a hyphen-separated string: ")
spl_str = str.split("-")
print("Splitted string:", spl_str)

'''5. Remove special symbols / punctuation from a string '''

import string
str = input("Enter a string with special symbols: ")
# Remove punctuation
cleaned = ""
for char in str:
    if char not in string.punctuation:
        cleaned += char

print("Cleaned string:", cleaned)

# List Manipulation

'''.  Reverse a list in Python'''

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

'''2. Turn every item of a list into its square '''

my_list = [2, 3, 4, 5]
for i in my_list:
    print(i**2)

'''3. Remove empty strings from the list of strings '''

my_list = ['hamza', '', 'ali', '', 'hammad', '']
my_list = [i for i in my_list if i != '']
print(my_list)


'''4. Add new item to list after a specified item '''

my_list = ['apple', 'banana', 'cherry']
new_item = 'mango'
after_item = 'banana'

# Find the index of the item after which to insert
index = my_list.index(after_item)

# Insert the new item at the next position
my_list.insert(index + 1, new_item)

print(my_list)


'''5. Replace list’s item with new value if found'''

my_list = ['apple', 'banana', 'cherry']
old_item = 'banana'
new_item = 'mango'

if old_item in my_list:
    index = my_list.index(old_item)
    my_list[index] = new_item

print(my_list)

# Dictionary Manipulation

'''1.  Check if a value exists in a dictionary '''

my_dict = {
    'name': 'Hamza',
    'age': 21,
    'city': 'Lahore'
}
value = 'Hamza'
# Check if value exists
if value in my_dict.values():
    print("Value exists in the dictionary.")
else:
    print("Value not found.")


'''2.  Get the key of a minimum value from the following dictionary '''

my_dict = {
    'a': 50,
    'b': 20,
    'c': 80,
    'd': 10
}
# Get key with minimum value
min_key = min(my_dict, key=my_dict.get)
print("Key with minimum value:", min_key)
max_key = max(my_dict, key=my_dict.get)
print("Key with maximum value:", max_key)

'''3.  Delete a list of keys from a dictionary'''

my_dict = {
    'a': 50,
    'b': 20,
    'c': 80,
    'd': 10
}
keys_to_remove = ['a', 'b']

for key in keys_to_remove:
    if key in my_dict:
        del my_dict[key]

print(my_dict)

# Tuple Manipulation

'''1. Reverse the tuple '''

my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)


'''2.  Access value 20 from the tuple '''

my_tuple = (10, 20, 30, 40)
print(my_dict[1])

'''3. Swap two tuples in Python '''

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Swapping
tuple1, tuple2 = tuple2, tuple1

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# Loop Manipulation 
'''1. Print first 10 natural numbers using while '''

i = 1
while i <= 10:
    print(i)
    i += 1

'''2.  Take Input from user , and print even number till that input number '''

n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


'''3.  Take Input from user , and print odd number till that input number '''

n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1

'''4. Take Input from user , and print prime number till that input number '''

n = int(input("Enter a number: "))
i = 2
while i <= n:
    is_prime = True
    j = 2
    while j < i:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        print(i)
    i += 1

'''5  Print multiplication table of a given number '''

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
