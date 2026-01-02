print("Select your ride :")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice:"))
if (choice ==1):
    print("What type of bike?")
    print("1.Scooty\n")
    print("2.Scooter\n")
    choice2 = int(input("Enter your choice2:"))
    if choice2==1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")

elif (choice ==2):
    print("What type of car?")
    print("1.SUV\n")
    print("2.Tesla\n")
    choice3 = int(input("Enter your choice3:"))
    if choice3==1:
        print("You have selected SUV")
    else:
        print("You have selected Tesla")

else:
    print("Wrong choice!")