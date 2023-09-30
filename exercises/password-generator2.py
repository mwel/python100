import random
import string

def generate_password(length, num_symbols, num_numbers):
    # Define character sets
    letters = string.ascii_letters
    symbols = '!#$%&()*+'
    numbers = string.digits

    # Check if the requested length is too short
    if length < num_symbols + num_numbers:
        print("Password length is too short to accommodate the requested symbols and numbers.")
        return None

    # Generate password elements
    password_elements = random.choices(letters, k=length - num_symbols - num_numbers)
    password_elements += random.choices(symbols, k=num_symbols)
    password_elements += random.choices(numbers, k=num_numbers)

    # Shuffle the elements to create randomness
    random.shuffle(password_elements)

    # Create the password by joining the elements
    password = ''.join(password_elements)

    return password

print("Welcome to the PyPassword Generator!")

while True:
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
        
        password = generate_password(nr_letters, nr_symbols, nr_numbers)
        
        if password:
            print("Generated Password:", password)
            break
    except ValueError:
        print("Invalid input. Please enter valid numbers for password length and quantities of symbols and numbers.")