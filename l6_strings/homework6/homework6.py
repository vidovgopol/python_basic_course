from function import check_credit_card
from function import check_exp_date
from function import check_cvv_code
from function import check_holder_name
from function import check_what_bank

while True:
    holder_name = input("Enter your Name Surname:\n")
    if check_holder_name(holder_name) == True:
        break

while True:
    card_num = input("Enter your card number in format 1111 1111 1111 1111:\n")
    if check_credit_card(card_num) == True:
        break

check_what_bank(card_num)

current_year = 18
while True:
    exp_date = input("Enter expiration date:\n")
    if check_exp_date(exp_date, current_year) == True:
        break


while True:
    cvv_code = input("Enter your CVV code:\n")
    if check_cvv_code(cvv_code) == True:
        break

print("Your credit card information:\n")
print(holder_name.upper())
print(card_num)
print(exp_date)
print(cvv_code)
