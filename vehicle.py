class Vehicle:
    def __init__(self,type,reg_no,colour) -> None:
        self.type = type.upper()
        self.registration_number = reg_no
        self.colour = colour