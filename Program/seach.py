a= int(input("Enter Number Of a"))
b= int(input("Enter Number Of b"))
c= int(input("Enter Number Of c"))


# if a > b and a > c:
#     print("a is Great ",a)
# elif b > a and b > c:
#     print("b is Great ",b)
# else:
#     print("c is great...",c)    

if a > b:
    if a > c:
        print("a is Great ",a)
    else:
        print("c is great ",c)       
else:
    if b > c :
        print("b is great ",b)
    else:
        print("c is great ",c)            