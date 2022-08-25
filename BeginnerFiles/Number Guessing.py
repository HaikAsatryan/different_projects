import random
print("Welcome to number guessing game created by Haik")
while True:
    UserRange = input("Please type a number: ")
    if UserRange.isdigit():
        UserRange = int(UserRange)
        if UserRange <= 1:
            print("Please type a number above 1")
            continue
        else:
            break
    else:
        print("You typed not a number, please type a number this time")
        continue
GuessNumber = random.randint(0,UserRange)
Tries = 0
while True:
    UserGuess = input("Try to guess number by typing it: ")
    if UserGuess.isdigit():
        UserGuess = int(UserGuess)
        if UserGuess <= 1:
            print("Please type a number above 1")
            continue
        elif UserGuess < GuessNumber:
            print("Your guess is lower, try again")
            Tries += 1
            continue
        elif UserGuess > GuessNumber:
            print("Your guess is higher, try again")
            Tries += 1
            continue
        else:
            print ("Congratulations you have guessed the correct number with", Tries, "tries!")
            break
    else:
        print("You typed not a number, please type a number this time")
        continue