try: 
    age = int(input("Enter age: "))
    if age % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Value Error")