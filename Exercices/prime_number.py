def prime_number():
    #a = [1,2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    num = int(input("Enter a number or 0 to exit: "))
    #for k in range(len(a)):
        #num = a[k]
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if num == 0:
        #count += 1
        exit()
    if count == 0:
        print("The number", num, "is a prime number")
        prime_number()
    else:
        print("The number", num, "is not a prime number")
        prime_number()    
    return 0
prime_number()