import random

def game():
    # generate random number
   
    secret_num = random.randint(1, 10)
    guesses = []


    while len(guesses) < 5:
         # safely make aan int
        try:
            # get number guess from player
            guess = int(input("guess a number between 1 and 10 > "))
            
        except ValueError:
            print(" The value {} you entered is not a number. ".format(guess))
        else:
            # compare guess to secret number 
            if guess == secret_num:
                print("Yeyyyy u got it. My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}. ".format(guess))
            elif guess > secret_num:
                 print("My number is lower than {} .".format(guess))
            # print hit/miss
            else:
                print("Thats not it.")
            guesses.append(guess)
    else:
        print("You did not get it sorry my friend. My number was {}".format(secret_num))
        
    play_again = input("Do you want to play again?  Y/n > ")
    if play_again.lower() != "n":
        game()
         
    else:
        print("Bye....!!!! Thanks for playing my game. Hope you play again soon")

# calling game function 
game()