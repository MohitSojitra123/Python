arr=['val1','val2','val3','val4','val5','val6']

for a in  arr:
    print(a,end=" ")

arr.pop()


# insert element

arr.insert(0,'element1')  #element add Frist Index
arr.append("element2")  # element add Last Index


print(arr)

# copy one array to another array

new_arr=arr.copy()

print(new_arr)

squ=[x**2 for x in range(11)]
print(squ)

