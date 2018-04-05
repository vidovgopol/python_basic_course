def cvv_code_check():
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
        else:
            print("CVV code incorrect")
    return cvv_code