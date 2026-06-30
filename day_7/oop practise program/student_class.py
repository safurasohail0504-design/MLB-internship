class student:
    def __init__ (self):
        self.name=input("enter name:")
        self.rollno=input("enter rollno:")
        self.depart=input("enter depart:")
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.depart)
s1=student()
s2=student()
s1.display()
s2.display()
