import random

num_random = random.randint(0,20)

count = 0
while True:
    while True:
        num = int(input("Guess the number chosen by the computer between 0 and 20: "))
        count += 1
        if num == num_random:
            print("Well done, you have guessed the number in",count,"tries!")
            break
        elif num < num_random:
            print("the number you have chosen is smaller than the number to guess!")
        elif num > num_random:
            print("the number you have chosen is bigger than the number to guess!")
    replay = input("Do you want to replay? press 1 to continue and 0 to exit: ")
    if replay == 0:
        break
    