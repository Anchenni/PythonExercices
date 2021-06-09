


try:
    name = input("Enter file: ")
    fhand = open(name)
except:
    print("The file cannot be opened")
    quit()
#text = fhand.read()
mydict = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        mydict[word] = mydict.get(word, 0) + 1

count = -1
word = None

for a,b in mydict.items():
    if b > count:
        count = b
        word = a
print("done: ", word, count)

