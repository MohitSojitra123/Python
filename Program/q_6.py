

password=input("Enter Your Password")

if len(password) <= 6:
    print("Password Is Great In 6")
elif len(password) <= 10:
    print("Password Is Great In 10")
elif len(password) <=15:
    print("Password Is Great In 15")
else:
    print("Enter Valid Password")           