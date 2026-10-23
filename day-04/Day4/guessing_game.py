secret_number =12
attempt = 0
guess_correct = 0
while attempt < 5 and guess_correct == False:
    guess = input ("Guess number : ")
    if guess.isdigit():
        guess_value = int(guess)
        if guess_value < 1 and guess_value > 20 :
            print("The correct range is 1 to 20")
        else:    
           attempt += 1
           if guess_value == secret_number:
                print ("CORRECT!")
                guess_correct = True
           elif guess_value < secret_number:
                print("Too low")
           else:           
                print("Too high")
              
if guess_correct == False:
    print(f"Failed to guess, Secret number is {secret_number}")