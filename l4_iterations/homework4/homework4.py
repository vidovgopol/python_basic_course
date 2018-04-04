while True:
    card_num = input("Please enter your credit card number in format xxxx xxxx xxxx xxxx:\n")
    card_num_list = card_num.split(' ')
    loop_exit_var = 0
    if len(card_num_list) == 4:
        for i in card_num_list:
            if len(i) == 4:
                try:
                    temp_var = int(i)
                    loop_exit_var += 1
                except:
                    print("credit card number incorrect")
                    break
            else:
                loop_exit_var = 0
                print("credit card number incorrect")
                break
    if loop_exit_var == 4:
        break


if card_num_list[0] == "5167":
    print("You use PrivateBank credit card\n")
elif card_num_list[0] == "5375":
    print("You use Monobank credit card\n")
else:
    print("You use credit card from unknown bank\n")

cur_year = 18
while True:
    exp_date = input("Please enter expiration date in format mm/yy:\n")
    exp_date_list = exp_date.split('/')
    loop_exit_var = 0
    for i in exp_date_list:
        if len(i) == 2 and len(exp_date_list) == 2:
            try:
                temp_var = int(i)
                if int(exp_date_list[0]) >= 1 and int(exp_date_list[0]) <= 12 and int(exp_date_list[1]) >= cur_year:
                    loop_exit_var = 1
            except:
                break
    if loop_exit_var == 1:
        break
    else:
        print("expiration date incorrect")

while True:
    cvv_code = input("Please enter your CVV code:\n")
    loop_exit_var = 0
    if len(cvv_code) == 3:
        try:
            temp_var = int(cvv_code)
            loop_exit_var = 1
        except:
            continue
    if loop_exit_var == 1:
        break

print(f"Credit card number is< {card_num} >")
print(f"Expiration date is < {exp_date} >")
print(f"CVV code is < {cvv_code} >")