def check_palindrome(str):

    clean_str = (str.replace(" ","")).lower()
    reverse_str=clean_str[::-1]
    return clean_str == reverse_str



user=input("Enter a string...")

if check_palindrome(user):
    print("It Is Palindrome String")
else:
    print("Not a Palindrome")    