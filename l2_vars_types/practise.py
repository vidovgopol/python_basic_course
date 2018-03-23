print("Hi")

# List or spisok
my_guest = ["Alina", "Ruslan", "Tanya"]
type(my_guest)

#Dict
my_dict = {"1":"name", "2":"lastname"}
type(my_dict)

#Tuple
my_tuple = ("Tup1", "Tup2")
type(my_tuple)



name = "Vova"
last_name = "Dovgopol"

result = f"Your name is {name}, your last name is {last_name}" # P3.6

print(result)

result = "Your name is %s, your last name is %s" % (name, last_name)

print(result)

result = "Your name is {0}, your last name is {1}".format(name,last_name)

print(result)