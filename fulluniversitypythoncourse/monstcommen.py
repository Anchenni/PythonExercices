filename = input("Enter File: ")
if len(filename) < 1:
    filename = "text.txt"
hand = open(filename)


di = dict()
#i = 1
for line in hand:
    line = line.split()
    for word in line:
        di[word] = di.get(word, 0) + 1
        #print("***", i, "line", di)
        #i += 1
print(di)
count = None
word = None
mylist = list()


#----------------My way to find all words-----------------------------------


for a,b in di.items():
    if count is None or b >= count:
        count = b
        word = a
        if (b == count):
            mylist.append(a)
            #print("lis is: ", mylist)
print("word :")
for i,j in di.items():
    #print(i,j)
    if count is j:
        print(i)
#for i in mylist:
#   print(i)
print("and count = ", count)
