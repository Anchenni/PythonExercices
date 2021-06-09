choise_test = ""
secret_word = ""
guess = ""
guess_count = 0
guess_limit = 3
guess_limit_print = 3
out_of_guess = False
#cont = False



print("*******************Guess Word*****************")
print("-----------------------------------------------")




#while not(cont):
try:
    choise_test = int(input("enter \"1 for easy, 2 for medium, 3 for difficult\": "))
    if choise_test == 3:
        secret_word = "telescope"
        print("**********************")
        print("Defintion of the word")
        print("**********************")
        print("-------------------------------------------------------------------------------------")
        print("An optical instrument for making distant objects appear larger and therefore nearer.")
        #cont = True
    elif choise_test == 1:
        secret_word = "table"
        print("**********************")
        print("Defintion of the word")
        print("**********************")
        print("-------------------------------------------------------------------------------------")
        print("an article of furniture consisting of a flat, slablike top supported on one or more legs or other. ")
        #cont = True
    elif choise_test == 2:
        secret_word = "salt"
        print("**********************")
        print("Defintion of the word")
        print("**********************")
        print("-------------------------------------------------------------------------------------")
        print("a crystalline compound, sodium chloride, NaCl, occurring as a mineral, a constituent of seawater, etc., and used for seasoning food, as a preservative, etc. ")
        #cont = True
    else:
        print("Invalid choice!")

    print("-------------------------------------------------------------------------------------")


    while secret_word != guess and not(out_of_guess):
        print("you have ",guess_limit_print," chances left ")
        if (guess_count < guess_limit):
            guess = input("Enter guess: ")
            guess_count += 1
            guess_limit_print -= 1
        else:
            out_of_guess = True

    if out_of_guess:
        print("Out of Guesses, YOU LOSE!")
        print("the word was " + secret_word)
    else:
        print("YOU WIN!")

except ValueError as err:
    print("Invalid input")