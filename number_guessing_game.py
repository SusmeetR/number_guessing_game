import random
mynum = random.randint(0,10)

print("I have a number in my mind. Can you guess it?")

while True:
    usernum = int(input("Enter your guess:"))

    if (mynum > usernum):
        print("Nope, increase your guess")

    elif ( mynum < usernum):
        print("Nope, decrease your guess")

    else:
        print("Hurray! You guessed it right.")
        break