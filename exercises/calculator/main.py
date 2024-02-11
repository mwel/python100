# simple arithmetic calculator

import calculator_logo

""" OPERATIONS """
# addition
def add (var1,var2):
    return var1 + var2

# subtraction
def sub (var1,var2):
    return var1 - var2

# multiplication
def mult (var1,var2):
  return var1 * var2

# division
def div (var1,var2):    
  return var1 / var2


""" OPERATORS"""
operators = {
   "+": add,
   "-": sub,
   "*": mult,
   "/": div
}

def loop(var1, operators):
   while True:
    # choose operation
    operator = input("Choose operator...")

    var2 = float(input("Input next variable... "))

    # determine operation
    operation = operators[operator]

    result = operation(var1,var2)
    
    print (f"Result: {var1} {operator} {var2} = {result}")
    var1 = result
    stop = input ("Stop? Y/N")
    if stop == "Y":
       return result



# main

print (calculator_logo.logo)
print ("CALCULATOR READY... ")

# print possible operations
print("The following operations are available:")
for symbol in operators:
  print (symbol)

var1 = float(input("Input starting variable..."))

result = loop(var1, operators)

print (f"Final result is {result}. Thanks for using this calculator.") 


