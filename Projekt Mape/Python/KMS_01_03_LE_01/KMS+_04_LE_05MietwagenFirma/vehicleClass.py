





class Vehicle: 
    def __init__(self, serialID, brand, model, rentalPrice):
        self.serialID= serialID
        self.brand = brand
        self.model = model
        self.rentalPrice= rentalPrice

    @classmethod
    def getVehicleMapping(cls):
         
        vehicleFields = {
            'Serien Nummer (ID)': 'serialID',
            'Marke': 'brand',
            'Modell': 'model',
            'Preis': 'rentalPrice',
        }
        return vehicleFields


    @staticmethod
    def createVehicleObj(record):

        return Vehicle(
            serialID=record['serialID'],
            brand=record['brand'],
            model=record['model'],
            rentalPrice=record['rentalPrice']
        )

    def __str__(self):
        return (f'Fahrzeug:\n  Serien Nummer: {self.serialID}\n  Marke: {self.brand}\n  Modell: {self.model}\n  Mietpreis: {self.rentalPrice}') 