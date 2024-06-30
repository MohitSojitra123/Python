# def outer_fun():
#     x=40
#     def inner_fun():
#      y=20
#      print("sum of x and y is...",x+y)

#     inner_fun()


# outer_fun()    




def outer_fun():
    x=40
    def inner_fun():
     y=10
     return x+y

    return inner_fun()



fun1=outer_fun()
print(fun1)
