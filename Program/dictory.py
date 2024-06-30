dic={
    'name':"mohit",
    'std':12,
    'city':'vadiya'
}

print(dic)

print(len(dic))

print(type(dic))

print(dic['name'])
print(dic['std'])

dic['name']='keval'

# remove 

dic.pop('std')

print(dic)

# for i in dic:
#     print(dic[i])


for x,y in dic.items():
    print(x ,  y)


# Nested Dictionaries

phone={
    'area1':{
        'x':10,
        'y':20,
        'z':30
    },
    'area2':{
        'a':40,
        'b':50,
        'c':60
    },
    'area3':{
        'p':70,
        'q':80,
        'r':90
    }
}

print(phone['area1']['x'])
print(phone['area2']['b'])
print(phone['area3']['r'])


dic2={
    'a':100,
    'b':200,
    'c':300
}

print(sum(dic2.values()))

# # two list merge and create dic...
# l1=['a','b','c']

# l2=[1,2,3]

# dic123 =dict(zip(l1,l2))

# print(dic123)


# Reverce String
str1='abcdefghijklmnop'

str2=str1[::-1]
print(str2)




