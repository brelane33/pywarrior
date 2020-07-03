import random

name = input("Enter your name: ")
print(f'Hello, {name}!')

def guessing():
  number = random.randint(0, 100)
  while True:
    user_guess = int(input("What number was chosen?  "))
    if (number < user_guess):
      print(f'Guess was too high.')
    if (number > user_guess):
      print(f'Guess was too low.')
    if (number == user_guess):
      print(f'Guess was correct!.')
      break 
 

guessing() 
