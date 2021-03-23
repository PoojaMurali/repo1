import random
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Nummer = random.choice(number)   #random.randint(1,20) würde auch gehen
guess = int(input("Guess a number between 1 and 20:\n"))


flag = False
i = 0
while flag == False and i < 10:
    if guess == Nummer:
        print("Correct, you Win!!!")
        flag = True

    else:
        i += 1
        if guess < Nummer:
            print("Your Number was too low, try again")
            guess = int(input("Guess a number between 1 and 20:\n"))
        elif guess > Nummer:
            print("Your Number was too high, try again")
            guess = int(input("Guess a number between 1 and 20:\n"))
if flag == False and i == 10:
    print("You lost, the number was: "+ str(Nummer))
