class employee:
    def __init__ (self):
        self.emp_id=input("enter employee id:")
        self.emp_name=input("enter employee name:")
        self.emp_depart=input("enter employee depart:")
    def report(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_depart)
e1=employee()
e1.report()
