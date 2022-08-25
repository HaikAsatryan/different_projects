import random
print("Welcome to Rock Paper Scissors game developed by Haik")
while True:
    Decision = input("Do you want to start playing RPS (Yes/No)?: ").lower()
    if Decision == "yes":
        UserName = input("Please type your name: ") + " jan"
        break
    elif Decision == "no":
        print(":(")
        quit()
    else:
        print("Please type only yes or no")
        continue
UserScore = 0
ComputerScore = 0
while True:
    PossibleOptions = ["paper", "rock", "scissors"]
    UserOption = input(UserName + " choose Paper/Rock/Scissors or Q for quitting: ").lower()
    if UserOption in PossibleOptions:
        ComputerOption = random.randint(0,2)
        if UserOption == "paper" and PossibleOptions[ComputerOption] == "rock":
            print(UserName + " congratulation you won this round")
            UserScore +=1
            continue
        elif UserOption == "rock" and PossibleOptions[ComputerOption] == "scissors":
            print(UserName + " congratulation you won this round")
            UserScore +=1
            continue
        elif UserOption == "scissors" and PossibleOptions[ComputerOption] == "paper":
            print(UserName + " congratulation you won this round")
            UserScore += 1
            continue
        elif UserOption == "paper" and PossibleOptions[ComputerOption] == "paper":
            print(UserName + " it is draw")
            UserScore += 1
            ComputerScore += 1
            continue
        elif UserOption == "rock" and PossibleOptions[ComputerOption] == "rock":
            print(UserName + " it is draw")
            UserScore += 1
            ComputerScore += 1
            continue
        elif UserOption == "scissors" and PossibleOptions[ComputerOption] == "scissors":
            print(UserName + " it is draw")
            UserScore += 1
            ComputerScore += 1
            continue
        else:
            print(UserName + " unfortunately computer won this round")
            ComputerScore +=1
            continue
    if UserOption == "q":
        if UserScore > ComputerScore:
            print("Congratulations!", UserName, "you scored", UserScore, "and computer scored", ComputerScore)
            print("Bye bye, we will miss you, come back whenever you have time!")
            quit()
        elif UserScore < ComputerScore:
            print(UserName, "unfortunately you lost by scoring", UserScore, "because computer scored", ComputerScore)
            print("Bye bye, we will miss you, waiting for your revenge!")
            quit()
        else:
            print("It is draw!", UserName, "you scored", UserScore, "and computer scored", ComputerScore)
            print("Bye bye, we will miss you, come back whenever you have time!")
            quit()
    else:
        print(UserName + " I cannot understand what you want")
        continue