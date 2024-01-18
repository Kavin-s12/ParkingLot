from abc import ABC,abstractmethod

class Slot(ABC):
    def __init__(self,number) -> None:
        self.number = number
        self.is_occupied = False
        self.vehicle = None
    
    @abstractmethod
    def can_park(self,vehicle):
        pass

    def can_park_vehicle(self,vehicle):
        if self.can_park(vehicle):
            self.is_occupied =  True
            self.vehicle = vehicle
            return self

    def unpark_vehicle(self):
        if self.is_occupied:
                print(f"Unparked vehicle with Registration Number: {self.vehicle.registration_number} and Color: {self.vehicle.colour}")
                self.is_occupied =  False
                self.vehicle = None
        else:
            print('Invalid Ticket')
    

class TruckSlot(Slot):

    def can_park(self, vehicle):
        return 'TRUCK' == vehicle.type
        
class BikeSlot(Slot):

    def can_park(self, vehicle):
        return 'BIKE' == vehicle.type

class CarSlot(Slot):

    def can_park(self, vehicle):
        return 'CAR' == vehicle.type

class ParkingFloor:
    def __init__(self,floor_no, slots) -> None:
        self.floor_no = floor_no
        self.slots = slots
    
    def find_available_slot(self,vehicle):
        for slot in self.slots:
            if not slot.is_occupied and slot.can_park_vehicle(vehicle):
                return slot
        return None
    
    def display_occupied_slots(self,type):
        return [ str(slot.number) for slot in self.slots if slot.check_occupied(type)]

    def display_free_slots(self,type):
        return [ str(slot.number) for slot in self.slots if slot.is_free(type)]

    def display_free_count(self,type):
        free_count = 0

        for slot in self.slots:
            if slot.is_free(type):
                free_count += 1
        return free_count
        

class ParkingLot:
    def __init__(self,lot_id,no_floors,no_of_slots) -> None:
        self.lot_id = lot_id
        self.floors = [ParkingFloor(floor_no + 1, self.build_slots(no_of_slots)) for floor_no in range(no_floors) ]
        
    def build_slots(self, no_of_slots):
        slots = []
        if no_of_slots >= 1:
            slots.append(TruckSlot(1))
        
        if no_of_slots >= 2:
           slots.append(BikeSlot(2))
        
        if no_of_slots >= 3:
            slots.append(BikeSlot(3))
        
        for n in range(4,no_of_slots+1):
            slots.append(CarSlot(n))
        return slots

    def park_vehicle(self,vehicle):
        
        for floor in self.floors:
            slot = floor.check_parking(vehicle)
            if slot:
                print(f"Parked vehicle. Ticket ID: {self.lot_id}_{floor.floor_no}_{slot.number}")
                return True
        print('Parking Lot Full')
        return False

    def unpark_vehicle(self, ticket_id):
        try:
            parking_lot_id, floor_no, slot_no = ticket_id.split('_')
            floor = self.floors[int(floor_no) - 1]
            floor.slots[int(slot_no) - 1].unpark_vehicle()
        except (IndexError, ValueError):
            print('Invalid Ticket')
    
    def display(self, display_type, vehicle_type):
        for floor in self.floors:
            if display_type == 'free_count':
                count = floor.display_free_count(vehicle_type)
                print(f"No. of free slots for {vehicle_type} on Floor {floor.floor_no}: {count}")
            elif display_type == 'free_slots':
                free_slots = floor.display_free_slots(vehicle_type)
                print(f"Free slots for {vehicle_type} on Floor {floor.floor_no}: {','.join(free_slots)}")
            elif display_type == 'occupied_slots':
                occupied_slots = floor.display_occupied_slots(vehicle_type)
                print(f"Occupied slots for {vehicle_type} on Floor {floor.floor_no}: {','.join(occupied_slots)}")