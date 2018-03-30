card_num = True
while card_num == True:
    card_num = input("Please enter your credit card number in format xxxx xxxx xxxx xxxx:\n")
    card_num_list = card_num.split(' ')
    for i in card_num_list:
        if len(i) == 4 and len(card_num_list) == 4:
            try:
                temp_var = int(i)
            except:
                card_num = True
                print("credit card number incorrect")
                break
        else:
            card_num = True
            print("credit card number incorrect")
            break


if card_num_list[0] == "5167":
    print("You use PrivateBank credit card\n")
elif card_num_list[0] == "5375":
    print("You use Monobank credit card\n")
else:
    print("You use credit card from unknown bank\n")

exp_date = True
cur_year = 18
while exp_date == True:
    exp_date = input("Please enter expiration date in format mm/yy:\n")
    exp_date_list = exp_date.split('/')
    for i in exp_date_list:
        if len(i) == 2 and len(exp_date_list) == 2:
            try:
                temp_var = int(i)
                if int(exp_date_list[0]) < 1 or int(exp_date_list[0]) > 12 or int(exp_date_list[1]) < cur_year:
                    exp_date = True
                    print("Expiration date incorect")
                    break
            except:
                exp_date = True
                print("expiration date incorrect")
                break
        else:
            exp_date = True
            print("Expiration date incorect")
            break

cvv_code = True
while cvv_code == True:
    cvv_code = input("Please enter your CVV code:\n")
    if len(cvv_code) == 3:
        try:
            temp_var = int(cvv_code)
        except:
            cvv_code = True
    else:
        cvv_code = True

print(f"Credit card number is< {card_num} >")
print(f"Expiration date is < {exp_date} >")
print(f"CVV code is < {cvv_code} >")

