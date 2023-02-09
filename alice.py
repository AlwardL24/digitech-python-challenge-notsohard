def guess():
    line = input("Guess? ")

    if line.lower() == "electricity":
        print("You guessed it! Buzzzz")
    else:
        print("Not even close.")
        guess()

print("What is my favorite food?")
guess()