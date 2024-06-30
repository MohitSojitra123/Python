number = [1,-2,3,-4,5,6,-7,-8,9,10]

for num in number:
    print(num,end=" ")

 
positive = 0

for i in number:
    if i > 0:
     positive += 1

print("Positive Number...",positive)
