import random

print("Welcome Secret Code Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

q_letters = int(input("How many letters? "))
q_numbers = int(input("How many numbers? "))
q_symbols = int(input("How many special symbols? "))

password_list = []
for char in range(q_letters):
    letters1 = random.choice(letters)
    password_list.append(letters1)

for char in range(q_numbers):
    numbers1 = random.choice(numbers)
    password_list.append(numbers1)

for char in range(q_symbols):
    symbols1 = random.choice(symbols)
    password_list.append(symbols1)

password_list.append(random.choice(letters))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

final_password = "#" + password

print(f"Your password is: {final_password}")