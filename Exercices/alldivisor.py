#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Enter a number: "))
a = list()
for i in range(1,num+1):
    if num % i == 0:
        a.append(i)
print(a)
print(i)
print([j for j in range(1, num + 1) if num % j == 0])
print([x for x in range(1, num + 1) if num % x == 0])