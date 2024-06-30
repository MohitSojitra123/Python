student={
    "name":"mohit",
    'math':88,
    'phy':89,
    'chem':87
}

student.update({'total':230})

print(len(student))
print(student.values())
print(student.keys())
print(student.items()) 
print(student['name'])
print(student.get('name'))
