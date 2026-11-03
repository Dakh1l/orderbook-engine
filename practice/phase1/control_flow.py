attempts = 7
for i in range(attempts):
    x = input("Enter a number: ")
    while x.isdigit() == False:
        print("Please enter a valid integer.")
        x = input("Enter a valid number: ")
        #attempts += 1
    x = int(x)
    if x < 42:
        print("Too low!")
    elif x > 42:
        print("Too high!")
    else:
        break
if x == 42:
    print("Congratulations! You've guessed the correct number.")
else: 
    print("Sorry, you've run out of attempts.")
