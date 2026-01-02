Medical_cause = input("Did you have a medical cause Y or N:")
atten = int(input("enter the attendance of the student:"))
if Medical_cause== 'Y':
    print("You are allowed ")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")