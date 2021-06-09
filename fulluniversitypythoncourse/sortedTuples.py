name = input("Enter File name: ")

if len(name) < 1:
    name = "text.txt"

hand = open(name)

dictio = dict()
for line in hand:
    line.rstrip()
    linesplit = line.split()
    for i in linesplit:
        dictio[i] = dictio.get(i, 0) + 1
#print(dictio)

mylis = list()
for v,k in dictio.items():
    tmp = (k,v)
    mylis.append(tmp)
#print(mylis)

mylistsorted = sorted(mylis, reverse=True)
#print(mylistsorted)
for v,k in mylistsorted[:3]:
    print(k,v)