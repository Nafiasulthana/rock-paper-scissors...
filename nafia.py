import time
import random
start=["ROCK","PAPER","SCISSOR"]
for i in start:
    print(i,end="......")
    time.sleep(3)
print("\n")
print("""WELCOME TO THE GAME
I HOPE YOU ALL KNOW THE RULES
SO LETS START THE GAME""")


print("enter the number of rounds you wanna play:")
round=int(input())

while True:
    userpoints=0
    cmppoints=0
    for i in range(round):
        choice_=["ROCK","PAPER","SCISSOR"]
        cmp_choice=random.choice(choice_)

        print("select the choices: ROCK , PAPER , SCISSOR\n")
        user_choice=input("enter the choice")
        if cmp_choice==user_choice:
            print(user_choice,"VS",cmp_choice)
            time.sleep(2)
            print("\n")
            print("oops!! its a draw\n")
            print("userpoints:",userpoints,end=" ")
            print("computerpoints:",cmppoints)
        elif user_choice=="ROCK":
            if cmp_choice=="PAPER":
                print(user_choice,"VS",cmp_choice)
                time.sleep(2)
                print("\n")
                print("paper covers the rock..\n")
                cmppoints+=1
                print("userpoints:",userpoints,end=" ")
                print("computerpoints:",cmppoints)
            else:
                print(user_choice,"VS",cmp_choice)
                time.sleep(2)
                print("\n")
                print("rock hits the scissor....\n")
                userpoints+=1
                print("userpoints:",userpoints,end=" ")
                print("computerpoints:",cmppoints)
        elif user_choice=="PAPER":
            if cmp_choice=="SCISSOR":
                print(user_choice,"VS",cmp_choice)
                time.sleep(2)
                print("\n")
                print("oops!! the scissor tore you..\n")
                cmppoints+=1
                print("userpoints:",userpoints,end=" ")
                print("computerpoints:",cmppoints)
            else:
                print(user_choice,"VS",cmp_choice)
                time.sleep(2)
                print("\n")
                print("paper covers the rock..\n")
                userpoints+=1
                print("userpoints:",userpoints,end=" ")
                print("computerpoints:",cmppoints)
        elif user_choice=="SCISSOR":
            if cmp_choice=="ROCK":
                print(user_choice,"VS",cmp_choice)
                time.sleep(2)
                print("\n")
                print("rock hits the scissor...you loose..")
                cmppoints+=1
                print("userpoints:",userpoints,end=" ")
                print("computerpoints:",cmppoints)
            else:
                print(user_choice,"VS",cmp_choice)
                time.sleep(2)
                print("\n")
                print("scissor cuts the paper..and..")
                userpoints+=1
                print("userpoints:",userpoints,end=" ")
                print("computerpoints:",cmppoints)
    if userpoints==cmppoints:
        print("DRAW")

    elif userpoints>cmppoints:
        print("YOU WONN")
    else:
        print("OMG THE COMPUTER WON..BETTER LUCK NEXT TIME")
    print("\n\n\n")

    print("if you want to play again..press y for yes")
    playagain=input()
    if playagain != 'y':
        break

print("THANKS FOR PLAYING ...BYE!!")
    