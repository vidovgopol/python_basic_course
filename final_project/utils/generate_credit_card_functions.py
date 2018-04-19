import random
import string

# Name generator


def rand_name_fun():
    first_name_coll = ["Ivan", "Nataliya", "Denis", "Ruslan", "Viktoriya", "Artem", "Vladislav"]
    last_name_coll = ["Kuzmenko", "Bondarenko", "Ivanenko", "Radchenko", "Stepanenko", "Skripko", "Samko"]

    rand_fist_name_index = random.randint(0, len(first_name_coll) - 1)
    rand_last_name_index = random.randint(0, len(last_name_coll) - 1)
    rand_name = first_name_coll[rand_fist_name_index] + " " + last_name_coll[rand_last_name_index]
    return rand_name

# Phone generator


def rand_phone_fun():
    rand_character = string.ascii_letters + "[" + "-" + "]"
    rand_phone = "+380"
    while True:
        rand_phone = rand_phone + str(random.randint(0, 9))
        if len(rand_phone) == 13:
            break
    chance = random.randint(1, 50)
    if chance == 1:
        rand_phone = list(rand_phone)
        rand_phone[random.randint(1, 11)] = random.choice(rand_character)
        rand_phone = "".join(rand_phone)
        return rand_phone
    else:
        return rand_phone


# Expiration date generator


def rand_exp_date_fun():
    rand_month = str(random.randint(1, 12))
    rand_year = str(random.randint(18, 30))
    if len(rand_month) < 2:
        rand_exp_date = "0" + str(rand_month) + "/" + str(rand_year)
    else:
        rand_exp_date = str(rand_month) + "/" + str(rand_year)
    return rand_exp_date

# Card number generator


def rand_card_number_fun():
    rand_card_number = ""
    rand_character = string.ascii_letters + "[" + "-" + "]"
    while True:
        if len(rand_card_number) == 4 or len(rand_card_number) == 9 or len(rand_card_number) == 14:
            rand_card_number = rand_card_number + " "
        else:
            rand_card_number = rand_card_number + str(random.randint(0, 9))
        if len(rand_card_number) == 19:
            break
        chance = random.randint(1, 100)
    if chance == 1:
        rand_card_number = list(rand_card_number)
        rand_card_number[random.randint(0, 18)] = random.choice(rand_character)
        rand_card_number = "".join(rand_card_number)
        return rand_card_number
    else:
        return rand_card_number


def card_holders_generation():
    card_holders_list = []
    exit_var = 0
    while True:
        rand_name = rand_name_fun()
        rand_phone = rand_phone_fun()
        rand_exp_date = rand_exp_date_fun()
        rand_card_number = rand_card_number_fun()
        card_holder_dict = {"Name": rand_name, "Phone": rand_phone, "Exp_day": rand_exp_date, "Card": rand_card_number}
        card_holders_list.append(card_holder_dict)
        exit_var = exit_var + 1
        if exit_var == 100:
            break
    return card_holders_list
