import Logo_game
import random
import Data_game
import os
print(Logo_game.logo)
score =0


def display_accountinfo(account):
    name=account['name']
    description=account['description']
    country= comapre1['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guess,follower_count1,follower_count2):
    if follower_count1<follower_count2:
        if guess ==1:
            return False
        else:
            return True
        
    else:
        if guess == 1:
            return True
        else:
            return False
compare2 = random.choice(Data_game.data_game)
continue_flag = True
        
while  continue_flag:
    comapre1= compare2
    compare2 = random.choice(Data_game.data_game)


    display_accountinfo(comapre1)
    display_accountinfo(compare2)
    print(f"Compare 1 : {display_accountinfo(comapre1)}")
    print (Logo_game.vs)
    print(f"Compare 2 : {display_accountinfo(compare2)}")

    guess = int (input("Who has more follower Type '1' or '2' ?"))

    follower_count1 = comapre1['follower_count']
    follower_count2 = compare2['follower_count']

    os.system('cls')
    print(Logo_game.logo)
        
    is_correct =check_answer(guess,follower_count1,follower_count2)
    if is_correct == True:
        score+=1
        print(f"You are right.Your score is {score}")

    else:
        print(f"You are wrong .Your final score  is {score}")
        continue_flag = False
    