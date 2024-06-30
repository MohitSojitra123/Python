letter = '''

Dear <|NAME|>,
You are Selected |

Date : <|DATE|>
....
'''


name=input("ENter Your Name...\n")
date=input("Enter Date\n")

letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)

print(letter)


# Dectect Double Space

sp="ab  cad cwer erg nh kj dfr wer gph  "

print(sp.find("  "))
print(sp.replace("  ","-"))