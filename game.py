import random
import time
header = "\033[1;36;40mWelcome!\033[0m"
middle = header.center(130)
print(middle)
print()
print("Do you want to start or leave?")
input1 = int(input("Option (Type 1 or 2): "))
#---------------------------------------------------------------------------------
#Methoden erstellen für die beiden Spiele:
def roll_the_dice():
    random_number = random.randint(1,7)
    sh1 = input("Roll the Dice! Type Roll to begin!: ")
    if sh1 == "Roll":
        print("Please wait 5 Seconds...")
        time.sleep(5)
        print(f"The Result is: {random_number}.")
    else:
        input("I'm sorry I didn't understand your input!")
        exit()

def flip_the_coin():
    choises = ["Head", "Number"]
    random_value = random.choice(choises)
    sh2 = input("Flip the Coin! Type Flip to begin!: ")
    if sh2 == "Flip":
        print("Please wait 5 seconds...")
        time.sleep(5)
        print(f"The Result is: {random_value}")
    else:
        input("I'm sorry I didn't understand your input!")
        exit()
#---------------------------------------------------------------------------------
if input1 == 1:
    print("Alright lets go!")
    print()
elif input1 == 2:
    input("\033[1;33;40mGod loves you!\033[0m Never forget that. Thank you for using my program!")
    exit()      #Damit lässt sich das programm direkt beenden
while True:
    print("First of all, Choose between:")
    for i in["• \033[34mRoll the Dice!\033[0m", "• \033[34mFlip the Coin!\033[0m", "• \033[34mSocial Media\033[0m", "• \033[31mEnd the program\033[0m"]:
        print(i)
    print("(Type the number 1,2,3 or 4)")
    print()
    while True:
        chse = input("Choice (1,2,3 or 4): ")
        if chse == "1":
            roll_the_dice()
        elif chse == "2":
            flip_the_coin()
        elif chse == "3":
            print()
            for social_media in["\033[33mInstagram\033[0m: faxi.ffoo", "\033[34mDiscord\033[0m: TimespyPShell","\033[34mLinkedIn\033[0m: einschaf boy", "\033[31mGitHub\033[0m: Colleblock83"]:
                print(social_media)
            print()
        elif chse == "4":
            break
    break
print("Thanks for using my Program, \033[1;33;40mGod loves you!\033[0m")
input("Press any key to leave...")
exit()