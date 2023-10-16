from Classes import Classes
from Seat import Seat
class BusinessClass(Classes):
    def build(self):
        self.seats=[]
        k=1
        while k<=self.no_of_seats:
            self.seats.append(
                Seat(
                    seat_no=k,
                    position='Window',
                    seat_in_class='BusinessClass'                    
                )
            )
            k+=1
            self.seats.append(
                Seat(
                    seat_no=k,
                    position='Aisle',
                    seat_in_class='BusinessClass'                    
                )
            )
            k+=1
        return self