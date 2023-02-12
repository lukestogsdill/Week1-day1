class Garage():
    def __init__(self, num_of_tickets):
        self.num_of_tickets = num_of_tickets
        self.tickets = []
        self.parking = []
        self.current_ticket= {}

    def create_garage(self):

        self.parking = [luke_bike.look, luke_car.look, luke_truck.look]
        self.tickets = [i for i in range(self.num_of_tickets)]
        spaces_open = len(self.tickets) - len(self.parking)
        for i in range(spaces_open):
            self.parking.append('____')

        print('              / \ ')
        print('__________----|_|_______')
        parked = ''
        for i,x in enumerate(self.parking):
            if i%2 == 0:
                parked += f'|_{x}     |'
            elif i%2 == 1:
                parked += f'|_{x}     |'[::-1] +'\n'
              
        print(parked)

    def space_display(self):
        print(f'\nSpaces open: {len(self.tickets)}')

    # def add_car(self):

    def runner(self):
            self.create_garage()
            self.space_display()
            print(self.tickets)

class Vehicle(Garage):
    def __init__(self, year, make, model, look):
        self.year = year
        self.make = make
        self.model = model
        self.look = look

luke = Garage(8)
luke_car = Vehicle(2004,'Mazda','3',':-:_')
luke_truck = Vehicle(2004, 'Toyota', 'Tundra', ':-:=')
luke_bike = Vehicle('2005','Sting','Ray','.-._')
luke.runner()