# Pass By Value => Not Change Original Value (inmutable)


def fun_1(a):
    a=a+1
    print(a)

x=10
fun_1(x)

print(x)

# Pass By Reference =>Change Original Value (mutable)

def add(pass_list):
   pass_list.append(50)
   print(pass_list)

list1=[10,20,30,40]
add(list1) 


print(list1)
