
def calculateNum(a , b, operator):
  # TO add
  if operator == '+':
    return a+b
  # TO subtract
  elif operator == '-':
    return a-b
  # To Multiply
  elif operator == '*':
    return a*b
  # To Divide
  elif operator == '/':
    return a/b
  # To Find remainder
  elif operator == '%':
    return a%b
  
# For FActorial
def factorial(n):

  if n == 0 or n == 1:
    return 1
  
  return n * factorial(n - 1)




# Complex Number Operations


def add_complex(a, b):
  return complex(a) + complex(b)

def multiply_complex(a, b):
  return complex(a) * complex(b)


# Main Function

def main():

  choice = input("Enter operation (+, -, *, /, %, !): ")

  # CHOICE FOR FACTORIALS
  if choice == '!':

    num = int(input("Enter number: "))

    print(factorial(num))

  else:

    a = float(input("Enter first number: "))

    b = float(input("Enter second number: "))

    print(calculateNum(a, b, choice))

  print("\nComplex Operations:")
  print("Add Complex:", add_complex(2+3j, 1+4j))
  print("Multiply Complex:", multiply_complex(2+3j, 1+4j))


# print(round(43.6))

main()
