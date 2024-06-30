
class emp:
    company = "Google"
    # salary=None
    def getSalary(self):
        print(f"Salary Is {self.salary} and Company Is {self.company}")


mh  = emp()
mh.salary=10000

mh.getSalary()