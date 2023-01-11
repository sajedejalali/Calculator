numbers = int(input("how many numbers do you enter?"))

if numbers == 1 :
    a = float(input("a = "))
    print("result = ", a)

if numbers == 2 :
    a = float(input("a = "))
    b = float(input("b = "))
    action = input("which action do you want to perform(+ or - or * or /)?")
    if action == "+":
        sum = a + b
    if action == "-":
        sum = a - b
    if action == "*":
        sum = a * b
    if action == "/":
        sum = a / b

if numbers == 3 :
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    action1 = input("which action do you want to perform (1) (+ or - or * or /)?")
    action2 = input("which action do you want to perform (2) (+ or - or * or /)?")
    
    if action1 == "+":
        if action2 == "+":
            sum = a + b + c
        if action2 == "-":
            sum = a + b - c
        if action2 == "*":
            sum = a + b * c
        if action2 == "/":
            sum = a + b / c
    if action1 == "-":
        if action2 == "+":
            sum = a - b + c
        if action2 == "-":
            sum = a - b - c
        if action2 == "*":
            sum = a - b * c
        if action2 == "/":
            sum = a - b / c
    if action1 == "*":
        if action2 == "+":
            sum = a * b + c
        if action2 == "-":
            sum = a * b - c
        if action2 == "*":
            sum = a * b * c
        if action2 == "/":
            sum = a * b / c
    if action1 == "/":
        if action2 == "+":
            sum = a / b + c
        if action2 == "-":
            sum = a / b - c
        if action2 == "*":
            sum = a / b * c
        if action2 == "/":
            sum = a / b / c

print("result = ", sum)
