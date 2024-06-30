n = int(input("Enter Size Of list"))


list = []

for i in range(n):
    num = int(input())
    list.append(num)

print("List",list)

idx1=int(input("Enter Index1 : "))    
idx2=int(input("Enter Index2 : "))

temp =list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print("list", list)