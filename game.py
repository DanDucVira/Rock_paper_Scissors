import random

choice = []

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
choice.append(rock)
choice.append(paper)
choice.append(scissors)

computer_choice = random.randint(0,2)


player_input = input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")




if player_input not in ["0", "1", "2"]:
    print("Invalid input. You lose!")
else:
    player_choice = int(player_input)

    print("player chose:")
    print(choice[int(player_choice)])
    print("Computer chose:")
    print(choice[computer_choice])

if player_choice == computer_choice:
        print("Its a Draw!")

elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win")
else:
    print("You Lose!")
