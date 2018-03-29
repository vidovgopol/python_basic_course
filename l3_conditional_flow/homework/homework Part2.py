print("Enter your credit card please:")
card_num = input("Enter credit card number: ")
card_num_len = len(card_num)
if card_num_len != 16:
    exit()
else:
    exp_date = input("Enter expiration date in format (dd/yy):")
    try:
        int(exp_date)
        exit()
    except ValueError:
        print("Ok")

cvv_code = input("Enter CVV code: ")
cvv_code_len = len(cvv_code)
if cvv_code_len < 3:
    print("CVV code incorrect")
else:
    print("Ha-ha-ha. Now I will use your credit card!")







