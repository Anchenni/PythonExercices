a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b  = list()

for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
print(b)

print([a[i] for i in range(len(a)) if a[i] % 2 == 0])

print([a[j] for j in range(len(a)) if a[j] % 2 == 1])

"""

name = input("Enter Your name: ")
age = int(input("Enter your age: "))
ageold = 2021 - age
print("Hello " + name + " in", ageold + 100, "You'll be 100 years old!")
"""