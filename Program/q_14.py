items = ["apple","bananna","orange","apple","mango"]

unique_item = set()

for item in items:
    if item == unique_item:
        print("Duplicate : ",item)
        break
    unique_item.add(item)

    
    
print(unique_item)
