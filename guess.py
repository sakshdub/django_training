secret = 8  
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")
