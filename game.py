import random

game = ["rock", "paper", "scissor"]
pscore = 0
cscore = 0

print("welcome to the rock paper scissor...")

while True:
    player = input("\nrock / paper / scissor (or exit): ").strip().lower()
    if player == "exit":
        print("final scores:")
        print(f"player score {pscore}")
        print(f"computer score {cscore}")
        if pscore > cscore:
            print("you won the match!! Congratulation!!")
        elif cscore > pscore:
            print("computer won!! better luck next time.")
        else:
            print("it is a tie!!")
        break

    if player not in game:
        print("invalid input!!")
        print(f"\nplayer score {pscore}")
        print(f"computer score {cscore}")
        continue

    computer = random.choice(game)
    print(f"computer choose {computer}")

    if player == computer:
        print("tie!!")
    elif player == "rock" and computer == "scissor":
        print("player won!!")
        pscore += 1
    elif player == "rock" and computer == "paper":
        print("computer won!!")
        cscore += 1
    elif player == "scissor" and computer == "rock":
        print("computer won!!")
        cscore += 1
    elif player == "scissor" and computer == "paper":
        print("player won!!")
        pscore += 1
    elif player == "paper" and computer == "scissor":
        print("computer won!!")
        cscore += 1
    elif player == "paper" and computer == "rock":
        print("player won!!")
        pscore += 1

    print(f"\nplayer score {pscore}")
    print(f"computer score {cscore}")
