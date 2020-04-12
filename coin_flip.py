from random import randint
from time import sleep

total_flips = 0
total_correct = 0

def flipCoin():
    result = randint(1, 10)
    if result%2==0:
        return "Heads"
    else:
        return "Tails"

while True:
    flip = input("Would you like to flip the coin? Yes or No: ")
    if flip == "Yes" or flip == "yes":
        user_guess = input("Guess the outcome of the coin flip (Heads or Tails): ")
        cur_flip = flipCoin()
        total_flips += 1
        flip_result = (user_guess == cur_flip)
        if flip_result:
            outcome = "Correct"
            total_correct += 1
        else:
            outcome = "Incorrect"
        print("The result of the coin flip is : {result}. You guessed {outcome}.".format(result=cur_flip, outcome=outcome))
        print("You have guessed the correct result {correct} times out of {total} coin flips.".format(correct=total_correct, total=total_flips))
    else:
        break