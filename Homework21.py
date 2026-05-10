num = int(input("Enter a number: "))

odd_numbers = [i for i in range (num * 2) if i % 2 != 0]

more_odd_numbers = [i for i in range (num * 2) if i % 2 != 0]

print("Odd numbers under", num, ":", odd_numbers)
print("Another list of odd numbers:", more_odd_numbers)