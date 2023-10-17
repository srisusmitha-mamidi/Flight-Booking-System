from Ticket import Ticket

class Bookings:
    def __init__(self):
        self.bookings=[]
        
    def add_bookings(self,ticket):
        self.bookings.append(ticket)