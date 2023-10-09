#--------------------importing library--------------------
import sys
import random
#------------------------Coding----------------------------
var = 10
while var < 10000:
    print(" ______            _ _        ")
    print("|  ____|          | (_)       ")
    print("| |__ __ _ _ __ __| |_ _ __ ")
    print("|  __/ _` | '__/ _` | | '_ \  ")
    print("| | | (_| | | | (_| | | | | |")
    print("|_|  \__,_|_|  \__,_|_|_| |_| ")
    random_number = random.randint(1, 6)
    print("                            ")
    print("Welcome To The World Of LUDU")
    print("Read The Condition. \n 1. Play Ludu. \n 2. Know About Devloper. \n 3. Update This Proggram. \n 4. Exit.")
    user = input("Enter Your Opinion--> ")
    if user == "1":
        print("Your Ludu Number is", random_number)
    elif user == "2":
        print("The Name Of The Devloper Is Tanjimul Hisham (Fardin) \n Ethical Hacker, Devloper, Cyber Security Specialist \n Thanks For Using Our Tool")
    elif user == "3":
        print("You Are Up To Date \n No Need To Update This Tool")
    elif user == "4":
        break
    else:
        print("404 ERROR!!!")
    var += 1
sys.exit()