def print_squares(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    print("Evens:", [n for n in squares if n % 2 == 0])
    print("Odds:", [n for n in squares if n % 2 != 0])
print_squares(1,10)
