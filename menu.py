import random
min=1
max=6
stillplay="y"


def dice_roll():
    return random.randint(min, max)


def duel_with_pc():
    pc_value=value=0
    amount=int(input("How many dices you want to roll? "))

    try:
        for i in range(amount):
            z=dice_roll()
            print(z)
            pc_value+=z
        print(f"PC got {pc_value}, now its ur turn")
        for i in range(amount):
            z=dice_roll()
            print(z)
            value=value+z
        if value>pc_value:
            print(f"You got {value}, and won")
        else:
            print(f"You got {value}, and lost")
    except:
        amount=input("You should have put in number")


def solo_rolling():
    summ=0
    repeat="y"

    while repeat=="y":
        roll=dice_roll()
        answer=input(f"You rolled {roll}, do you want to add it to your score? (y/n) ")
        if answer=="y":
            summ+=roll
            print(f"Overall score is {summ}")
        repeat=input("Do you want to roll again? (y/n) ")


def menu(stillplay):
    print("Welcome to the dice roll")

    while stillplay=="y":
        duel=input("Want to duel with computer?(y/n)")
        if duel=="y":
            duel_with_pc()
        else:
            print("Then you can roll dice by yourself :)")
            solo_rolling()            
        stillplay=input("Do you still want to play dice roll? (y/n) ")
        
    print("Goodbye, it was nice having you!")    

        
menu(stillplay)
