a=int(input("Enter Value Of a"))
b=int(input("Enter Value Of b"))


try:
    result=a/b
except ZeroDivisionError:
    result=None
    print("Error : COnnot Divide By Zero")
finally:
   print("Ans Is...",result)
