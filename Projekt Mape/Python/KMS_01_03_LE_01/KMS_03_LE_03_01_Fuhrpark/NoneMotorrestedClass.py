from VehicleClass import Vehicle


class NoneMotorrested(Vehicle):
    def __init__(self, type, color, model, brand,id):
        super().__init__(type, color, model, brand)
        self.id = id
    
class Bicycle(NoneMotorrested):
    def __init__(self, color, model, brand, id,gears):
        super().__init__('Bicycle', color, model, brand, id)
        self.gears = gears
            
    def __str__(self):
        return (f'Type: Fahrrad\n{super().__str__()} ID: {self.id}\n Gangzahl: {self.gears}\n')