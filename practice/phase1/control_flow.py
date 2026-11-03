x = float(input("Enter a number: "))
attempts = 6
while x != 42 and attempts >= 0:
    if x < 42:
        print("Too low!")
        x = float(input("Try again: "))
        attempts -= 1
    elif x > 42:
        print("Too high!")
        x = float(input("Try again: "))
        attempts -= 1

if attempts == 0 and x != 42:
    print("Sorry, you've run out of attempts.")
else:
    print("Congratulations! You've guessed the correct number.")