"""
While is a loop statement that repeats a block of code while a condition condition is true.
The while loop is used when you do not know how many times you want to loop.
The while loop is used when you want to repeat a block of code until a condition is false.
"""

print("while:")
should_continue = True
score = 2

while should_continue:
    if score > 5:
        should_continue = False
        print("Loop is stopped.")
    else:
        score += 1
        print(f"Score is {score}.")

print("Nested While:")
n = 5
i = 0

while i < n:
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1

    print()
    i += 1
