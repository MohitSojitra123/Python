
# Creating a Tuple 

# fruit = ("apple")
# fruit = ("apple",)
fruit=tuple("apple")

print(type(fruit))

# Tuple Function 

colours=('red','yellow','green')

print(len(colours))

# Accesing Item

print(colours[1])
print(colours[-1])
print(colours[0:2])
print(colours[0:])
print(colours[:1])

# Check Item Is exists in Tuple

if "red1" in colours:
    print("Present")
else:
    print("Not Present")  

if "red" not in colours:
    print("red1 is Not Present In Tuple")
else:
    print("red1 is Present")   

 
cl1 , cl2 , cl3=colours

print(cl1)
print(cl2)
print(cl3)

tu=(50,40,30,20,10)

# for i in reversed(tu):
#     print(i)

# tuple are store in reverse formate in list and list is convert in tuple

list1=[]

for i in reversed(tu):
    list1.append(i)

# converting list type to tuple type
print(tuple(list1))    


