import random

#Function determines whether password contains special chars
def has_special_chars(password, special_chars_list):
    has_special_chars = False
    for i in password:
        if i in special_chars_list:
            has_special_chars = True
    return has_special_chars    


#Function determines whether password contains a number
def has_num(password, digits_list):
    has_num = False
    for i in password:
        if i in digits_list:
            has_num = True
    return has_num


#Function determines whether password contains an uppercase letter
def has_upper(password, upper_case_list):
    has_upper = False
    for i in password:
        if i in upper_case_list:
            has_upper = True
    return has_upper


#Function determines whether password contains a lowercase letter
def has_lower(password, lower_case_list):
    has_lower = False
    for i in password:
        if i in lower_case_list:
            has_lower = True
    return has_lower   


def main():
    password_length = int(input("How long should the password be? \n"))
    special_input = int(input("Does the password require special characters? (@#$%=:?./|~>*()<) \nType 0 for no and 1 for yes \n"))
    while special_input != 0 and special_input != 1:  # ensures user inputs either a 0 or 1
        special_input = int(input("Invalid input! \nType 0 for no and 1 for yes \n"))
    special_chars = bool(special_input)
    password = ""

    lower_case_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_chars_list = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    #creates a list of all possible chars to iterate over
    if special_chars:
        chars_list = lower_case_list + upper_case_list + digits_list + special_chars_list
    else:
        chars_list = lower_case_list + upper_case_list + digits_list

    #main loop - generates the password from list of all possible chars
    for i in range(password_length):
        char_index = random.randint(0, len(chars_list)-1)
        char = chars_list[char_index]
        password += char

    #tests to determine whether password is strong
    has_special_char = has_special_chars(password, special_chars_list)
    
    has_digit = has_num(password, digits_list)

    has_upper_char = has_upper(password, upper_case_list)

    has_lower_char = has_lower(password, lower_case_list)
    
    char_to_replace = -1
    if special_chars and not has_special_char:
            char_index = random.randint(0, len(special_chars_list)-1)
            char = special_chars_list[char_index]
            password.replace(password[char_to_replace], char)
            char_to_replace -= 1
    
    viable = has_special_char and has_digit and has_upper_char and has_lower_char

    # loop ensures that password contains one of each type of char
    while not viable:
        if not has_num:
            char_index = random.randint(0, len(digits_list)-1)
            char = digits_list[char_index]
            password.replace(password[char_to_replace], char)      
        elif not has_upper:
            char_index = random.randint(0, len(upper_case_list)-1)
            char = digits_list[char_index]
            password.replace(password[char_to_replace], char)
        elif not has_lower:
            char_index = random.randint(0, len(lower_case_list)-1)
            char = digits_list[char_index]
            password.replace(password[char_to_replace], char)
        
        char_to_replace -= 1

        viable = has_num and has_upper and has_lower

    if viable and special_chars and has_special_char and len(password) >= 8:
        print(f"Your password is: {password} and it is strong.")
    else:
        print(f"Your password is {password}, but it is not very strong")
        if len(password) < 8 and not has_special_chars:
            print("Consider increasing the length of your password and adding special characters to make it stronger")
        elif len(password) < 8 and has_special_chars:
            print("Consider increasing the length of your password to make it stronger.")
        elif not has_special_chars:
            print("Consider adding special characters to make your password stronger")


main()
