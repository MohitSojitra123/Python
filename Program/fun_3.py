def fun1():
    x=100

    def fun2():
       print(x)

    return fun2

myresult =fun1()

myresult()