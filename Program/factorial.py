user=int(input("Enter a Number...."))

def find_facto(a):
    ans=1
    if a == 0:
        ans=1
    else:
        for i in range(1,a+1):
            ans=ans*i

    return ans

print(find_facto(user))            