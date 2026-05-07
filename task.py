
print("Welcome to the pizaa calculator")
size = input("What size do you have? S, M, L?")
toppings = int(input("How many toppings do you have?"))
delivery = input("Do you want delivery? Yes or No?")

bill = 0
if size == "S":
    bill = 10
elif size == "M":
    bill = 15
elif size == "L":
    bill = 20

bill += toppings * 2

if delivery == "Yes":
    bill += 5

print(f"Your final bill is ${bill}")