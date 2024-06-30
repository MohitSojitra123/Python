# def factorial(n):

#     if  n==0:
#         return 1
#     ans=n*factorial(n-1)
#     return ans

# print(factorial(3))


# Using Recursion Print 5 to 1

def print_num(n):
    if n==0:
        return 1
    else:
        print(n)
        print_num(n-1)

print_num(5)        