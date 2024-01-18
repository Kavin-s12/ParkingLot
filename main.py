from vehicle import Vehicle
from parking import ParkingLot

# class ParkingFunctions:
#     def create_parking_lot(self,lot_id,no_floors,no_of_slots):
#         return ParkingLot(lot_id,no_floors,no_of_slots)

#     def park_vehicle(self, parking , vehicle):
#         parking.park_vehicle(vehicle)
    
#     def unpark_vehicle(self, parking , floor_no, slot_no):
#         parking.unpark_vehicle(floor_no,slot_no)
            


if __name__ == '__main__':
    Parking = None
    while True:
        instruct = input().split(' ')

        if instruct[0].upper() == 'EXIT':
            break

        if instruct[0] == 'create_parking_lot':
            _, lot_id , no_floors , no_of_slots = instruct
            Parking = ParkingLot(lot_id,int(no_floors),int(no_of_slots))
            print(f"Created parking lot with {no_floors} floors and {no_of_slots} slots per floor")
        
        elif Parking:
            if instruct[0] == 'park_vehicle':
                _, type , reg_no , colour = instruct
                Parking.park_vehicle(Vehicle(type,reg_no,colour))
            
            elif instruct[0] == 'unpark_vehicle':
                Parking.unpark_vehicle(instruct[1])

            elif instruct[0] == 'display':
                _ , choice , type = instruct
                Parking.display(choice, type)
        else:
            print("No parking lot")
