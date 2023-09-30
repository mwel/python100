# this little program will determine, whether a given number is even or odd and tell the user.

number = int(input("Enter a number to determine, whether it is even or odd."))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")