import random
import os
print("================================= Cows And Bulls Game ==================================")
print("")
print("             the players each write a 4-digit secret number.")     
print("             The digits must be all different. Then, in turn,")
print("             the players try to guess their opponent's number who gives")
print("             the number of matches. If the matching digits are")
print("             in their right positions, they are 'bulls',")
print("             if in different positions, they are 'cows'. ")
print("----------------------------------------------------------------------------------------")
print("             Example:")
print("             Secret number: 4271")
print("             Opponent's try: 1234")

print("             Answer: 1 bull and 2 cows. (The bull is '2', the cows are '4' and '1'.)")
print("=========================================================================================")
print(" ")
#clear = lambda:os.system("clear")
def random_number():
    a = list()
    for i in range(4):
        a.append(random.choice('123456789'))
    #print(a)
    return(a)

#1234

a = random_number()
#print(a)
#1345
tmp = 1;
while True:
    cows = 0
    bulls = 0
    while True:
        guess = input("Enter your guess: ")
        if len(guess) > 4 or len(guess) < 4 or len(guess) == 0:
            print("The number must be 4 digits long!")
        else:
            break
    for i in range(4):
        if guess[i] == a[i]:
            cows += 1
        elif guess[i] in a:
            bulls += 1
    if list(guess) == a:
        print("Bravo! You found the number after",tmp,"tries ")
        break
    else:
        tmp += 1
        if cows > 1 and bulls == 0:
            print(cows, "cows" ,bulls,"bull")
        elif bulls > 1 and cows == 0:
            print(cows, "cow" ,bulls,"bulls")
        elif bulls > 1 and cows > 1:
            print(cows, "cows" ,bulls,"bulls")
        else:
            print(cows, "cow" ,bulls,"bull")
    






