name = input("Enter your name please\n")
age = input("Enter your age please\n")

email = f"{name}{age}@itea.ua"


try:
   name / "SOMETEXT"
   surname = "NOOB"
   print(surname)
except Exception as e:
    surname = "Kozlov"
print("\nDeveloping with Python\n")

if surname == "NOOB":
    print("Tu dopustil ohubku")
else:
    print("Molodec")


