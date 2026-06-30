class person:
    def __init__(self, n, id, d):
        self.name=n
        self.id=id
        self.depart=d
    def display(self):
        print(self.name)
        print(self.id)
        print(self.depart)
class teacher(person):
    def __init__(self,n,id,d,t):
        super().__init__(n,id,d)
        self.new=t
t1=teacher("Sarah",5,"Math","phd holder")
t1.display()
print(t1.name)
print(t1.id)
print(t1.depart)
print(t1.new)