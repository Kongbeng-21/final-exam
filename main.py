class Person:
    def __init__(self,name):
        self.name = name
        
    def introduce(self):
        print (f"Hi, I'm {self.name}.")
        
class Customer(Person):
    def __init__(self,name,address):
        super().__init__(name)
        self.name = name
        self.address =address
        
    def place_order(self,item):
        return "Laptop" and "Headphones"
    
class Driver(Person):
    def __init__(self,name,vehicle):
        super().__init__(name)
        self.name = name
        self.vehicle = vehicle
        
    def deliver(self,order):
        print(f" {self.driver_name} is delivering {self.item} to {self.customer_name} using {self.vehicle}.")
        
class DeliveryOrder:
    def __init__(self,customer,item,status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status
        
    def assign_driver(self,driver):
        pass
    
    def summary(self):
        print(f"Order Summary: ")
        print(f"Item: {self.order}")
        print(f"Customer: {self.name}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.name}")


ps = Person()
ctm = Customer()
drv = Driver()
dlv_ord = DeliveryOrder()
name = "ALICE"
