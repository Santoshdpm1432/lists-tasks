# names = [1,2,3,"santosh","ashok","nagaprasad"]
# print(names[0])
# print(names[3])

# indexing
# names = [1,2,3,"santosh","ashok","nagaprasad"]
# print(names[0])
# print(names[2])
# print(names[5])

# slicing
# sequence[start:stop:step]#syntax

# names = [1,2,3,"santosh","ashok","nagaprasad"]
# print(names[2:6])
# print(names[:])
# print(names[0:])
# print(names[:5])
# print(names[::])

# negative index
# names = [1,2,3,"santosh","ashok","nagaprasad"]
# print(names[-1])
# print(names[-2])
# print(names[-6])
# print(names[-4:])
# print(names[:-4])

# Skipping Characters (Step):skip by elements
# list = [0,1,2,3,4,5,6,7,8,9,10]
# print(list[::-1])
# print(list[::2])
# print(list[::-3])

# append

# list = [0,1,2,3,4,5,6,7,8,9,10]
# list.append("santosh")
# list.append(11)
# print(list)

# extend()
# Adds multiple elements (from another iterable) to the end of the list.
# list = [0,1,2,3,4,5,6,7,8,9,10]
# list.extend([11,12,13])
# list.extend(["santosh","ashok"])
# print(list)

# fruits = ["apple", "banana"]
# fruits.extend(["cherry", "mango"])
# print(fruits)

# copy()
# Creates a shallow copy of the list.
# fruits = ["apple", "banana"]
# copied_fruits = fruits.copy()
# print(copied_fruits)

# clear()
# Removes all elements from the list.

# list = [0,1,2,3,4,5,6,7,8,9,10]
# list.clear()
# print(list)

# count()
# Counts the occurrences of a specific element in the list.

# list = [0,1,2,3,3,3,3,3,4,5,6,7,8,8,8,8,8,8,9,10]
# print(list.count(8))

# index()
# Returns the index of the first occurrence of a specific element.

# list = [0,1,2,3,3,3,3,3,4,5,6,7,8,8,8,8,8,8,9,10]
# print(list.index(10))

# remove()
# Removes the first occurrence of a specific element from the list.

# list = [0,1,2,3,3,3,3,3,4,5,6,7,8,8,8,8,8,8,]
# list.remove(3)
# print(list)

# pop()
# Removes and returns an element at a specific index (default is the last element).

# list = [0,1,2,3,3,3,3,3,4,5,6,7,8,8,8,8,8,8,9,10]
# pop_list = list.pop(2)
# print(pop_list)
# print(list)

# insert()
# Inserts an element at a specific index.

# list = ["santosh","ashok","nagaprasad","rajasekhar"]
# inserted = list.insert(1,"raju")
# print(list)

# reverse()
# Reverses the order of elements in the list.

# list = ["santosh","ashok","nagaprasad","rajasekhar"]
# list.reverse()
# print(list)

# sort()
# Sorts the list in ascending (default) or descending order.

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)

# Nested List:
# A nested list is a list that contains other lists. This allows for creating a matrixlike structure or representing hierarchical data.
# list = [[1,2,3],[4,5,6],[7,8,9],"santosh"]
# print(list[1][0])
# print(list[3][0])

# list comprehansions
# List comprehensions provide a concise way to create lists. They consist of an
# expression followed by a for loop inside square brackets.
# Syntax
# [expression for item in iterable]
# empty_list = []
# for i in range(1,6):
#     empty_list.append(i**2)
#     print(empty_list)


# _________________tasks__________________
# task_1

# Reverse List:
# Write Python code to reverse the order of elements in the given list my_list .
# Print the reversed list.
# my_list = [10, 20, 30, 40, 50, 11]

# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse()
# print(my_list)


# task_2

# Given two lists list1 and list2 , find and print the common elements between
# them.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# list_1 = [[1, 2, 3, 4, 5],[4, 5, 6, 7, 8]]
# print(list_1[0][3])
# print(list_1[0][4])

# task_3
# Create a new list unique_list containing only the unique elements from the
# given list original_list . Print the unique list.
# original_list = [1, 2, 2, 3, 4, 4, 5]

# original_list = [1, 2, 2, 3, 4, 4, 5]
# original_list.remove(2)
# original_list.remove(4)
# print(original_list)

# task_4

# Remove duplicate elements from the given list duplicated_list and print the list
# without duplicates while preserving the order.
# list = [1, 2, 2, 3, 4, 4, 5]
# pop_list = list.pop(2)
# pop_list = list.pop(4)
# print(pop_list)
# print(list)

# task_5

# Write a Python script that concatenates two lists and prints the result.

# list_1 = [1,2,3]
# list_2 = [4,5,6]
# print(list_1 +list_2)

# task_6

# Write a Python script that repeats a list three times and prints the result.

# list_1 = [1,2,3]
# print(3*list_1)

# task_7

# Write a Python script that removes the elements at even indices from a list.

# list = [1,2,3,4,5,6,7,8,9]
# print(list[::2])

# task_8

# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
# a list

# list = ["santosh","ashok","nagaprasad","rajasekhar"]
# inserted_1 = list.insert(0,10)
# inserted_2 = list.insert(0,11)
# inserted_3 = list.insert(0,12)
# print(list)


# task_9

# suare Numbers Create a list of squares of numbers from 1 to 10.

# empty_list = []
# for i in range(1,11):
#     empty_list.append(i**2)
# print(empty_list)
# comprehensive method

# print([i**2 for i in range (1,11)])

# task_10

# cerate a list of even numbers from 1 to 20.

# even_numbers = [num for num in range(1, 21) if num % 2 == 0]
# print(even_numbers)

# print a list of words, create a list containing the lengths of
# each word.
# words = ["apple", "banana", "cherry", "date"]

# task_11


# words = ["apple", "banana", "cherry", "date"]
# lenght_of_words = [len(words) for word in words]
# print(words)
# print(lenght_of_words)