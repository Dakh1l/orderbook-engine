#x = input("Enter a number: ")
#attempts = 6
#while x.isdigit() == False:
 #   print("Please enter a valid integer.")
 #   x = input("Enter a valid number: ")

#x = int(x)
#while x != 42 and attempts >= 0:
 #   if x < 42:
#        print("Too low!")
#        x = input("Try again: ")
#        while x.isdigit() == False:
#            print("Please enter a valid integer.")
#           x = input("Enter a valid number: ")
#        x = int(x)
 #       attempts -= 1
#    elif x > 42:
 #       print("Too high!")
   #     x = input("Try again: ")
 #       while x.isdigit() == False:
   #         print("Please enter a valid integer.")
   #         x = input("Enter a valid number: ")
   #     x = int(x)
  #      attempts -= 1

#if attempts == 0 and x != 42:
#    print("Sorry, you've run out of attempts.")
#else:
#    print("Congratulations! You've guessed the correct number.")
#
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