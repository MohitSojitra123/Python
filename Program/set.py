
set1={"keval","rahul","het"}

print(set1)

print(len(set1))

print(type(set1))


for i in set1:
    print(i)

# Not Support
# print(set1[0])    

if "keval" in set1:
    print("Precent in List")
else:
    print("Not Precent")  


if "mohit"  not in set1:
    print("Not Precent In List")
else:
    print("Precent In List")          


set1.add("mohit")

# Not Add Duplicate Value Not Allowed
set1.add("keval")

print(set1)

# Add another Sequnce

list1=[10,20,30]

set1.update(list1)

set1.remove("mohit") 

# Not Return Error
set1.discard("xzy")

print(set1)


# Join Two Set

s1={'a','b','c','d'}
s2={'a','e','f','d'}

print(s1.union(s2))

print(s1.update(s2))

# s1.intersection_update(s2)
# print(s1)

# s1.symmetric_difference(s2)
# print(s1)


# Duplicate Value Find

sett1={10,20,30,40,50,60,70}
sett2={10,20,30,100,200,300}
sett3={400,500,600,10,20,30}

final1=sett1.intersection(sett2)
final2=final1.intersection(sett3)

print(final2)