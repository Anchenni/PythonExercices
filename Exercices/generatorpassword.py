import random

#alpha = random.choice('abcdefghijklmnop')
#symbol = random.choice('!@#$%^&*()_')
#number = random.randrange(10)
def password_generator():
    
    a = list()
    random.shuffle(a)
    password = list()
    if user_pass == '2':
        for i in range(4):
            a.append(random.choice('abcdefghijklmnopqrstuvwxy'))
            a.append(random.choice('!@#$%^&*()_'))
            a.append(random.choice('0123456789'))
            a.append(random.choice('ABCDEFGHIGKLMNOPQRSTUVWXY'))
    elif user_pass == '1':
        for i in range(8):
            a.append(random.choice('abcdefghijklmnopqrstuvwxy'))
            a.append(random.choice('0123456789'))
    random.shuffle(a)
    a = "".join(a)
    print("Your password is: "+a)
while True:    
    user_pass = input("Enter 1 for a weak password or 2 for a strong password: ")
    if user_pass == '1' or user_pass == '2':
        password_generator()
    else:
        print("Error You have to choise between 1 or 2!")
    gout = input("Enter 0 to exit or another key to continue: ") 
    if gout =='0':
        print("GoodBay!")
        break
    