import random

#code for random number game
def game():
    print("I am thinking of a number between 1 and 20")
    secretNumber = random.randint(1,20)

    for guessesTaken in range(1,7):
        print ("Take a guess.")
        guess = int(input())

        if guess < secretNumber:
            print ("Your guess is too low.")
        elif guess > secretNumber:
            print("Your guess is too high.")
        else:
            break #This condition is for the correct guess

    if guess == secretNumber:
        print("Good job, " + name + "!  You guessed my number in " + str(guessesTaken) + " guesses.")
    else:
        print ('Nope. The number I was thinking of was ' + str(secretNumber))

        

print ("Hello, what is your name?")
name = input()

print("Hello, " + name + ". What is your favorite food?")
food = input()
if food == "pizza":
    print("Mine too!")
else:
    print("I don't like " + food + ". My favorite food is pizza!")

print("What is your favorite color?")
color = input()
if color == "red":
    print("Mine too!")
else:
    print ("My favorite color is red")

print("What is your favorite drink?")
drink = input()
if drink == "sweet tea":
    print("Mine too!")
else:
    print ("My favorite drink is sweet tea")

print("Want to play a game?")
answer = input()
while answer not in ["yes", "no"]:
    print("yes or no?")
    continue

if answer == "no":
    print("Ok")
if answer == "yes":
     game()



print("Goodbye, " + name + "!")

