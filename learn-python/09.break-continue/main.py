
num = 3
should_continue = True
while should_continue: 
    if num % 3 != 0:
        break # break intend to exit the loop

    print(f"{num} is divisible by 3")
    should_continue = False


#  Break loop is used to force exit the loop when the condition is met
print("Break loop")
for i in range(10):
    if i == 3:
        break
    print(i)

#  Continue loop is used to skip the current iteration of the loop and continue with the next iteration
print("Continue loop")
for i in range(10):
    if i == 3:
        continue
    print(i)