def exp_date_check():
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
    return exp_date