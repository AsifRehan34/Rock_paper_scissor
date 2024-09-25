#import random

guess= input("guess a number")
randomnumber = random.randint(1, 5)
number_guess=0

while(guess!=randomnumber):
    number_guess+=1
    guess=int(input("Guess a number: "))
print(f"it took you {number_guess} tries to guess the number right")

#testing for jenkins



