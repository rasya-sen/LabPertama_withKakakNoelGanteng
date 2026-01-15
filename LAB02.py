lives = 6
secret_word = "jeruk".upper()
secret_word1 = list(secret_word)
count = len(secret_word1)
display_word = count * ["_"]
used_words = set()
while True:
    if "_" in display_word and lives > 0:
        validGuess = False
        print("+--------------------------+")
        print(" ")
        print("Chances :", lives)
        print("".join(display_word))

        while validGuess == False:
            guess = input("Guess a letter : ").upper()
            print(" ")
            countguess = len(guess)
            if countguess > 1:
                print("Please guess one letter at a time.")
                validGuess = False
            else: 
                if guess in used_words:
                    print("You have already guessed that letter.")
                    print("+--------------------------+")
                    validGuess = False
                else:
                    used_words.add(guess)
                    validGuess = True

    
        if guess in secret_word1:
            print(guess, "is part of the word.")
            for num in range(count):
                if secret_word1[num] == guess:
                    display_word[num] = guess
                    lives = lives - 1

        else:
            print(guess, "is not part of the word.")
            lives = lives - 1
    elif lives <= 0:
        print("+--------------------------+")
        print(" ")
        print("You Lose")
        print("The word was,", secret_word)
        print(" ")
        print("+--------------------------+")
        break
    else:
        print("+--------------------------+")
        print(" ")
        print("You Win!")
        print("The word was,", secret_word)
        print(" ")
        print("+--------------------------+")
        break
