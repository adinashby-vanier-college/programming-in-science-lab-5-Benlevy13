# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
  if n == 1:
    return '*' 
  result = ""
  for i in range(n):
    result += "*"
  result += "\n"

  for i in range(n - 2):
    result += '*'
    for j in range( n - 2):
      result += " "
    result += '*\n'

  for i in range(n):
    result += "*"
  result += "\n"
  return result.strip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
  result = ""
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      result += str(j)
    result += "\n"
  return result.strip() 

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
  total = 0
  i = 1
  while i <= n:
    total += i
    i += 1
return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""