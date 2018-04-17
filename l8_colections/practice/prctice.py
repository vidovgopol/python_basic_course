import random

companies = ('cisco', 'hp', 'dell', 'watchguard', 'checkpoint', 'fortigate')

email_list_1 = []
exit_var = 0
rand_index = 0
while exit_var != 50:
    rand_number = random.randint(1, 11)
    rand_index = random.randint(0, len(companies) - 1)
    email_curent = companies[rand_index] + str(rand_number) + "@" + companies[rand_index] + ".com"
    email_list_1.append(email_curent)
    exit_var = exit_var + 1


email_list_2 = []
exit_var = 0
rand_index = 0
while exit_var != 50:
    rand_number = random.randint(1, 30)
    rand_index = random.randint(0, len(companies) - 1)
    email_curent = companies[rand_index] + str(rand_number) + "@" + companies[rand_index] + ".com"
    email_list_2.append(email_curent)
    exit_var = exit_var + 1

print(email_list_1)
print("***********************")
print(email_list_2)

email_set_1 = set(email_list_1)
email_set_2 = set(email_list_2)

print("***********************")

print(email_set_1)
print("***********************")
print(email_set_2)


inter =  email_set_1.intersection(email_set_2)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
print(inter)
