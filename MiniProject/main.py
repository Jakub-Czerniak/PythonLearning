class reservation:
    def __init__(self,name,row,place):
        self.row=row
        self.place=place
        self.name=name

    def display(self):
        print("Row:",self.row,"Place:",self.place)
        print("Reserved by:", self.name)

class sala:
    def __init__(self, row, place):
        self.row=row
        self.place=place
        self.places=[0 for _ in range(row*place)]
        self.reservations=[reservation("",0,0) for _ in range(row*place)]

    def display(self):
        for i in range(self.row):
            for j in range(self.place):
                if self.places[i*self.place+j]==0:
                    print("\033[1;92m[",j+1,end=" ]\033[00m")
                else:
                    print("\033[1;91m[",j+1,end=" ]\033[00m")
            print("")

    def reserve(self, _reservation):
        self.reservations[self.place * (_reservation.row-1) + _reservation.place]= _reservation
        self.places[self.place * (_reservation.row-1) + _reservation.place-1]=1
        print("Status: reserved")

    def unreserve(self, row, place):
        self.places[self.place*(row-1)+place-1]=0
        self.reservations[self.place*(row-1)+place-1]=0

    def status(self, row, place):
        if(self.places[self.place*(row-1)+place-1]==0):
            print("Status: free")
        else:
            print("Status: reserved")
            self.reservations[self.place*(row-1)+place].display()

class date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def display(self):
        print(self.day,":",self.month,":",self.year)

class spectacle:
    def __init__(self,sala,date):
        self.sala=sala
        self.date=date





s=sala(10,15)

while True: 
    print("""
    1.Place reservation.
    2.Remove reservation.
    3.Display places.
    4.Check place status.
    5.Exit
    """)
    selection=input("What do you want to do:")
    if selection =='1':
        name=input("Name:")
        row=int(input("Row:"))
        place=int(input("Place:"))
        _reservation=reservation(name,row,place)
        s.reserve(_reservation)
    elif selection == '2': 
        row=int(input("Row:"))
        place=int(input("Place:"))
        s.unreserve(row,place)
    elif selection == '3':
        s.display() 
    elif selection == '4':
        row=int(input("Row:"))
        place=int(input("Place:"))
        s.status(row,place)
    elif selection == '5': 
        break
    else: 
        print("Unknown Option Selected!") 