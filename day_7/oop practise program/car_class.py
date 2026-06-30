class car:
    def __init__ (self):
        self.car_company=input("enter car company:")
        self.car_colour=input("enter colour:")
        self.car_model=input("enter model:")
        self.car_price=int(input("enter price:"))
    def display(self):
        print(self.car_company)
        print(self.car_colour)
        print(self.car_model)
        print(self.car_price)
    def price_demand(self):
        if(self.car_price>500000):
            print("not affordable")
        else:
            print("affordable")
c1=car()
c2=car()
c1.display()
c1.price_demand()
c2.display()
c2.price_demand()