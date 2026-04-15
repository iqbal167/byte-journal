
is_pass = True

if is_pass:
    print("Pass")
else:
    print("Fail")
        
grade = 90

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")




# One-line if statement
# if grade >= 90: print("Passed")
# else: print("Failed")

# Ternary Operator
print("Ternary Operator:")
message = "Passed" if grade >= 65 else "Failed"
print(message)
