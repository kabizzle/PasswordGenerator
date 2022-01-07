import random

def passwordGen():
    password_length = int(input("How long should the password be? \n"))
    special_input = int(input("Does the password require special characters? (@#$%=:?./|~>*()<) \nType 0 for no and 1 for yes \n"))
    while special_input != 0 and special_input != 1:
        special_input = int(input("Invalid input! \nType 0 for no and 1 for yes \n"))
    special_chars = bool(special_input)
    password = ""

    lower_case_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_chars_list = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    if special_chars:
        chars_list = lower_case_list + upper_case_list + digits_list + special_chars_list
    else:
        chars_list = lower_case_list + upper_case_list + digits_list

    for i in range(password_length):
        char_index = random.randint(0, len(chars_list)-1)
        char = chars_list[char_index]
        password += char

    for i in password:
        if i in special_chars_list:
            has_special_chars = True
    else:
        has_special_chars = False

    if special_chars and not has_special_chars:
        char_index = random.randint(0, len(special_chars_list)-1)
        char = special_chars_list[char_index]
        password.replace(password[-1], char)

    if has_special_chars and len(password) >= 8:
        print(f"Your password is: {password} and it is strong.")
    else:
        print(f"Your password is {password}, but it is not very strong")
        if len(password) < 8 and not has_special_chars:
            print("Consider increasing the length of your password and adding special characters to make it stronger")
        elif len(password) < 8 and has_special_chars:
            print("Consider increasing the length of your password to make it stronger.")
        elif not has_special_chars:
            print("Consider adding special characters to make your password stronger")


passwordGen()
