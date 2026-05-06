def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("Welcome to Advanced Calculator!")

continue_calculating = True

num1 = float(input("Enter first number: "))

while continue_calculating:

    print("\nOperations:")
    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter next number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(
        f"Type 'y' to continue calculating with {answer}, "
        f"or type 'n' to start a new calculation: ").lower()

    if choice == "y":
        num1 = answer
    else:
        continue_calculating = False
        print("Calculator closed.")