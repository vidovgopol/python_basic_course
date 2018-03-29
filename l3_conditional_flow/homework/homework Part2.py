print("Enter your credit card please:")

#Card number section
card_num = input("Enter credit card number:\n")

#Check for digit in card number
try:
    int(card_num)
except ValueError:
    print("Error card number contains digit")
    exit()

#Check for card number lenght
card_num_len = len(card_num)
if card_num_len != 16:
    print("Card number incorrect")
    exit()
else:
    pass

#Expiration date section
exp_date = input("Enter expiration date in format (dd/yy):\n")
try:
        int(exp_date)
        print("Expiration date incorect")
        exit()
except ValueError:
        print("Ok")


#CVV code section
cvv_code = input("Enter CVV code:\n")
cvv_code_len = len(cvv_code)

#Check for digit in CVV

try:
    int(cvv_code)
except ValueError:
    print("CVV code contains digit")
    exit()

#Check for CVV leght
if cvv_code_len < 3:
    print("CVV code incorrect")
else:
    print("Ha-ha-ha. Now I will use your credit card!")







