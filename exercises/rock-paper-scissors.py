import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Start
moves = ['ROCK', 'PAPER', 'SCISSORS']
hands = [rock, paper, scissors]

print("Welcome to ROCK PAPER SCISSORS!")

player_choice = input("Choose! (Type R, P or S)")

if player_choice == "R":
    player_choice = moves[0]
    print(f"You chose {player_choice}.")
    print(hands[0])

elif player_choice == "P":
    player_choice = moves[1]
    print(f"You chose {player_choice}.")
    print(hands[1])

elif player_choice == "S":
    player_choice = moves[2]
    print(f"You chose {player_choice}.")
    print(hands[2])

else:
    print("Invalid choice. Please choose R, P, or S.")

# Opponent choice
computer_choice = random.randint(0, 2)
move = moves[computer_choice]
print(f"Your opponent chose {move}")
print(hands[computer_choice])

game = ['WIN', 'LOSE', 'DRAW']

if player_choice == move:
    print(f"It's a {game[2]}!")

elif (player_choice == moves[0] and move == moves[2]) or (player_choice == moves[1] and move == moves[0]) or (player_choice == moves[2] and move == moves[1]):
    print(f"You {game[0]}!")

else:
    print(f"You {game[1]}!")