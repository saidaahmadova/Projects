import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_symbols = int(input("How many symbols would you like? "))

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your generated password is: {password}")