import random
# create a list of options
Guess_list=['rock','paper','scissor']
# use while=true to loop through the process until player type quite
while True:
    # take input to know player wants to play or quite
    play = input("Enter Play to Play and quit to quit the game: ")
    # if the player types quit then break the loop
    if play=="quit":
        print("thanks for playing ")
        break

    computer_guess = random.choice(Guess_list)

    my_guess = input("Enter a guess: rock/paper/scissor: ").lower()
    if my_guess not in Guess_list:
        print("invalid input!")
        continue
    if computer_guess=="rock" and my_guess=="scissor":
        print("Computer wins because it guessed: ",computer_guess)
    elif computer_guess=="scissor" and my_guess=="rock":
        print("You won because computer guess was:", computer_guess)
    elif computer_guess=='scissor' and my_guess=="scissor":
        print('its a tie')
    elif computer_guess == "paper" and my_guess == "rock":
        print("Computer wins because it guessed: ", computer_guess)
    elif computer_guess == "rock" and my_guess == "paper":
        print("You won because computer guess was:", computer_guess)
    elif computer_guess == 'rock' and my_guess == "rock":
        print('its a tie')
    elif computer_guess == "scissor" and my_guess == "paper":
        print("Computer wins because it guessed: ", computer_guess)
    elif computer_guess == "paper" and my_guess == "scissor":
        print("You won because computer guess was:", computer_guess)
    elif computer_guess == 'paper' and my_guess == "paper":
        print('its a tie')

