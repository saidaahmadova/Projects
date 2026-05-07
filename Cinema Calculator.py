print("Welcome to the cinema calculator")
many = int(input("How mapy people?"))
time = input("Do you want after 6? Yes or No?")

bill = 0
if time == "Yes":
    bill += 10
if time == "No":
    bill += 5

popcorn = input("Will you have popcorn? Yes or No?")
total = 0
if popcorn =="Yes":
    size = input("What size: S,L?")
    if size == "S":
        total += 3
    if size == "L":
        total += 5

total_tickets_amount = many * bill
total_popcorn_amount = many * total

print(f"The total amount tickets for {many} people will be ${total_tickets_amount} and popcorn for {many} people will be {total_popcorn_amount}")
