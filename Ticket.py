import random
class Ticket:
    def __init__(self,train_no):
        self.pnr = random.randint(1111111,9999999)
        self.train_no = train_no
        self.ticket_metadata = {
            "passenger" :[],
            "class_name" :[],
            "seat_no" : [],
            "position" : [],
            "status" : []
        }
    def add_reserved_passengers(self,passenger,class_name,seat_no,position,status):
        self.ticket_metadata["passenger"].append(passenger)
        self.ticket_metadata["class_name"].append(class_name)
        self.ticket_metadata["seat_no"].append(seat_no)
        self.ticket_metadata["position"].append(position)
        self.ticket_metadata["status"].append(status)