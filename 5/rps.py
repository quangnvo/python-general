import random  # import random module for randint function
import sys  # import sys module for exit function
from enum import Enum  # import Enum class from enum module


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input(
    "Enter ... \n 1 for Rock \n 2 for Paper \n 3 for Scissors: \n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose", player)
print("Computer chose", computer)
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😗 It's a tie!")
else:
    print("🐍 Python wins!")
