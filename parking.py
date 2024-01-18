class Slot:
    def __init__(self,type,number) -> None:
        self.type = type
        self.number = number
        self.is_occupied = False
        self.vehicle = None
    
    def park_vehicle(self,vehicle):
        if not self.is_occupied and self.type == vehicle.type:
                self.is_occupied =  True
                self.vehicle = vehicle
                return self
        return None

    def unpark_vehicle(self):
        if self.is_occupied:
                print(f"Unparked vehicle with Registration Number: {self.vehicle.registration_number} and Color: {self.vehicle.colour}")
                self.is_occupied =  False
                self.vehicle = None

        else:
            print('Invalid Ticket')
    
    def check_occupied(self, type):
        return self.is_occupied and self.type == type
    
    def is_free(self, type):
        return not self.is_occupied and self.type == type


class Floor:
    def __init__(self,floor_no, no_of_slots) -> None:
        self.floor_no = floor_no
        self.slots = []
        self.build_slots(no_of_slots)
    
    def build_slots(self, no_of_slots):
        if no_of_slots >= 1:
            self.slots.append(Slot('TRUCK',1))
        
        if no_of_slots >= 2:
            self.slots.append(Slot('BIKE',2))
        
        if no_of_slots >= 3:
            self.slots.append(Slot('BIKE',3))
        
        for n in range(4,no_of_slots+1):
            self.slots.append(Slot('CAR',n))
    
    def check_parking(self,vehicle):

        for slot in self.slots:
            parked = slot.park_vehicle(vehicle)
            if parked:
                return parked
        return False

    def unpark_vehicle(self,slot_no):
        total_slots = len(self.slots)

        if 0 < slot_no < total_slots:
            self.slots[slot_no - 1].unpark_vehicle()
        else:
            print('Invalid Ticket')
    
    def display_occupied_slots(self,type):
        occupied_slots = []

        for slot_no in range(1,len(self.slots)+1):
            if self.slots[slot_no-1].check_occupied(type):
                occupied_slots.append(str(slot_no))
        
        return occupied_slots

    def display_free_slots(self,type):
        free_slots = []

        for slot_no in range(1,len(self.slots)+1):
            if self.slots[slot_no-1].is_free(type):
                free_slots.append(str(slot_no))
        
        return free_slots

    def display_free_count(self,type):
        free_count = 0

        for slot in self.slots:
            if slot.is_free(type):
                free_count += 1
        return free_count
        

class ParkingLot:
    def __init__(self,lot_id,no_floors,no_of_slots) -> None:
        self.lot_id = lot_id
        self.floors = []
        self.build_floors(no_floors,no_of_slots)
    
    def build_floors(self, no_floors, no_of_slots):
        for floor_no in range(no_floors):
            self.floors.append(Floor(floor_no + 1,no_of_slots))
        
    
    def park_vehicle(self,vehicle):
        
        for floor in self.floors:
            slot = floor.check_parking(vehicle)
            if slot:
                print(f"Parked vehicle. Ticket ID: {self.lot_id}_{floor.floor_no}_{slot.number}")
                return True
        print('Parking Lot Full')
        return False

    def unpark_vehicle(self, floor_no, slot_no):

        totalFloors = len(self.floors)
        if 0 < floor_no <= totalFloors:
            self.floors[floor_no - 1].unpark_vehicle(slot_no)
        else:
            print('Invalid Ticket')
    
    def display_free_count(self,type):
        for floor in self.floors:
            print(f"No. of free slots for {type} on Floor {floor.floor_no}: {floor.display_free_count(type)}")  

    def display_occupied_slots(self,type):
        for floor in self.floors:
            occupied = floor.display_occupied_slots(type)
            print(f"Occupied slots for {type} on Floor {floor.floor_no} : {','.join(occupied)}")
    
    def display_free_slots(self,type):
        for floor in self.floors:
            free = floor.display_free_slots(type)
            print(f"Free slots for {type} on Floor {floor.floor_no} : {','.join(free)}")