def card_num_check():
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

    return   card_num