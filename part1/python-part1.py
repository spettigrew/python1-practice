# print hello world
print("Hello, World!")

# declare a variable
name = "Sara"

# print a variable
print(name)

# String concatenation
print("Hello, " + name )

# `Hello ${name}`
print(f'Hello {name}')

### Data Structures

# List (In python, they are called lists, not arrays)
p = [10, 60, 20, 5, "Banana"]
print(p)

# add an element to the end of P
p.append(77)
print(p)

# Let's loop over the list P, and print every element. For every element in P, do some sort of code. A colon : indicates the start of a coding block.
for element in p:
    print(element)
    """this 'for loop' is now complete"""
print(" we printed it again")

# Let's print the index and the element at the index of P. enum = enumerate
#enumerate(p) => [(0, 10), (1, 60), (2, 20) ... ]
for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]}')

# List comprehensions. Another way to create a list.
numbers = [1, 4, 9, 14, 32]
#create a new list, of squares from the numbers list
#this is the non-fancy way of using this list. Non verbose.
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

#List comprehensions. For each element from numbers, multiply by itself, and add to the cooler_squares
# [ funciton(variable) fir variable in some_list]
cooler_squares = [num*num] for num in numbers
print(cooler_squares)

# Create a list of just even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

names = ["Sara", "sam", "Bob", "Frank", "sandy", "Kyle"]
#create a new list containing only names that start with 's'
#Also all names should be capitalized

s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)
#Note: upper() makes everything uppercase

# Dictionaries (objects, maps, hashmaps in JS)
# A key:value data structure
new_dict = {}

# create a dictionary with some keys and values

food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}
print(food_dict)

# Add a new key:value pair
food_dict['cucumber'] = 'is a frankly a fruit'
print(food_dict)

# access and print a specific element in food_dict
chosen_food = 'apple'

#food_dict.apple is not allowed in P (only JS)
print(food_dict[chosen_food])

# Iterate through the keys and values of a dictionary. For element in dict, do some code
for key, value in food_dict.items():
    print(f'{key} : {value}')

# How can we check if an element exists in a dictionary?
# is apple in food_dict?
print('apple' in food_dict)
print('banana' in food_dict)


### Tuples and Sets
# Tuples (like const in JS)
tup = (1, 2, 3, 4)
for item in tup:
    print(item)

#access a particular element
print(tup[1])

# Can NOT modify tub in any way. ex: tup[1] = 'new_thing'

# Sets are basically dictionaries without values. The set is unordered. An Array (or list) keeps it in order. Sets are mutable
fruit = {'cucumber', 'apple', 'banana'}
fruit.add('pizza')
fruit_array = ['cucumber', 'apple', 'banana']

for item in fruit:
    print(tiem)

if 'cucumber' in fruit:
    print("It's hard to think that a cucumber is a fruit.")

# This is very  inefficient
if 'cucumber' in fruit_array:
    print("It's hard to think that a cucumber is a fruit and please use a set.")

