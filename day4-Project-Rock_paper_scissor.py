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
gamename = [rock,paper,scissors]
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(gamename[user_choice])
computer_choice= random.randint(0,2)
print("Computer Choice:")
print(gamename[computer_choice])

if user_choice<0 or user_choice>2:
    print("WRONG INPUT.")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice==2:
    print("You won!")
elif user_choice == 0 and computer_choice==1:
    print("You lose.")
elif user_choice==1:
    if computer_choice==2:
        print("You lose.")
    else:
        print("You won!")
elif user_choice ==2:
    if computer_choice==1:
        print("You win!")
    else:
        print("You lose.")

