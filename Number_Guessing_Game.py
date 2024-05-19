import random

top_of_number = input("Enter a number for range (0-?) : ")
if top_of_number.isdigit():
    top_of_number=int(top_of_number)
if top_of_number <= 0 :
        print("Please Enter a number larger than 0 !!! ")
        quit()

random_number = random.randint(0,top_of_number)

guesses=0

while True:
    guesses+=1
    user_guest=input("Enter your Guest : ")

    if user_guest.isdigit():
       user_guest=int(user_guest)
    else : 
      print (" Enter a digit number !!!")
      quit()
      continue

    if user_guest == random_number :
        print("You got it  ")
        break
    elif user_guest< random_number:
        print("Enter bigger number !!!")
    else :
        print("Enter smaler number !!!")




print("You got it in ",guesses,"Guesses")   
        
 