import random

print("Welcome to the password generator!")

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

q_name = input("Your name: ")
q_animal = input("Your favorite animal: ")
q_numbers = int(input("How many random numbers? "))
q_symbols = int(input("How many symbols? "))

username = q_name + q_animal

for char in range(q_numbers):
    numbers1 = random.choice(numbers)
    username += numbers1

for char in range(q_symbols):
    symbols1 = random.choice(symbols)
    username += symbols1

print(f"Your password is: {username}")
