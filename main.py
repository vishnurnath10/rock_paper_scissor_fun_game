import random
moves = ["rock", "paper", "scissors"]
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
art=[rock, paper, scissors]

user_choice = int(input("Enter 0  for rock, 1 for paper and 2 for scissor : "))

if user_choice < 0 or user_choice > 2:
    print("enter correct value")
else:
    print(moves[user_choice])
    print(art[user_choice])
    computer_choice = random.randint(0,2)

    print(moves[computer_choice])
    print(art[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == 0 and computer_choice ==2) or ( user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
        print("User Win")
    else:
        print("Computer Win")