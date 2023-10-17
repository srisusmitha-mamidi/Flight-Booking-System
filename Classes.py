from EconomyClass import EconomyClass
from FirstClass import FirstClass
from BusinessClass import BusinessClass

class Classes:
    def __init__(self,class_name,class_no,no_of_seats):
        self.class_name=class_name
        self.class_no=class_no
        self.no_of_seats=no_of_seats
        self.available_classes=3
        self.status='Available'
    def build(self):
        if self.class_name=='EconomyClass':
            EconomyClass(self.class_name,self.class_no,self.no_of_seats,self.status).build()
            return self 
        elif self.class_name=='FirstClass':
            FirstClass(self.class_name,self.class_no,self.no_of_seats,self.status).build()
            return self
        elif self.class_name=='BusinessClass':
            BusinessClass(self.class_name,self.class_no,self.no_of_seats,self.status).build()
            return self
        
    def get_pref_available_seats(self,seat_pref,class_pref):
        if class_pref=='EconomyClass':
            seats=EconomyClass.get_pref_available_seats(self,seat_pref)
        elif class_pref=='FirstClass':
            seats=FirstClass.get_pref_available_seats(self,seat_pref)
        elif class_pref=='BusinessClass':
            seats=BusinessClass.get_pref_available_seats(self,seat_pref)
        return seats
        
    
        
        
        
    
    
            
        
        
        