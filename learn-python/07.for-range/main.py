"""
For-range is a loop statement that repeats a block of code a specified number of times.
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default).
"""

print("for-range:")
for i in range(5):
    print(i)

print("range:")
r = range(5)
print(r)
print(list(r))

print("for-range with list index:")
nums = [1, 2, 3, 4, 5]
for num in range(len(nums)):
    print(nums[num])

print("for-range with start and end:")
for i in range(1, 3):
    print(i)

print("for-range with step and end:")
for i in range(1, 10, 2):
    print(i)

print("for-range with list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

print("for-range with string:")
for char in "hello":
    print(char)

print("for-range with dictionary:")
profile = {"name": "Iqbal", "score": 80, "is_pass": True}
for key in profile:
    print(key, profile[key])

print("Nested for-range:")
max = 5
for i in range(max):
    for j in range(0, max - i):
        print("*", end="-") # end="" is default, "
    print()