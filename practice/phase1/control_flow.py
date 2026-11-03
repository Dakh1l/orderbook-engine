import random
secret_number = random.randint(1, 100)
attempts = 7
for i in range(attempts):
    x = input("Enter a number: ")
    while x.isdigit() == False:
        print("Please enter a valid integer.")
        x = input("Enter a valid number: ")
    x = int(x)
    if x < secret_number:
        print("Too low!")
    elif x > secret_number:
        print("Too high!")
    else:
        break
if x == secret_number:
    print("Congratulations! You've guessed the correct number.")
else: 
    print("Sorry, you've run out of attempts.")