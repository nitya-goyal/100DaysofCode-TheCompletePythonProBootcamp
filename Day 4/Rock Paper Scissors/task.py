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
choices=[rock,paper,scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input== 0 or 1 or 2:
    print(choices[user_input])
    computer_input = random.randint(0,2)
    print("Computer's Choice:")
    print(choices[computer_input])
    if user_input - computer_input ==0:
        print("Tie")
    elif computer_input-user_input== 1 or -2:
        print("You Lose!")
    else:
        print("You Win!")
else:
    print("Please enter a valid number! Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")