from Ticket import Ticket

class User:
    def __init__(self,name):
        self.name=name
        self.passengers=[]
    
    def add_passengers(self,passenger):
        self.passengers.append(passenger)
        
    def book_seats(self,flight):
        ticket = Ticket(flight.flight_no)
        if flight.get_available_seats() >= len(self.passengers):
            for passenger in self.passengers:
                class_pref = passenger.class_preference
                seat_pref = passenger.seat_preference
                if flight.get_available_pref_class(class_pref) == True:
                    if flight.get_available_pref_seat(seat_pref,class_pref):
                        class_name, seat_no, position = flight.allot_seat(passenger,class_pref=True,seat_pref=True)
                    else:
                        class_name, seat_no, position = flight.allot_seat(passenger,class_pref=True,seat_pref=False)
                    ticket.add_reserved_passengers(passenger,class_name,seat_no,position,status='Booked')
                else:
                    return 'Seats are not available in your preferred class'
        return ticket
    def cancel_seats(self,flight,passenger,ticket):
        for psngr in self.passengers:
            if psngr.name==passenger.name:
                class_pref = psngr.class_preference
                seat_pref = psngr.seat_preference
                seat_no=ticket.get_seat_no(passenger)
                flight.release_cancelled_seats(class_pref,seat_pref,seat_no)
                ticket.remove_cancelled_passengers(psngr)
        return ticket
        
                
                        
                    
            
        