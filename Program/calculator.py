print(
    '''
      + Add
      - Subtract
      * Multiply
      / Divide
    '''
)


num1=int(input("Enter The Value : 1..."))
num2=int(input("Enter The Value : 2..."))

ope=input("Enter The Operator....")

if ope == '+':
    print(num1+num2)
elif ope == '-':
    print(num1-num2)
elif ope == '*':
    print(num1*num2)
elif ope == '/':
    print(num1/num2)
else:
    print("Enter Valid Optino")                