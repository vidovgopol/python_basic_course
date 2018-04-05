from function import cvv_code_check
from function import card_num_check
from function import exp_date_check


card_num = card_num_check()
exp_date = exp_date_check()
cvv_code = cvv_code_check()

print(card_num)
print(exp_date)
print(cvv_code)