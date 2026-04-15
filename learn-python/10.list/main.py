
py_list = [1, "Iqbal", True, 9.5, None]

empty_list = []

print("List elements:")
for e in py_list:
    print(e)

print("List elements (using index):")
for e in range(len(py_list)):
    print(py_list[e])


status_list = ["active", "inactive", "suspended"]

print("Enumerate function:")
for k, v in enumerate(status_list):
    print(f"{k}: {v}")

matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

print("Matrix:")
for row in matrix:
    for cel in row:
        print(cel, end=" ")
    print()


print("Convert range to list:")
range_of_num = range(10)
list_of_num = list(range_of_num)
print(list_of_num)

print("Access list elements:")
print(list_of_num[0])
print(list_of_num[3])

print("Access list elements (using slice):")
print(list_of_num[0:5])

print("Check if a number is in the list:")
x = 5
is_exist = True if x in list_of_num else False
print(is_exist)

print("Add elements to the list with append method:")
list_of_num.append(10)
print(list_of_num)

print("Add elements to the list with slice method:")
print(list_of_num)
list_of_num[len(list_of_num):] = [11, 12]
print(list_of_num)

print("Add elements to the list with insert method:")
list_of_num.insert(len(list_of_num),  13)
print(list_of_num)

print("Modify list elements:")
list_of_num[0] = 14
print(list_of_num)


list_1 = [1, 2]
list_2 = [3, 4]

print("Concatenate two lists: with + operator")
list_3 = list_1 + list_2 # Need to create a new list
print(list_3)

list_1 = [1, 2]
list_2 = [3, 4]

print("Concatenate two lists: with extend method")
list_1.extend(list_2)
print(list_1)

list_1 = [1, 2]
list_2 = [3, 4]

print("Concatenate two lists: with slice method")
list_1[len(list_1):] = list_2
print(list_1)


print("Remove elements from the list:")
my_list = [1, 2, 3, 4, 5]
my_list.remove(1)
print(my_list)

my_list = [1, 2, 3, 4, 5]
print("Remove elements from the list with pop method:")
my_list.pop(0)
print(my_list)

print("Remove elements from the list with del statement:")
my_list = [1, 2, 3, 4, 5]
del my_list[0]
print(my_list)

print("Remove elements from the list with del statement (using slice):")
my_list = [1, 2, 3, 4, 5]
del my_list[0:3]
print(my_list)

my_list = [1, 2, 3, 4, 5, 1, 1]
print("Length of the list:")
print(len(my_list))

print("Count elements in the list:")
print(my_list.count(1))

names = ["Iqbal", "Ali", "Zkh"]
idx = names.index("Ali")
print(idx)

print("Clear the list:")
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

print("Clear the list with assignment operator:")
my_list = [1, 2, 3, 4, 5]
my_list = []
print(my_list)

print("Clear the list with del statement:")
my_list = [1, 2, 3, 4, 5]
del my_list[:]
print(my_list)

print("Reverse the list:")
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

print("Copy the list with copy method:") 
print("Deep copy:") # Deep copy is used to create a new list and copy the elements from the original list to the new list
print("Using copy method to copy the list will create a new reference to the original list.")
my_list = [1, 2, 3, 4, 5]
num = my_list.copy()
print(num)

print("Copy the list with slice operator:")
print("Shallow copy:") # Shallow copy is used to create a new list and assign the reference of the original list to the new list
print("Using slice operator to copy the list will not create the same reference as the original list.")
my_list = [1, 2, 3, 4, 5]
num = my_list[:]
print(num)
print(my_list)

print("Sort the list:")
my_list = [1, 4, 3, 2, 5]
my_list.sort()
print(my_list)