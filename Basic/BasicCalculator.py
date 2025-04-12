
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

op = input('Enter the operator (+, -, *, /): ')

if op == '+':
  print('The addition is', num1 + num2)
elif op == '-':
  print('The subtraction', num1 - num2)
elif op == '*':
  print('The Multiplaction is', num1 * num2)
elif op == '/':
  if num2 == 0:
    print('Error: Division by zero is not allowed.')
  else:
    print('The Division is',num1 / num2)
else:
  print('Invalid operator. Please use +, -, *, or /.')


# This is a simple calculator program that takes two numbers and an operator as input from the user.


