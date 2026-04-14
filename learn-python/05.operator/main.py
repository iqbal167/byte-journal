
# Arithmetic Operators
print("Arithmetic Operators:")
print("1 + 2 =", 1 + 2) # Addition
print("1 - 2 =", 1 - 2) # Subtraction
print("1 * 2 =", 1 * 2) # Multiplication
print("1 / 2 =", 1 / 2) # Division
print("1 // 2 =", 1 // 2) # Integer Division
print("1 ** 2 =", 1 ** 2) # Exponentiation
print("1 % 2 =", 1 % 2) # Modulus

# Unary Operators
print("Unary Operators:")
num1 = +2
print(num1)

# Unary Minus Operator
print("Unary Minus Operator:")
num2 = -2
print(num2)

# Assignment Operator
print("Assignment Operator:")
num3 = 2
print(num3)

# Compound Assignment Operator
print("Compound Assignment Operator:")
asg = 1
print("asg =", asg)
asg += 2
print("asg += 2 =", asg)
asg -= 2
print("asg -= 2 =", asg)
asg *= 2
print("asg *= 2 =", asg)
asg /= 2
print("asg /= 2 =", asg)
asg //= 2
print("asg //= 2 =", asg)
asg ** 2
print("asg ** 2 =", asg ** 2)
asg %= 2
print("asg %= 2 =", asg)

# Comparison Operator
print("Comparison Operator:")
print("1 == 2", 1 == 2)
print("1 != 2", 1 != 2)
print("1 < 2", 1 < 2)
print("1 > 2", 1 > 2)
print("1 <= 2", 1 <= 2)
print("1 >= 2", 1 >= 2)

# Logical Operator
print("Logical Operator:")
result1 = (1 == 2) and (2 > 1)
print("AND",result1)
print("1 & 2 =", 1 & 2)

result2 = (1 == 2) or (2 > 1)
print("OR",result2)
print("1 | 2 =", 1 | 2)

result3 = not (1 == 2)
print("NOT",result3)

# Bitwise Operator
print("Bitwise Operator")
num3 = 5
num4 = 6
print("5 AND 6 = ",num3 & num4) # 4 (1010 & 1100 = 1000)
print("5 OR 6 =",num3 | num4) # 7 (1010 | 1100 = 1111)
print("NOT 5 =",~num3) # -6 (11111010 = -6)
print("5 XOR 6 =",num3 ^ num4) # 3 (1010 ^ 1100 = 0011)
print("5 RIGHT 1 =",num3 >> 1) # 2 (1010 >> 1 = 010)
print("5 LEFT 1 =",num3 << 1) # 10 (1010 << 1 = 10100)

# Identity Operator
print("Identity Operator")
num5 = 10
num6 = 11
print("10 is 11", num5 is num6) # False
print("10 is not 11", num5 is not num6) # True
print(id(num5), id(num6))

print("Membership Operator")
list_of_num = [1, 2, 3, 4, 5]
print("1 in list_of_num", 1 in list_of_num) # True
print("6 in list_of_num", 6 in list_of_num) # False
print("1 not in list_of_num", 1 not in list_of_num) # False
print("6 not in list_of_num", 6 not in list_of_num) # True