from utils import card_holders_generation
from utils import check_credit_card
from utils import check_holder_name
from utils import check_exp_date
from utils import check_phone_number


card_holders_coll = card_holders_generation()
print(card_holders_coll)
current_year = 18
for el in card_holders_coll:
    card_holder_name_correct = check_holder_name(el['Name'])
    card_phone_correct = check_phone_number(el['Phone'])
    card_exp_date_correct = check_exp_date(el['Exp_day'], current_year)
    card_number_correct = check_credit_card(el['Card'])
    if card_phone_correct and card_number_correct:
        print("Ok")
    else:
        print("Bad")
