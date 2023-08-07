"""
David Wang
420-LCU-sec. 3
W2023
Prof. Jason Gullifer
Assignment #1, no 2
"""

print('think of a number from 1 to 1024, ill try to guess')
high = 1024 
low = 1
#Only thing changed is the bounds. Highest possible value is now 1024.
inp=''
guess = (high+low)//2
print("is it ", guess, "?")
# We define our initial guess which is outside of the loop.
# We also define our future guesses with the variable.
# This is done since, if we included this initial guess inside of the loop, we would be repeating this assignment of our guess variable.
while inp!='c':
# Our stopping condition.
  inp=input('type l if the guess is low, h if too high, and c if im right: ')
  if inp=='h':
    high = (high+low)//2 
    # The high bound is thus the result of bisection.
    guess = (high+low)//2
    # Our guess is a bisection.
    # Our divisons need to round down for 1 to be a possible answer.
    print("is it ", guess, "?")
  if inp=='l':
    low = round((high+low)/2)
    # The low bound is the result of the bisection.
    guess = round((high+low)/2)
    # Our guess is a bisection.
    # Our divisions need to round up for 1024 to be a possible answer.
    print("is it ", guess, "?")

print(f"got it, your number is {guess}")

