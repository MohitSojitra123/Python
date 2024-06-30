gender = input("Enter Male (m) or Female (f) : ")
age = int(input("Enter Age"))

if gender == 'm':
    if age >= 21:
        print("Legal Age Of Marriage")
    else:
        print("Not Legal Age Of Marriage")
elif gender == 'f':
     if age >= 18:
        print("Legal Age Of Marriage")
     else:
        print("Not Legal Age Of Marriage")
else:
     print("Enter Valid Data...")   
