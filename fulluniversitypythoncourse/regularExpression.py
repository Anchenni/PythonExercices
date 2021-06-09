import re


hand = open("text.txt")
for line in hand:
    line = line.rstrip()
#-----find by the first word----
#    if line.startswith('from:'):
#    if re.search('^from:', line):
#-----Find the word--------
#    if line.find('yanina') >= 0:
#    if re.search('yanina', line):
#    if re.search('^X-\S+:', line):
#        print(line)

#x = 'My 2 favorite numbers are 19 and 42'
#----find all numbers between 0 and 9, + --> one or more times
#y = re.findall('[0-9]+',x)
#------fins A or E or I or O or U
#y = re.findall('[AEIOU]+',x)
    #y = re.findall('^f.+',line)
    #y = re.findall('^X.+?:', line) #  : ---> last caracter in the match
    #y = re.findall('\S+@\S+',line) # : -----> to find between @, could be email
    #y = re.findall('^from: (\S+@\S+)', line) #the same thing Parenthese () to delimit what we are looking for
    #y = re.findall('@([^ ]*)', line)  #---->to find host in email adresse
    #y = re.findall('^from: .*@([^ ]*)', line) # the same thing but starting with a word (from)
    print(y)

#print(y)
