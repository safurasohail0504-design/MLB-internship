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
    def display(self):
        print("from student:",self.name)
s1=student("mylon",1,"IT","intelligent")
print(s1.name)
s1.display()