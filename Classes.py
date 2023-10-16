from EconomyClass import EconomyClass
from FirstClass import FirstClass
from BusinessClass import BusinessClass

class Classes:
    def __init__(self,class_name,class_no,no_of_seats):
        self.class_name=class_name
        self.class_no=class_no
        self.no_of_seats=no_of_seats
    def build(self):
        if self.class_name=='EconomyClass':
            return EconomyClass(class_name=self.class_name,class_no=self.class_no,no_of_seats=self.no_of_seats).build()
        if self.class_name=='FirstClass':
            return FirstClass(class_name=self.class_name,class_no=self.class_no,no_of_seats=self.no_of_seats).build()
        if self.class_name=='BusinessClass':
            return BusinessClass(class_name=self.class_name,class_no=self.class_no,no_of_seats=self.no_of_seats).build()
    
    
            
        
        
        