import random  # import random module for randint function
import sys  # import sys module for exit function

print("")
playerchoice = input(
    "Enter ... \n 1 for Rock \n 2 for Paper \n 3 for Scissors: \n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3")

computerchoice = random.choice("123")

print("")
print("You chose", player)
print("Computer chose", computerchoice)
print("")
