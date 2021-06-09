import re

hand = open("regex.txt")
numlist = list()
for line in hand:
    line = line.strip()
    number = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(number) != 1:
        continue
    #print(number)
    num = float(number[0])
    numlist.append(num)
    print(numlist)
print("Maximum is: ", max(numlist))
print("Minimum is: ", min(numlist))


x = 'We just received $10.00 for cookies.'
price = re.findall('\$[0-9.]+', x)
print(price)