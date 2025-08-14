# Secret number
secret_number = 8

while True:
    guess = int(input("Guess the number: "))
    
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")
