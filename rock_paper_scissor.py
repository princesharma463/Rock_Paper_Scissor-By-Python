'''import random
user = (input("choose Rock , Paper , or scissors :-"))
computer = random.choice(["rock" , "paper" , "scissors"])

print("user choose :-",user)
print("computer choose :-",computer)

if user == computer:
    print("the game is tie!")
elif user == "rock" and computer == "scissors":
    print("user is win a game!")
elif user == "paper" and computer == "rock":
    print("user is win a game!")
elif user == "scissors" and computer == "paper":
    print("user is win a game!")
elif user in ["rock","paper","scissors"]:
    print("the computer wins!")
else:
    print("invalid option!")'''

# Second code:-

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()
computer_choice = random.choice(item_list)

print(f"User choice is = {user_choice}")
print(f"Computer choice is = {computer_choice}")

if user_choice not in item_list:
    print("Invalid input! Please choose Rock, Paper, or Scissor.")

elif user_choice == computer_choice:
    print("Match Tie!")

elif (user_choice == "Rock" and computer_choice == "Scissor") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissor" and computer_choice == "Paper"):
    print("You win! ")

else:
    print("Computer wins! ")


