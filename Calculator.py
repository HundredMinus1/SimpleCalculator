C = "n"

while C == "n":
    print("Simple Calculator 1.0")
    print("//+-*/ for the operations")
    A = int(input("Enter your first number here: "))
    Opera = input("Enter your operation here: ")
    B = int(input("Enter your second number here: "))
   
    if Opera == "+":
        print("Result: ", A+B)
        C = input("Exit calculator? (y/n) ")
    elif Opera == "-":
        print("Result: ", A-B)
        C = input("Exit calculator? (y/n) ")
    elif Opera == "*":
        print("Result: ", A*B)
        C = input("Exit calculator? (y/n) ")
    elif Opera == "/":
        print("Result: ", A/B)
        C = input("Exit calculator? (y/n) ")
    elif Opera == "//":
        print("Result: ", A//B)
        C = input("Exit calculator? (y/n) ")
    elif Opera == "**":
        print("Result: ", A**B)
        C = input("Exit calculator? (y/n) ")


    


