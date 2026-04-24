# Calculator Class (OOP implementation)

class Calculator:
  def __init__(self, a=0, b=0):
    self.a = a
    self.b = b

  # Method 1: Basic operations
  def calculate(self, operator):
    if operator == '+':
        return self.a + self.b
    elif operator == '-':
        return self.a - self.b
    elif operator == '*':
        return self.a * self.b
    elif operator == '/':
        return self.a / self.b
    elif operator == '%':
        return self.a % self.b
    else:
        return "Invalid operator"

  # Method 2: Factorial
  def factorial(self, n):
    if n == 0 or n == 1:
        return 1
    return n * self.factorial(n - 1)

  # Method 3: Complex operations
  def add_complex(self, a, b):
    return complex(a) + complex(b)

  def multiply_complex(self, a, b):
    return complex(a) * complex(b)


# Function 1: Handle user input
def get_numbers():
  a = float(input("Enter first number: "))
  b = float(input("Enter second number: "))
  return a, b


# Function 2: Main program controller
def main():
  choice = input("Enter operation (+, -, *, /, %, !): ")

  calc = Calculator()

  if choice == '!':
    num = int(input("Enter number: "))
    print("Factorial:", calc.factorial(num))

  else:
    a, b = get_numbers()
    calc = Calculator(a, b)
    print("Result:", calc.calculate(choice))

  print("\nComplex Operations:")
  print("Add Complex:", calc.add_complex(2+3j, 1+4j))
  print("Multiply Complex:", calc.multiply_complex(2+3j, 1+4j))


# Run program
main()