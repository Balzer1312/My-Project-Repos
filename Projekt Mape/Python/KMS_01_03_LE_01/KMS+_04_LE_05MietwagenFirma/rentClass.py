class Rentals:

    def __init__(self, rentalID, customerID, customerName, serialID, vehicleDetails, rentalDate, returnDate):
        self.rentalID = rentalID
        self.customerID = customerID
        self.customerName = customerName  
        self.serialID = serialID
        self.vehicleDetails = vehicleDetails  
        self.rentalDate = rentalDate
        self.returnDate = returnDate



    @staticmethod
    def createRentalObj(record):

        return Rentals(
            rentalID=record['rentalID'],
            customerID=record['customerID'],
            customerName=record['customerName'],
            serialID=record['serialID'],
            vehicleDetails=record['vehicleDetails'],
            rentalDate=record['rentalDate'],
            returnDate=record['returnDate']
        )


    def __str__(self):
        return (
            f'Vermietung:\n'
            f'  Vermietung ID: {self.rentalID}\n'
            f'  Kunde ID: {self.customerID}\n'
            f'  Kundenname: {self.customerName}\n'
            f'  Fahrzeug (Seriennummer): {self.serialID}\n'
            f'  Fahrzeugdetails: {self.vehicleDetails}\n'
            f'  Mietdatum: {self.rentalDate}\n'
            f'  Rückgabedatum: {self.returnDate if self.returnDate else 'Noch nicht zurückgegeben'}'
        )