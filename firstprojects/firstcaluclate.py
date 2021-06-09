num1 = float(input("Entrer the first number: "))
op = input("Entrer the operator: ")
num2 = (input("Entrer the first number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print((num1 * num2))
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
