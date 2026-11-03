x = float(input("Enter a number: "))
for i in range(6):
    if x < 42:
        print("Too low!")
        x = float(input("Try again: "))
    elif x > 42:
        print("Too high!")
        x = float(input("Try again: "))

if x == 42:
    print("Congratulations! You've guessed the correct number.")
else:
    print("Sorry, you've run out of attempts.")