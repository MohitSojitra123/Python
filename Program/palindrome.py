list1=[1,2,1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("Palindrome")
else:
    print("Not Palindrome")    

tup=('A','B','A','D','C','B','D','A')

print(tup.count('A'))