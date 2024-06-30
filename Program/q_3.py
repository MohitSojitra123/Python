user=int(input("Enter Your Grade..."))

print(user)

g=""
if user >= 101:
    print("Pleace Enter Valid Detail")
else:
 if user >=90:
    g= 'A+'
 elif user >=80:
    g= 'A'
 elif user >=70:
     g='B'
 elif user >= 60:
    g='C'
 elif user >= 50:
    g='D'
 else:
    g="Fail"
    

print("Grade Is...",g)   


