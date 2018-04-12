import re

my_name = "vladimir dovgopol"
my_name_list = my_name.split(" ")
print(f'{my_name_list[0].capitalize()} {my_name_list[1].capitalize()}')
print(my_name.title())
print(my_name[::-1])

number = "+380977279286"
phone_reg = re.match(r'(^\+[0-9]{12})', number)
while True:

    if phone_reg:
        print("Cool")


#while True
#   phone_numb = input("Enter your phone number: ")
