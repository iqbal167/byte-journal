# '=' is assignment operator
# Naming Convention: https://peps.python.org/pep-0008/

name = 'Iqbal'
score = 90
is_pass = True

#  Legacy Style
print("Legacy Style:")
print("Name: %s, Score: %d, Is Pass: %s" % (name, score, is_pass))

# f-string Style
print("f-string Style:")
print(f"Name: {name}, Score: {score}, Is Pass: {is_pass}")

print("Declare variable with data type:")
name: str = 'Iqbal'
score: int = 90
is_pass: bool = True

print(f"Name: {name}, Score: {score}, Is Pass: {is_pass}")

print("Multiple Assignment:")
name, score, is_pass = 'Iqbal', 90, True
print(f"Name: {name}, Score: {score}, Is Pass: {is_pass}")