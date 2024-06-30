class detail:
    # Parameter Constructure...
    def __init__(self,name,std):
        self.name=name
        self.std=std

    def pr(self):
        print("Name Is...",self.name,"Std Is...",self.std)

obj1=detail("keval",12)

obj1.pr()