#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

elements = []

# choose random letters
print (f"Letters: {nr_letters}")
for l in range(0, nr_letters):
    letter = letters[random.randint(0, len(letters)-1)]
    elements.append(letter)

# choose random symbols
print (f"Symbols: {nr_symbols}")
for s in range(0, nr_symbols):
    symbol = symbols[random.randint(0, len(symbols)-1)]
    elements.append(symbol)

# choose random numbers
print (f"Numbers: {nr_numbers}")
for n in range(0, nr_numbers):
    number = numbers[random.randint(0, len(numbers)-1)]
    elements.append(number)

print (f"Elements: {elements}")

random.shuffle(elements)

password = ''.join(elements)

print (password)

