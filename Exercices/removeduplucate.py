a = [32,25, 26, 27, 28, 25, 32, 34, 26, 26, 26, 29, 30, 31, 32, 33, 34]

def remove_duplicate_list(a):
    b = list()
    for i in range(len(a)):
        j = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                if a[j] not in b:
                    b.append(a[i])
    print(b)
    
remove_duplicate_list(a)

def  set_duplicate(a):
    b = set(a)
    k = []
    for i in range(len(a)):
        b.add(a[i])
    b = list(b)
    print(b)
set_duplicate(a)
        