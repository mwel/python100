# a number of friends wants to give tips and share the bill equally. Ask and answer.

# how much was the bill?
bill = float(input("How much is the bill?"))
print(f"Ok. Your bill seems to be $ {bill} in total.")

# how many people are paying? 
people = int(input("How many people are paying?"))
print(f"Ok. Seems you are {people} people to share the bill.")

# how much tip do you give in total?
tip = int(input("How much would you like to tip? (in %)")) / 100

# whats the total amount?
bill += bill * tip
print (f"Ok. In total you will pay $ {bill}.")

# whats the amount per person?
per_person = (round((bill / people), 2))
print(f"Each of you ows $ {per_person}. Pay up!")





