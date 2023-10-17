from Classes import Classes
class Flight:
    def __init__(self,flight_no,no_of_classes,total_seats):
        self.flight_no=flight_no
        self.no_of_classes=no_of_classes
        self.total_seats=total_seats
    def build(self):
        self.classes=[]
        for i in range(self.no_of_classes):
            if i==0:
                self.classes.append(
                        Classes(
                            class_name='EconomyClass',
                            class_no=i+1,
                            no_of_seats=self.total_seats*(40/100)
                        ).build()
                )
            if i==1:
                self.classes.append(
                        Classes(
                            class_name='FirstClass',
                            class_no=i+1,
                            no_of_seats=self.total_seats*(40/100)
                        ).build()
                    )
            if i==2:
                self.classes.append(
                        Classes(
                            class_name='BusinessClass',
                            class_no=i+1,
                            no_of_seats=self.total_seats*(20/100)
                        ).build()
                    )
        return self
    def get_available_classes(self):
        return self.no_of_classes
    
    def get_available_pref_class(self,pref):
        for clas in self.classes:
            if clas.class_name == pref and clas.status == 'Available':
                return True
        return False
    
    def get_available_pref_seat(self,seat_pref,class_pref):
        seats=Classes.get_pref_available_seats(self,seat_pref,class_pref)
        return seats
            
            
            
            
            
            
                
                
        
        
            
    
        