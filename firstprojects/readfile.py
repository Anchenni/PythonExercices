
# 'a' -->to append into the file --> employed_file = open("myfile.txt", "a")
employed_file = open("index.html", "w")
# -------------- read a file-----------
# to see if the file is readable --> print(employed_file.readable())
# to read line by line print(employed_file.readline())
# to put theme in a list print(employed_file.readlines())
# the first line inside the list print(employed_file.readlines()[1])

#for i in employed_file.readlines():
#    print(i)
# -------------- write in a file-----------
employed_file.write("\n<html>")
employed_file.write("\n<p>this is a wab html page</p>")
employed_file.write("\n</html>")
employed_file.close()