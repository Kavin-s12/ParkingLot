from vehicle import vehicle
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
        
        elif instruct[0] == 'park_vehicle':
            _, type , reg_no , colour = instruct
            if Parking:
                Parking.park_vehicle(vehicle(type,reg_no,colour))
            else:
                print("No parking lot")
        
        elif instruct[0] == 'unpark_vehicle':
            _, floor_no , slot_no = instruct[1].split('_')
            
            if Parking:
                Parking.unpark_vehicle(int(floor_no), int(slot_no))
            else:
                print("No parking lot")
        
        elif instruct[0] == 'display':
            _ , choice , type = instruct
            if choice == 'free_count':
                Parking.display_free_count(type)
            elif choice == 'free_slots':
                Parking.display_free_slots(type)
            else:
                Parking.display_occupied_slots(type)
