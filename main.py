class Person:
    def __init__(self,name):
        self.name = name
        
    def introduce(self):
        print (f"Hi, I'm {self.name}.")
        
class Customer(Person):
    def __init__(self,name,address,item):
        super().__init__(name)
        self.name = name
        self.address =address
        self.item = item
        
    def place_order(self,item):
        return item
    
class Driver(Person):
    def __init__(self,name,vehicle,order):
        super().__init__(name)
        self.name = name
        self.vehicle = vehicle
        self.order = order
        
    def deliver(self,order):
        print(f" {self.driver_name} is delivering {self.item} to {self.customer_name} using {self.vehicle}.")
        return order
        
class DeliveryOrder:
    def __init__(self,name,customer,item,status="preparing"):
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

name = ["Alice","Bob"]
customer = ["Alice","Bob"]
item =["Laptop","Headphones"]
vehicle = "motorcycle"
status = ['preparing','delivering','delivered']
driver = ["David"]
order = []
ps = Person(name)
ctm = Customer(name,item)
drv = Driver(name,vehicle,order)
dlv_ord = DeliveryOrder(name,customer,driver,item,status)

