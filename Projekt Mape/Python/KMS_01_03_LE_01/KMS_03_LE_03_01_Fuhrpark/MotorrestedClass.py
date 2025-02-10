import os
import json
from VehicleClass import Vehicle


class Motorrested(Vehicle):
    currentJsonFuelPos=os.path.dirname(__file__)
    fuelJsonList= os.path.join(currentJsonFuelPos, 'fuelData.json')

    def __init__(self, type, color, model, brand, mark, fuel, consumption, mileage):
        super().__init__(type, color, model, brand)
        self.mark = mark
        self.fuel=fuel               
        self.consumption = consumption 
        self.mileage = mileage   

    @classmethod
    def refuelJsonData(cls):
        with open(Motorrested.fuelJsonList, 'r') as file:
            data = json.load(file)
            return data
    
    def refuel(self, year, month, fuelType, amount):

        with open(Motorrested.fuelJsonList, 'r') as file:
            data = json.load(file)

        data["refuels"][year][month][fuelType] += amount

        with open(Motorrested.fuelJsonList,'w') as file:
            json.dump(data,file, indent=4)

    
class Car(Motorrested):
    def __init__(self, color, model, brand, mark, fuel, consumption, mileage, doors):
        super().__init__('Car', color, model, brand, mark, fuel, consumption, mileage)
        self.doors = doors
    
    def __str__(self):
        return (f'Type: PKW\n{super().__str__()} Kennzeichen: {self.mark}\n Treibstoff: {self.fuel}\n Verbrauch: {self.consumption}L/100km\n Kilometerstand: {self.mileage}km\n Türen: {self.doors}\n')
    
class Motorcycle(Motorrested):
    def __init__(self, color, model, brand, mark, fuel, consumption, mileage, gears):
        super().__init__('Motorcycle', color, model, brand, mark, fuel,consumption, mileage)
        self.gears = gears

    def __str__(self):
        return (f'Type: Motorrad\n{super().__str__()} Kennzeichen: {self.mark}\n Treibstoff: {self.fuel}\n Verbrauch: {self.consumption}L/100km\n Kilometerstand: {self.mileage}km\n Gänge: {self.gears}\n')  

class Truck(Motorrested):
    def __init__(self, color, model, brand, mark, fuel, consumption, mileage, loadingWeight):
        super().__init__('Truck', color, model, brand, mark, fuel, consumption, mileage)
        self.loadingWeight = loadingWeight

    def __str__(self):
        return (f'Type: LKW\n{super().__str__()} Kennzeichen: {self.mark}\n Treibstoff: {self.fuel}\n Verbrauch: {self.consumption}L/100km\n Kilometerstand: {self.mileage}km\n Max Traglast: {self.loadingWeight}\n')  