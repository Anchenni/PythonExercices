mylist = ['anwar', 'yanina', 'brahim', 'brahim','brahim']
list_number = [12, 54, 5, 98, 43]
mylist.append("kamal")
#list_number.extend(mylist) ---> extend the list mylist inside list_number
mylist.insert(1, "soufiane")
# mylist.clear() ---> remove everything inside the list
# mylist.pop() ----> remove the last element inside the list
#print(mylist.index("yanina")) ----> to find the index of element "yanina"
#print(mylist.count("brahim")) ---> for count how many element of "brahim" inside the list
#print(mylist)
#list_number.sort() ---> sort by numerical order
#mylist.sort() ---> to sort alphabetically or
#list_number.reverse() ---> revese the list 

mylist2 = mylist.copy()
print(mylist2)