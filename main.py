import random
number = random.randint(1, 10000)
Guess = int(input("Guess the number! "))
while Guess != number:
  if Guess < number:
    Guess = int(input("Guess the number! "))
    print("Higher")
  if Guess > number:
    print("Lower")