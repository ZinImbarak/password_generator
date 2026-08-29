print("🔐 PASSWORD GENERATOR 🔐")

import string
import random

while True:
    characters = string.ascii_letters

    try:
        length = int(input("How long should your password be? "))
    except ValueError:
        print("Please enter a number!")
        continue

    if length <= 0:
        print("Please enter a positive number!")
        continue

    while True:
        numbers = input("Include numbers? ").lower()

        if numbers == "yes" or numbers == "no":
            break

        print("Please answer yes or no!")

    if numbers == "yes":
        characters += string.digits

    while True:
        symbols = input("Include symbols? ").lower()

        if symbols == "yes" or symbols == "no":
            break

        print("Please answer yes or no!")

    if symbols == "yes":
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("--------------------")
    print("Your password is:", password)
    print("--------------------")

    again = input("Do you want another password? ").lower()

    if again == "no":
        print("Goodbye! 👋")
        break