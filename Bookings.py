from Ticket import Ticket

class Bookings:
    def __init__(self):
        self.bookings=[]
        
    def add_bookings(self,ticket):
        self.bookings.append(ticket)
        
    def show_bookings(self):
        print('-'*61)
        print(f'| {"S.No.".rjust(6)} | {"Flight No.".rjust(10)} | {"PNR".rjust(12)} | {"No. of Passengers".rjust(20)} |')
        print('-'*61)
        for i in range(len(self.bookings)):
            print(f'| {str(i+1).ljust(6)} | {str(self.bookings[i].train_no).rjust(10)} | {str(self.bookings[i].pnr).rjust(12)} | {str(len(self.bookings[i].ticket_metadata["passenger"])).rjust(20)} |')
        print('-'*61)