import random
import time

print(""""************************************

Number Guessing Game


Guess a number between 1 and 50


**************************************

""")

random_number = random.randint(1,50)
guessing_attempt = 7
while True:

    attempt= int(input("Your guess: "))

    if (attempt < random_number):
        print("Checking information...")
        time.sleep(1)
        print("Guess a higher number...")
        guessing_attempt-=1
    elif (attempt > random_number):
        print("Checking information...")
        time.sleep(1)
        print("Guess a lower number...")
        guessing_attempt -= 1
    else:
        print("Checking information...")
        time.sleep(1)
        print("Congratulations, number is ",random_number)
        break
    if(guessing_attempt==0):
        print("Game Over...")
        print("Number is : ",random_number)
        break















