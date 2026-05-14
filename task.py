import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the password generator!")

q_letters = int(input("How many letters: "))
q_symbols = int(input("How many symbols: "))
q_numbers = int(input("How many numbers: "))
capital = input("Should password start with capital letter? Y or N: ").lower()

password_list = []

for char in range(q_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for char in range(q_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

for char in range(q_numbers):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

if capital == "Y":
    password_list[0] = password_list[0].upper()

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")

