
class Vehicle:
    def __init__(self, type, color, model, brand):
        self.type = type
        self.color = color
        self.model = model
        self.brand = brand

    def vehicleInfo(self):
        
        print(f"Typ: {self.type}, Farbe: {self.color}, Modell: {self.model}, Marke: {self.brand}")

class Motorrested(Vehicle):
    def __init__(self, type, color, model, brand, mark, consumption, mileage):
        super().__init__(type, color, model, brand)
        self.mark = mark               
        self.consumption = consumption 
        self.mileage = mileage      
    

class Car(Motorrested):
    def __init__(self, color, model, brand, mark, consumption, mileage, doors):
        super().__init__("Car", color, model, brand, mark, consumption, mileage)
        self.doors = doors
    
    def pkwInfo(self):
        print(f"Typ: PKW, Farbe: {self.color}, Modell: {self.model}, Marke: {self.brand}, Verbrauch{self.consumption}l, Km-stand: {self.mileage}km,Türen: {self.doors}")

class Motorcycle(Motorrested):
    def __init__(self, color, model, brand, mark, consumption, mileage, gears):
        super().__init__("Motorcycle", color, model, brand, mark, consumption, mileage)
        self.gears = gears
    
    def motorcycleInfo(self):
        print(f"Typ: Motorrad, Farbe: {self.color}, Modell: {self.model}, Marke: {self.brand}, Verbrauch: {self.consumption}l, Km-stand: {self.mileage}km, Gangezahl: {self.gears}")

class Truck(Motorrested):
    def __init__(self, color, model, brand, mark, consumption, mileage, loadingWeight):
        super().__init__("Truck", color, model, brand, mark, consumption, mileage)
        self.loadingWeight = loadingWeight
    
    def truckInfo(self):
        print(f"Typ: LKW, Farbe: {self.color}, Modell: {self.model}, Marke: {self.brand}, Verbrauch: {self.consumption}l, Km-stand: {self.mileage} km, Nutzlast: {self.loadingWeight}t")

class Bicycle(Vehicle):
    def __init__(self, color, model, brand, gears):
        super().__init__("Bicycle", color, model, brand)
        self.gears = gears
    
    def bicycleInfo(self):
        print(f"Typ: Fahrrad, Farbe: {self.color}, Modell: {self.model}, Marke: {self.brand}, Gangzahl: {self.gears}")


if __name__ == "__main__":
 
    car = Car("Schwarz", "C63", "Mercedes", "G-12345X", 12, 15000, 5)
    truck = Truck("Rot-Weiß","TGX","MAN", "G-12345Y",28.1,36200,19 )
    motorcycle = Motorcycle("Orange","EXC-250", "KTM","G-123X",4.54,2000,6)
    bicycle = Bicycle("orange","Myroon-Elite","KTM",12)

    print("\n\n---- PKW ----")
    car.pkwInfo()
    print("\n")

    print("\n\n---- LKW ----")
    truck.truckInfo()
    print("\n")

    print("\n\n---- Motorrad ----")
    motorcycle.motorcycleInfo()
    print("\n")

    print("\n\n---- Fahrrad ----")
    bicycle.bicycleInfo()
    print("\n")
