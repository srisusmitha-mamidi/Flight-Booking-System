from EconomyClass import EconomyClass
from FirstClass import FirstClass
from BusinessClass import BusinessClass

class Flight:
    def __init__(self,flight_no,no_of_classes,total_seats):
        self.flight_no=flight_no
        self.no_of_classes=no_of_classes
        self.total_seats=total_seats
    def build(self):
        self.classes=[]
        for i in range(self.no_of_classes):
            if i==0:
                self.classes.append(
                        EconomyClass(
                            class_name='EconomyClass',
                            class_no=i+1,
                            no_of_seats=self.total_seats*(40/100)
                        ).build()
                )
            if i==1:
                self.classes.append(
                        BusinessClass(
                            class_name='FirstClass',
                            class_no=i+1,
                            no_of_seats=self.total_seats*(20/100)
                        ).build()
                    )
            if i==2:
                self.classes.append(
                        FirstClass(
                            class_name='BusinessClass',
                            class_no=i+1,
                            no_of_seats=self.total_seats*(40/100)
                        ).build()
                    )
        return self
    def get_available_seats(self):
        return self.total_seats
    
    def get_available_pref_class(self,class_pref):
        for clas in self.classes:
            if clas.class_name == class_pref and clas.status == 'Available':
               return True
        return False
    
    def get_available_pref_seat(self,seat_pref,class_pref):
        for clas in self.classes:
            if clas.class_name == class_pref and clas.status == 'Available':
               seats=clas.get_available_pref_seats(seat_pref)
        return seats
    
    def allot_seat(self,passenger,class_pref,seat_pref):
        if class_pref and seat_pref:
            for clas in self.classes:
                for seat in clas.seats:
                    if seat.status=='Available' and seat.position==passenger.seat_preference:
                        seat.status='Booked'
                        clas.no_of_seats-=1
                        clas.booked_seats+=1
                        return (clas.class_name,seat.seat_no,seat.position)
        elif class_pref:
            for clas in self.classes:
                for seat in clas.seats:
                    if seat.status=='Available':
                        seat.status='Booked'
                        clas.no_of_seats-=1
                        clas.booked_seats+=1
                        return (clas.class_name,seat.seat_no,seat.position)
    def release_cancelled_seats(self,class_pref,seat_pref,seat_no):
        for clas in self.classes:
            if clas.class_name==class_pref:
                for seat in clas.seats:
                    if seat.status=='Booked' and seat.position==seat_pref and seat.seat_no==seat_no:
                        seat.status='Available'
                        clas.no_of_seats+=1
                        clas.booked_seats-=1
                        self.total_seats+=1
        
        
                        
                        
                        
                        
            
        
        
        
            
            
            
            
            
            
                
                
        
        
            
    
        