import random
playing = True
number=str(random.randint(0, 9))
print("I am generating a number. Please guess the number between 0 and 9")
while playing:
    guess=input("Enter a number")
    if number==guess:
        print("Your guess is correct. You win the game.")
        print("the number was:", guess)
        break
    else:
        print("Try again.")
        