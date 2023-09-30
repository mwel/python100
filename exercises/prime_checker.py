#Write your code below this line 👇

import math

def prime_checker (number):
    divisor = math.ceil(number / 2)
    while divisor >= 2:
        remainder = number % divisor
        print(f"{number} % {divisor} = {remainder}")
        if remainder == 0:
            print(f"NOT PRIME")
            return False
        else:
            divisor -= 1
            
    print(f"LIKELY PRIME ;)")
    return True
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
