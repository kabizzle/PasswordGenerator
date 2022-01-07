#I wrote this program to automate the process of creating lists of characters for passwordGenerator.py

char_str = "abcdefghijklmnopqrstuvwxyz"
lower_char_list = []
for i in char_str:
    lower_char_list.append(i)
print(lower_char_list)

upper_char_list = []
for i in char_str:
    upper_char_list.append(i.upper())
print(upper_char_list)

digit_str = "0123456789"
digit_list = []
for i in digit_str:
    digit_list.append(i)
print(digit_list)

special_chars = "@#$%=:?./|~>*()<"
special_chars_list = []
for i in special_chars:
    special_chars_list.append(i)
print(special_chars_list)
