class a1:
    def pr(self):
        return "mohit1"
    
class a2(a1):
    def pr(self):
        return "mohit2"

obj1 = a1()
print(obj1.pr())


obj2 = a2()
print(obj2.pr())