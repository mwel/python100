# Caesar cipher

from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers_specials = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~', '|', '\\', '/', ':', ';', ' '
]


def caesar(text, shift, direction):
    def shift_character(char, alphabet, shift, direction):
        if char in alphabet:
            alphabet_index = alphabet.index(char)
            if direction == "encode":
                shifted_index = (alphabet_index + shift) % len(alphabet)
            elif direction == "decode":
                shifted_index = (alphabet_index - shift) % len(alphabet)
            return alphabet[shifted_index]
        return char

    shifted_text = []

    for char in text:
        if char.isalpha():
            shifted_text.append(shift_character(char, alphabet, shift, direction))
        elif char in numbers_specials:
            shifted_text.append(shift_character(char, numbers_specials, shift, direction))
        else:
            shifted_text.append(char)

    encrypted_text = ''.join(shifted_text)
    print(f"Result: {encrypted_text}")


# LAUNCH
print(logo)


# CALL

while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt or 'N' to exit:\n")

    if direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        print ("Would you like to continue? Y/N ")

    elif(direction == "N"):
        print("Ok, thank you for using caesar cipher. Good bye.")
        quit()

    else:
        print("Invalid command.")

