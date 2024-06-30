detail={
    'name':"rahul",
    'std':12,
    'mobile_number':2233445566
}
    
print(detail.keys())
print(detail.items())
print(detail.values())

detail1={
    'addd':'new Item'
}

detail.update(detail1)

print(detail)