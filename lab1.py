# 1- Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
'''
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

print(lname, fname)
'''

# 2- Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''
n = input("Enter a number: ")
result = int(n) + int(n * 2) + int(n * 3)

print(result)
'''

# 3- Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
'''
str = """Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""
print(str)
'''

# 4- Write a Python program to get the volume of a sphere with radius 6
'''
r = int(input("Enter the radius of the sphere: "))
volume = 4/3 * 3.14 * r**3
print(volume)
'''

# 5-  Write a Python program that will accept the base and height of a triangle and compute the area.
'''
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(area)
'''

# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
'''
rows = int(input("Enter the number of rows: "))
for i in range(rows):
  for j in range(i + 1):
    print("*", end=" ")
  print()

for i in range(rows - 1, 0, -1):
  for j in range(i):
    print("*", end=" ")
  print()
'''

# 7- Write a Python program that accepts a word from the user and reverse it.
'''
word = input("Enter a word: ")
print(word[::-1])
'''

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
for i in range(7):
  if i == 3 or i == 6:
    continue
  print(i)
'''

# 9- Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
'''
def fibonacci(n):
  if n < 0:
    print("Incorrect input")
  # First Fibonacci number is 0
  elif n == 0:
    return 0
  # Second Fibonacci number is 1
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter length of series: "))
for i in range(n):
  print(fibonacci(i))
'''

# 10- Write a Python program that accepts a string and calculate the number of digits and letters.
'''
str = input("Enter a string: ")
letters = digits = 0
for i in str:
  if i.isdigit():
    digits += 1
  elif i.isalpha():
    letters += 1
  else:
    pass
print("Letters", letters)
print("Digits", digits)
'''