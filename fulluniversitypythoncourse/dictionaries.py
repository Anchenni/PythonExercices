mydict = dict()

mydict['candy'] = 12
mydict['pens'] = 10
mydict['cigarette'] = 2
print(mydict)
print(mydict['cigarette'])
mydict['candy'] = mydict['candy'] + 2
print(mydict['candy'])
mylist = list()
mylist.append(12)
mylist.append("12")
mylist.remove(12)
print("mylist are: ", mylist)
#for  the list we put data inside [] and for the dictionaries we put data inside {}

mydict2 = {1: "banana", '2':"apple", '3': 'strawberry'}
print(mydict2[1])
#Counting in dictionarie

mydict3 = dict()
list_1 = ["banana", "apple", 'strawberry', "orange", "banana", "apple", "banana"]
while 1:
    word = input("enter a word: ")
    if word == 'done':
        break
    else:
        list_1.append(word)

for word in list_1:
    #if word not in mydict3:
        #mydict3[word] = 1
    #else:
        #mydict3[word] = mydict3[word] + 1
# the 4 lines above(au dessus) is the same as below(qu'en dessous) in one line
    mydict3[word] = mydict3.get(word, 0) + 1
print(mydict3)





