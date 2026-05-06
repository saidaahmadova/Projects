alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_cipher(text, shift, direction):
    result = ""

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += char

    print(f"The {direction}d message is: {result}")


print("Welcome to Caesar Cipher!")

restart = "yes"

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar_cipher(text, shift, direction)

    restart = input("Do you want to go again? Type 'yes' or 'no': ").lower()

print("Goodbye!")