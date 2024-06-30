
class emp:
    salary=100

    @classmethod
    def change(cls,sal):
      cls.salary=sal

e=emp()

print(e.salary)
e.change(150)
print(e.salary)