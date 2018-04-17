name = input("Enter your name:\n")
surname = input("Enter your surname:\n")

my_text = f"""
Hi,

I am a Python developer and i want to work in a cool team.
I would like to get a chance to work in your company.
My work expirience isn't big enought, but I am an open minded persone and
ready to work hard.

Best regards,

{name} {surname}"""


my_file = open("first_file.txt", "r+")
my_file.write(my_text)

with open("first_file.txt", "r") as f:
    word = "work"
    word_found = False
    word_counter = 0
    for line in f:
        if word in line:
            word_counter = word_counter + 1
            word_found = True

if word_found:
    print(word_counter)

