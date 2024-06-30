
detail={
    'name':"mohit",
    'age':18,
    'm_number':"9988562959"
}

# print(detail.keys())
# print(detail.values())

# Add

detail['pin_code']=365480


print(len(detail))


print(detail['name'])


print(detail.get('age'))


for i in detail:
    print(detail[i])


for key,value in detail.items():
    print("Key...",key)  
    print("Value...",value)  


# Dic.. inside Dic...

intro={
    "report1":{"a1":"good1","a2":"good2","a3":"good3"},
    "report2":{"b1":"bad1","b2":"bad2","b3":"bad3"},
    "report3":{"c1":"fine1","c2":"fine2","c3":"fine3"}
}

print(intro['report1'])
print(intro['report1']['a1'])

mul={
    i:i**2 for i in range(10)
    }


print(mul)
