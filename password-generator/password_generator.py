import random
import string

def generate_password(length):
    # Characters to use in password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


print("---- Auto Password Generator ----")

length = int(input("Enter password length: "))

password = generate_password(length)

print("Generated Password:", password)