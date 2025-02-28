import random
import time

def game():
    i = 0
    x = -1
    print("WELCOME IN THE NUMBER GUESSING GAME\n" "RULES: guess the number between 1 and 100 and have FUN ")
            
    print("SELECT THE DIFFICULTY LEVEL:\n" "1. Easy (10 chances)\n" "2. Medium (5 chances)\n" "3. Hard (3 chances)\n" "4. Impossible (1 chances)\n")
            
    ch = int(input("Enter your choice: "))
            
    numc = random.randint(1, 100)
            
    if ch == 1:
        while i in range(10) and x != numc:
                
            if i == 10:
                print(f"I'm sorry you have no more chances, the number was {numc}")
                break
            
            x = int(input("Try to guess a number: "))
            i += 1
            
            if x > numc:
                print(f"Incorrect, the number is smaller than {x}")
            elif x < numc:
                print(f"Incorrect, the number is bigger than {x}")
            else:
                print(f"Correct, the number is {x}, you guessed it in {i} chances")
                break
   
    if ch == 2:
        while i in range(5) and x != numc:
                
            if i == 5:
                print(f"I'm sorry you have no more chances, the number was {numc}")
                break
            
            x = int(input("Try to guess a number: "))
            i += 1
            
            if x > numc:
                print(f"Incorrect, the number is smaller than {x}")
            elif x < numc:
                print(f"Incorrect, the number is bigger than {x}")
            else:
                print(f"Correct, the number is {x}, you guessed it in {i} chances")
                break
    
    if ch == 3:
        while i in range(3) and x != numc:
                
            if i == 3:
                print(f"I'm sorry you have no more chances, the number was {numc}")
                break
            
            x = int(input("Try to guess a number: "))
            i += 1
            
            if x > numc:
                print(f"Incorrect, the number is smaller than {x}")
            elif x < numc:
                print(f"Incorrect, the number is bigger than {x}")
            else:
                print(f"Correct, the number is {x}, you guessed it in {i} chances")
                break
    
    if ch == 4:
        while i in range(1) and x != numc:
                
            
            x = int(input("Try to guess a number: "))
            i += 1
            
            if x > numc:
                print(f"Incorrect, the number is smaller than {x}")
            elif x < numc:
                print(f"Incorrect, the number is bigger than {x}")
            else:
                print(f"Correct, the number is {x}, you guessed it in {i} chances")
                break   
            
            if i == 1:
                print(f"I'm sorry you have no more chances, the number was {numc}")
                break

while True:
    game()
    b = str(input("Do you want to play again? (yes/no) ")).strip().lower()
    if b != "no" and b != "yes":
        print("Invalid input")
        break
    elif b == "no":
        print("Thank you for playing")
        break
    
