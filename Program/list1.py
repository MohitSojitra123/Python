# fruits=["apple","mango","cherry","banana"]


# print(len(fruits))

# print(type(fruits))

# print(fruits[0])
# print(fruits[-2])
# print(fruits[1:3])
# print(fruits[-3:-1])
# print(fruits[:2])
# print(fruits[2:])


# fruits.insert(2,"mango123")
# fruits.append("mango321")

# li=[10,20,30]

# fruits.append(li)

# fruits.pop(1)
# fruits.pop()
# fruits.remove()


# print(fruits)

# if "banana" in fruits:
#     print("Bnana Is Part Of The List")
# else:
#     print("Banana Is Not A Part of The List")    


# if "kiwi" is not fruits:
#     print("Not Present")
# else:
#     print("Present")    


# Chageing Items
  
# li1=[10,20,30,40,50,60]

# print(li1)

# li1[0]=100
# li1[2:4]=[300,400]

# print(li1)


# Sorting

list1=['a','h','b','i','c','j','k','d','l','e','m','f','n','o','g']

# list1.sort()
# list1.sort(reverse=True)
list1.reverse()
print(list1)

# copy

list2=list1.copy()

print(list2)


# nested list

list3=[10,20,30,40,50,[100,200,300,[400,500]]]
#      0  1  2  3  4    5[0  1  2    3]

print(list3[5][0])
print(list3[5][3][0])

