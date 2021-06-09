print("-------------#The Fibonnaci seqence#-------------")

def febonnaci(a):
    if a==1:
        b=[1]
    elif a!=1:
        b=[1,1]
        for i in b:
            if len(b)<a:
                i=b[-1]+b[-2]
                b.append(i)
    print(b)

a = int(input('Please input number: '))
febonnaci(a)