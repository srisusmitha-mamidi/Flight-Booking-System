from Classes import Classes
class Flight:
    def __init__(self,flight_no,no_of_classes,total_seats):
        self.flight_no=flight_no
        self.no_of_classes=no_of_classes
        self.total_seats=total_seats
    def build(self):
        self.classes=[]
        self.classes.append(
                Classes(
                    class_name='EconomyClass',
                    class_no=1,
                    no_of_seats=self.total_seats*(40/100)
                ).build()
            )
        self.classes.append(
                Classes(
                    class_name='FirstClass',
                    class_no=1,
                    no_of_seats=self.total_seats*(40/100)
                ).build()
            )
        self.classes.append(
                Classes(
                    class_name='BusinessClass',
                    class_no=1,
                    no_of_seats=self.total_seats*(20/100)
                ).build()
            )
        return self
        
            
    
        