from Flight import Flight
from User import User
from Passenger import Passenger
from Bookings import Bookings

def main():
    flight = Flight(flight_no=12181,no_of_classes=3,total_seats=100).build()
    p1=Passenger()
    p1.set_class_preference("EconomyClass").set_seat_preference("Window").set_age(22).set_name("Ajay")
    p2=Passenger()
    p2.set_class_preference("EconomyClass").set_seat_preference("Window").set_age(22).set_name("Vijay")
    user1=User("Vijay")
    user1.add_passengers(p1)
    user1.add_passengers(p2)
    ticket = user1.book_seats(flight)
    print(ticket) #separate ticket data will be shown
    bookings=Bookings()
    bookings.add_bookings(ticket)
    bookings.show_bookings() #all the bookings will be shown
    
    #Removing cancelled tickets
    user1.cancel_seats(flight,p1,ticket)
    print(ticket) 
    bookings.show_bookings()
    
    #adding passenger after cancellation
    user2=User("Vijay")
    p3=Passenger()
    p3.set_class_preference("EconomyClass").set_seat_preference("Aisle").set_age(22).set_name("Alia")
    user2.add_passengers(p3)
    ticket = user2.book_seats(flight)
    print(ticket) #separate ticket data will be shown
    bookings.add_bookings(ticket)
    bookings.show_bookings()
    
    
if __name__ == '__main__':
    main()