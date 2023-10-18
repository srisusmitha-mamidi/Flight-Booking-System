from Seat import Seat
class EconomyClass():
    def __init__(self,class_name,class_no,no_of_seats):
        self.class_name=class_name
        self.class_no=class_no
        self.no_of_seats=no_of_seats
        self.status='Available'
        self.booked_seats=0
    def build(self):
        self.seats=[]
        k=1
        while k<=self.no_of_seats:
            self.seats.append(
                Seat(
                    seat_no=k,
                    position='Window',               
                )
            )
            k+=1
            self.seats.append(
                Seat(
                    seat_no=k,
                    position='Aisle',             
                )
            )
            k+=1
        return self
    def get_available_seats(self):
        return self.no_of_seats
    
    def get_available_pref_seats(self,pref):
        no_of_pref_seats=0
        for seat in self.seats:
            if seat.position==pref and seat.status=='Available':
                no_of_pref_seats+=1
        return no_of_pref_seats
                
                
        
        