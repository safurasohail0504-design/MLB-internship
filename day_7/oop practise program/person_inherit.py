class person:
    def __init__ (self,n,id,d):
        self.name=n
        self.id=id
        self.depart=d
    def display(self):
        print(self.name)
        print(self.id)
        print(self.depart)
class student(person):
    def __init__ (self,n,id,d,s):
        super().__init__(n,id,d)
        self.new=s
class teacher(person):
    def __init__ (self,n,id,d,t):
        super().__init__(n,id,d)
        self.new=t
