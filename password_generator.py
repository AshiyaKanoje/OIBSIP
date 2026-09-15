"""Random Password Generator."""
import random
import string

print("----- Random Password Generator -----")

while True:
    # Ask for password length
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Password length should be at least 8.")
        continue

    # Choose character types
    upper = input("Include uppercase letters? (y/n): ")
    lower = input("Include lowercase letters? (y/n): ")
    numbers = input("Include numbers? (y/n): ")
    symbols = input("Include symbols? (y/n): ")

    characters = ""
    password = ""
    if upper == "y":
        characters = characters + string.ascii_uppercase
    if lower == "y":
        characters = characters + string.ascii_lowercase

    if numbers == "y":
        characters = characters + string.digits

    if symbols == "y":
        characters = characters + string.punctuation

    # Check if at least two types are selected
    selected = 0

    if upper == "y":
        selected += 1
    if lower == "y":
        selected += 1
    if numbers == "y":
        selected += 1
    if symbols == "y":
        selected += 1

    if selected < 2:
        print("Please select at least 2 character types.")
        continue

    # Generate password
    for i in range(length):
        password = password + random.choice(characters)

    print("\nYour password is:", password)

    # Generate another password
    again = input("\nDo you want another password? (y/n): ")

    if again != "y":
        print("Thank you for using the password generator!")
        break
    
