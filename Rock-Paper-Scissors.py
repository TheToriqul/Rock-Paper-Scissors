import random

user_wins = 0
bot_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)

    bot_pick = options[random_num]
    print("Bot picked", bot_pick + ".")

    if user_input == "rock" and bot_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and bot_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and bot_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        bot_wins += 1

print("You won", user_wins, "times.")
print("The bot won", bot_wins, "times.")
print("See you again. Bye, Bye.")
