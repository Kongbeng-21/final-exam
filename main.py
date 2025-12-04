class Person:
    def __init__(self,name):
        self.name = name
        
    def introduce(self):
        print (f"Hi, I'm {self.name}.")
        
class Customer(Person):
    def __init__(self,name,address):
        self.name = name
        self.address =address
        
    def place_order(self,item):
        return 
    
class Driver(Person):
    def __init__(self,name,vehicle):
        self.name = name
        self.vehicle = vehicle
        
    def deliver(self,order):
        print(f" {self.driver_name} is delivering {self.item} to {self.customer_name} using {self.vehicle}.")
        
class DeliveryOrder:
    def __init__(self,customer,item,status):
        self.customer = customer
        self.item = item
        self.status = status
        
    def assign_driver(self,driver):
        pass
    
    def summary(self):
        return
