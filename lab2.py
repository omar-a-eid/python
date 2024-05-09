# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.
'''
def remove_adjacent(lst):
  new_lst = []
  for i, item in enumerate(lst):
    if i == 0 or item != lst[i - 1]:
      new_lst.append(item)
  return new_lst

lst = [1, 2, 3, 3]
print(remove_adjacent(lst))
'''

# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)
'''
def split_half(s):
  half_length = len(s) // 2
  return s[:half_length], s[half_length:]

def split_string(a, b):
  a_front, a_back = split_half(a)
  b_front, b_back = split_half(b)

  return a_front + b_front + " " + a_back + b_back

a = "abced"
b = "abcd"
print(split_string(a, b))
'''


# 3- Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
'''
def is_unique(lst):
  for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
      if lst[i] == lst[j]:
        return False
  return True

lst = [1, 2, 3, 4, 4]
print(is_unique(lst))
'''

# 4- Given unordered list, sort it using algorithm bubble sort
'''
def bubble_sort(lst):
  for i in range(len(lst)):
    for j in range(len(lst) - 1):
      if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
  return lst

lst = [9, 5, 6, 2, 1, 3, 4, 7, 8]
print(bubble_sort(lst))
'''

# 5- Gusses game
# ● Your game generates a random number and gives only 10 tries for the user to
# guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of
# the random number
# ● If the user type number is out of range(100), display a message that is not allowed
# and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and
# don’t count this as try
# ● In case the user entered a correct number within the 10 tries, display a
# congratulations message and let your application guess another random number with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play again or not
'''
import random
def guess_game():
  random_number = random.randint(1, 100)
  tries = 10
  guessed_numbers = set()

  while tries > 0:
    try:
      user_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if user_guess < 1 or user_guess > 100:
      print("Number out of range. Please try again.")
      continue

    if user_guess in guessed_numbers:
      print("You already guessed that number. Try again.")
      continue

    guessed_numbers.add(user_guess)
    tries -= 1

    if user_guess == random_number:
      print("Congratulations! You guessed the number in", 10 - tries, "tries!")
      if input("Play again? (y/n): ").lower() == "y":
        guess_game()  # Start a new game
      else:
        print("Thanks for playing!")
        break  # Exit the game
    elif user_guess < random_number:
      print("Too low. Try again.")
    else:
      print("Too high. Try again.")

  if tries == 0:
    print("You ran out of tries. The number was", random_number)
    if input("Play again? (y/n): ").lower() == "y":
      guess_game()  # Start a new game
    else:
      print("Thanks for playing!")

guess_game()
'''