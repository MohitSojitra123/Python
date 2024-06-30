num1=int(input("Enter Value Of Num 1..."))
num2=int(input("Enter Value Of Num 2..."))

operator=input("Enter Operator :")

match operator:
    case "+":
        print("Sum Is ", num1+num2)
    case "-":
        print("Difference Is ", num1-num2)
    case "*":
        print("Multipli Is ", num1*num2)
    case "/":
        print("Divided ", num1/num2)
    case _:
        print("Enter a Valid Operator...")

        