class Seat:
    def __init__(self,seat_no,position):
        self.seat_no=seat_no
        self.status='Available'
        self.position=position
    def is_available(self):
        return True if self.status=='Available' else False