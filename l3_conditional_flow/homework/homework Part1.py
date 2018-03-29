#Var examples
integer_var = input("Enter number: ")

try:
    print(int(integer_var))
except ValueError:
    print("It isn't number: ")

float_var = input("Enter mumber: ")
try:
    print(float(integer_var))
except ValueError:
    print("It isn't number: ")

if integer_var > float_var:
    print("First number greater than second")
else:
    print("Second number greater than first")


char_var = input("Enter some text:")
print(char_var)

bull_var = bool(input("Enter something: "))
print(bull_var)


