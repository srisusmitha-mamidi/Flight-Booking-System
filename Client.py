from Flight import Flight
from User import User
from Passenger import Passenger

def main():
    flight = Flight(flight_no=12181,no_of_classes=3,total_seats=100).build()
    p1=Passenger()
    p1.set_class_preference("EconomyClass").set_seat_preference("Window").set_age(22).set_name("Ajay")
    user1=User("Vijay")
    user1.add_passengers(p1)
    ticket = user1.book_seats(flight)
    print(ticket)
    
    print('Hello')
    
if __name__ == '__main__':
    main()