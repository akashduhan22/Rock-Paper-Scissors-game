import random
##l=[10,20,30]
##print(random.choice(l))
##def computer():
##        return(comp)
####print(computer())
def again():
    play=input("Do you want to play again(Y/N):").lower()
    if play=="yes" or play=="y":
        user()
    elif play=="no" or play=="n":
        print("Thanks for playing the game!!!")
    else:
        print("sorry I didn't understand can you tell me again!!!")
        again()

def user():
    l=["rock","paper","scissors"]
    print()
    comp=random.choice(l)
    print()
    print("--Welcome to Rock Paper Scissors game--")
    print()
    choice=input("Choices are:\n1.Rock\n2.Paper\n3.Scissors\nEnter your choice:-").lower()
    if choice==comp:
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("Your match is tie!!!")
        again()
    elif choice=="rock" and comp=="paper":
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("You loose!!! ")
        again()
    elif choice=="rock" and comp=="scissors":
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("You won !!!")
        again()
    elif choice=="paper" and comp=="scissors":
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("You loose !!!")
        again()
    elif choice=="paper" and comp=="rock":
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("You won !!!")
        again()
    elif choice=="scissors" and comp=="paper":
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("You won !!!")
        again()
    elif choice=="scissors" and comp=="rock":
        print()
        print(f"Your choice is {choice}")
        print(f"Computer choice is {comp}")
        print()
        print("You loose !!!")
        again()
    else:
        print()
        print("Enter the proper message:")
        user()

user()