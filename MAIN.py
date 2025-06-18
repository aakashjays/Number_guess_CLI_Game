import random

target =  int(random.randrange(1,100))
while True:
    guess = input("Guess the number target number or Quit(Q): ")
    if guess == ("Q"):
        break
    guess = int(guess)
    if  guess < target:
        print("You guessed small number try bigger number !!!")
    elif guess > target:
        print("You guessed bigger number try smaller number !!!")
    elif guess == target :
        print("You entered the correct number,!!!") 
        break

print("---GAMEOVER---")