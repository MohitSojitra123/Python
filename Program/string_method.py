name="welcome to code help"

# print(name[1:])
# print(name[:4])
# print(name[:])
# :2 increment  
print(name[0:15:2])



# strip --> Remove Spaace
abc = "  abc    "

print(abc)
print(abc.strip())

# remove left side stream
# print(abc.lstrip())

# remove right side stream
# print(abc.rstrip())



# Replace
val_1="mohit"

print(val_1)

print(val_1.replace("mohit","Raj"))



# Split
val_2="mohit,keval,vivek,raj,deep"

print(val_2)
print(val_2.split(","))

# find

print(val_2.find("keval"))

# count

print(val_2.count('e'))

# format

detail="My Name Is {} I am Study Is {}"

print(detail.format('man','bca'))

# join

detail_1="keval is big borther of rahul"


print(" ".join(detail_1))
print("-".join(detail_1))
print(len(detail_1))


detail_2="rahul call \"papa\" "
print(detail_2)


detail_3=["val_1","val_2","val_3","val_4"]

detail_3[0:1]=["value_123"]


detail_3[1:3]=["value_123","value_123"]

print(detail_3)

values_1="mohit sojitra"

# print(values_1.endswith('tra'))
# print(values_1.endswith('tro'))


# capitalize

# print(values_1.capitalize())


vall="rahul is study in bcom"

print("bcom" in vall)
print("bca" in vall)


print(2/2)

print(2//2)


# splite

str3="qwe rty uio asd fgh jkl"
str4=str3.split(" ")
print(str4)
