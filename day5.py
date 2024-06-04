def divide_numbers(a, b):
  """Divides two numbers and handles division by zero error."""
  if b == 0:
    raise ValueError("Cannot divide by zero!")
  else:
    return a / b

try:
  result = divide_numbers(10, 0)
except ValueError as e:
  print(e)
else:
  print("The result is:", result)
