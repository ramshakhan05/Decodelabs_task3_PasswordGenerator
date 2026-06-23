import secrets
import string

print("===== Password Generator =====")

try:
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits

    password = ''.join(secrets.choice(characters) for i in range(length))

    print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")
