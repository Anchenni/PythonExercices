x = list()
print(type(x))
print(dir(x))
x = [4, 2, 3]
#x.append(4)
#print(x)
#x.sort() #---> trier
print(len(x))  # length in the list
print(max(x))  # maximum in the list
print(min(x))  # minimum in the list
print(sum(x))  # the sum of the list
print(sum(x)/len(x))
print(max(3,98))
count = 0
total = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    count += 1
    total += float(num)
average = total / count
print(average)

mylist = list()
while True:
    num1 = input("Enter a number: ")
    if num1 == "done" : break
    value = float(num1)
    mylist.append(value)
    print(len(mylist))
average2 = sum(mylist) / len(mylist)
print(average2)


