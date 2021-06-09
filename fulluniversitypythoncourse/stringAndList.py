

word = 'anwar:woke:up:early'

wordsplited = word.split(':')
print(wordsplited)
print(len(wordsplited))
for i in wordsplited:
    print(i)

fhand = open("file.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    line = line.split()
    linesearch = line

print(linesearch)
email = linesearch[1]
print(email)
dns = email.split('@')
print(dns[1])
