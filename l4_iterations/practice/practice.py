favorite_nun = 3
low_digit_limit = 1
upper_digit_limit = 100
my_list = []

input_var = favorite_nun
while input_var != "3":
    input_var = input("Enter your number one more time")
    try:
        int_var = int(input_var)
        if int_var < 1:
            print("Your number less than 1")
        if int_var > 100:
            print("Your number greater than 100")
        my_list.append(int_var)
    except:
        print("You enter text")
        my_list.append(input_var)

my_str_list = [ s for s in my_list if type(s) == str ]
print(my_list)
print(my_str_list)
