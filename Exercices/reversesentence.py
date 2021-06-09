def reverse_sentence(string):
    a = list()
    b = list()
    a = string.split()
    tmp = -1
    for i in range(len(a)):
        b.append(a[tmp])
        tmp = tmp - 1
    b = " ".join(b)
    print(b)
    
stringtest = input("Enter your string: ")
reverse_sentence(stringtest)
