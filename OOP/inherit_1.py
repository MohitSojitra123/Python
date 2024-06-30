# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance


class detail1:
    name="Mohit"
    std=12

class detail2(detail1):

    def show_data(self):
       print("Hiii Name Is...",super().name)

obj1=detail2()

# Object Help To Call Function
obj1.show_data()

print(obj1.name)
print(obj1.std)