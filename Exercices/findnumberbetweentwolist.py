import random

#a = [1, 1, 2, 66, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 55, 8, 9, 10, 11, 89, 13, 66]
a = [random.randint(0,100) for i in range(20)]
b = [random.randint(0,100) for i in range(15)]
print(a)
print(b)
count = 0
if len(a) > len(b):
    count = len(a)
else:
    count = len(b)
#mylist = list()  





mylist = list()
for i in range(count):
    if len(a) > len(b):
        if a[i] in b:
            mylist.append(a[i])
    else:
        if b[i] in a:
            mylist.append(b[i])
            
print(mylist) 
# In one line (very smart)
print(list(set(a).intersection(b)))
