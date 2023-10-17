from Ticket import Ticket
class User:
    def __init__(self,name):
        self.name=name
        self.passengers=[]
    
    def add_passengers(self,passenger):
        self.passengers.append(passenger)
        
    def book_seats(self,flight):
        ticket = Ticket(flight.flight_no)
        if flight.get_available_classes() >= len(self.passengers):
            for passenger in self.passengers:
                class_pref = passenger.class_preference
                seat_pref = passenger.seat_preference
                if flight.get_available_pref_class(class_pref) == True:
                    if flight.get_available_pref_seat(seat_pref,class_pref):
                        print(seat_pref,class_pref)
                        
                        
                    
            
        