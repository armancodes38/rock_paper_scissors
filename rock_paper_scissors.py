import random

def play_game():
    print("Rock Papper Scissor Game")
    print("r = rock, p = papper, s = scissor")
    """
    1 for rock
    -1 for papper
    0 for scissor
    """
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice: ")
    youDict = {"r": 1, "p": -1, "s": 0}
    reverseDict = {1: "rock", -1: "papper", 0: "scissor"}
    
    try:
        you = youDict[youstr]
    except KeyError:
        print("Invalid input! Use 'r', 'p', or 's'.")
        exit()
        
    print(f"You choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")
    
    if(computer == you):
        print("its a draw!")
    else:
        if(computer == 1 and you == -1):
            print("you win")
        elif(computer == 1 and you == 0):
            print("you lose")
        elif(computer == -1 and you == 1):
            print("you lose")
        elif(computer ==-1 and you == 0):
            print("you win")
        elif(computer == 0 and you == 1):
            print("you win")
        elif(computer == 0 and you == -1):
            print("you lose")
        else:
            print("something went wrong!")

# Main game loop
while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break