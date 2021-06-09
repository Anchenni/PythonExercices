#----------------Countign Pattern----------


dictio1 = dict()
#text = input("Enter a line of text: ")
fhand = open("text.txt")
text = fhand.read()
text = text.split()
print("text: ", text)
for line in text:

    dictio1[line] = dictio1.get(line, 0) + 1

print("dictionarie 1: ", dictio1)

#--------Retrieving list of keys and values-------------

print("keys: ", dictio1.keys())
print("Values: ", dictio1.values())
print("Items: ", dictio1.items())
print("--------------Items (Êlements)---------------")
for a,b in dictio1.items():
    print(a,b)