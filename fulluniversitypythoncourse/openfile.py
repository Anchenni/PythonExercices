
#xfile = open("text.txt")
#readline = xfile.read()

#print(len(readline))

#print(readline[:15])

count = 0
#for i in xfile:
    #count = count + 1
    #print(i)
#xfile = open("text.txt")
#for line in xfile:
 #   line = line.strip()
 #   if line.startswith("Each"):
 #       print(line)
 #   if line.startswith("Returns"):
 #       print(line[:20])
#xfile = open("text.txt")
#for line in xfile:
#   line = line.strip()
#    if not line.startswith("Each"):
#        continue
#    print(line)
    #if line.startswith("Returns"):     #startswith("argument")  fuction that verify if the first line start with the argument asked
        #print(line[:20])
#print("number of lines ", count)

addsentence = input("Enter a word or a sentence: ")

file = open("file.txt", "a")

file.write('\n' + addsentence)




subject = input("Entrer le mot a chercher: ")
filepath = input("entrer le non de fichier: ")
try:
    fhand = open(filepath)
except:
    print("File cannot be be opened:", filepath)
    quit()

i = 0
for line in fhand:
        #line = line.strip()
        #if line.startswith('yanina:'):
            #i = i + 1
        #if not subject in line:
            #continue
        #print(line)
    if subject in line:
            i += 1
print("there is ", i, " word ", subject, " in", filepath)
