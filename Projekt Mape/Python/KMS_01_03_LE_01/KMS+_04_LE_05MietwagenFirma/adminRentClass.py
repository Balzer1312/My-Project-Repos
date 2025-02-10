from tkinter import messagebox
from  DBUtilis import DBManager

from rentClass import Rentals
from customerClass import Customer
from vehicleClass import Vehicle


class RentManager:

    customerList=[]
    vehicleList=[]
    rentList=[]
###############  Lade Daten aus der DB ######################

    # Lade alle Kunden aus der DB 
    @classmethod
    def loadCustomers(cls):
        query = 'SELECT customerID, name, address, email, phoneNumber FROM customers'
        customers = DBManager.fetchData(query)

        if not customers:
            messagebox.showerror('Fehler', 'Keine Kunden gefunden.')
            return
        
        for customer in customers:
            cls.customerList.append({'customerID': customer[0], 'name': customer[1], 'address': customer[2], 'email': customer[3], 'phoneNumber': customer[4]})

    # Lade alle Fahrezuge aus der DB 
    @classmethod
    def loadVehicle(cls):

        query = 'SELECT serialID, brand, model, rentalPrice FROM vehicles'
        vehicles=DBManager.fetchData(query)

        if not vehicles:
            messagebox.showerror('Fehler', 'Keine Fahrzeuge gefunden.')
        
        for vehicle in vehicles:
            cls.vehicleList.append({'serialID': vehicle[0], 'brand': vehicle[1], 'model': vehicle[2], 'rentalPrice': vehicle[3]})

    # Lade alle Verlei einträge aus der DB             
    @classmethod
    def loadRentals(cls):

        query = '''
        SELECT r.rentalID, r.customerID, r.serialID, r.rentalDate, r.returnDate, 
               c.name AS customerName, v.brand AS vehicleBrand, v.model AS vehicleModel
        FROM rentals r
        JOIN customers c ON r.customerID = c.customerID
        JOIN vehicles v ON r.serialID = v.serialID
        '''
        
        rentals = DBManager.fetchData(query)
        
        for rental in rentals:
            cls.rentList.append ({
            'rentalID': rental[0],                 
            'customerID': rental[1],               
            'customerName': rental[5],             
            'serialID': rental[2],                 
            'vehicleDetails': f'{rental[6]} {rental[7]}',     # Fahrzeugdetails (Marke + Modell)
            'rentalDate': rental[3],               
            'returnDate': rental[4]
            })
        

################# Ausgabe Funktionen für Display darstellung ###############

## Führ mehrere Datensätze:

 
    @classmethod
    def showAllRentals(cls):

        rentInfos=[Rentals.createRentalObj(rent)for rent in cls.rentList]
        return rentInfos
    
    
    @classmethod
    def showAllCustomers(cls):
        
        customerInfos = [ Customer.createCustomerObj(customer) for customer in cls.customerList]
        return customerInfos
    

    @classmethod
    def showAllVehicle(cls):

        vehicleInfos=[Vehicle.createVehicleObj(vehicle)for vehicle in cls.vehicleList]
        return vehicleInfos
    

## Für einzelnen Datensatz:

    @classmethod
    def getCustomerById(cls, customerID):
        for customer in cls.customerList:
            if customer['customerID'] == customerID:
                customerObj=Customer.createCustomerObj(customer)
                return customerObj
        return None

    @classmethod
    def getVehicleById(cls, serialID):
        for vehicle in cls.vehicleList:
            if vehicle['serialID'] == serialID:
                vehicleObj=Vehicle.createVehicleObj(vehicle)
                return vehicleObj
        return None

    @classmethod
    def getRentalById(cls, rentalID):
        for rental in cls.rentList:
            if rental['rentalID'] == rentalID:
                rentalObj=Rentals.createRentalObj(rental)
                return rentalObj
        return None
    

        
########### Vermitungs eintrag Hinzufügen #############

    @classmethod
    def getNextRentalID(cls):
        
        if not cls.rentList:  # Wenn die Liste leer ist
            return 1  # Starte mit 1, da keine Eintraege vorhanden sind

        # Extrahiere alle bestehenden rentalIDs aus der rentList
        rentalIDs = [rental['rentalID'] for rental in cls.rentList]

        # Bestimme die maximale ID und erhoehe sie um 1
        nextID = max(rentalIDs) + 1
        return nextID


    @classmethod
    def registerRental(cls,record):

        nextRentalId = cls.getNextRentalID()

        # Neuer Eintrag erstellen
        newRental = {
            'rentalID': nextRentalId,
            'customerID': record['customerID'],
            'serialID': record['serialID'],
            'rentalDate': record['rentalDate'],
            'returnDate': None  # Rueckgabedatum ist zunächst leer
        }
        success = DBManager.insertRental(newRental)
        if success:
            messagebox.showinfo('Erfolg', 'Mieteintrag wurde erfolgreich hinzugefügt.')
            cls.loadRentals()
        else:
            messagebox.showerror('Fehler', 'Mieteintrag konnte nicht hinzugefügt werden.')