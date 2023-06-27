def add(n1, n2):
  return n1 + n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def division(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": division
  
}
def calculator():
  num1 = float(input("what's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    
    operation_symbol = input("pick an operation: ")
    num2 = float(input("what's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' ro continue calculating with {answer}, or type 'n' to start new calculation:")== "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
calculator()
