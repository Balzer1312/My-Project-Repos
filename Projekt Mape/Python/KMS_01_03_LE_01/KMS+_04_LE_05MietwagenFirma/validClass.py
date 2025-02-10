from adminRentClass import RentManager
import re

class Validor:

########### Kunden Valedierung ###################
    @staticmethod
    def validID(record):
        customerIDs= [customer['customerID'] for customer in RentManager.customerList]
        if not str(record['customerID']).isdigit() or record['customerID'] in str(customerIDs):
                return False
        else:
            return True
        
    # E-Mail Validierung        
    @staticmethod
    def validEmail(record):
        
        # Einfacher Ausdruck für die E-Mail Validierung
        emailPattern = (
            r'^[a-zA-Z0-9](?!.*--)(?!.*\.\.)[a-zA-Z0-9._%+-]*[a-zA-Z0-9]'  # Lokaler Teil
            r'@[a-zA-Z0-9](?!.*--)[a-zA-Z0-9.-]*[a-zA-Z0-9]\.[a-zA-Z]{2,}$'  # Domäne
        )
        
        # Match mit regulärem Ausdruck
        if re.match(emailPattern, record['email']):
            return True  
        else:
            return False 

#############  Fahrzeug Valedierung ####################
        
    @staticmethod
    def validVehicleID(record):
        vehicleIDs= [vehicle['serialID'] for vehicle in RentManager.vehicleList]
        if not str(record['serialID']).isdigit() or record['serialID'] in str(vehicleIDs):
                return False
        else:
            return True
        
    @staticmethod
    def valiedPrice(record):
         
        print(record)
        pricePattern = r'^\d+(\.\d{1,2})?$'  # Preisformat: Ganzzahl oder Zahl mit bis zu 2 Dezimalstellen
        price = record.get('rentalPrice')  # Hole den Preis aus dem Record

        if price and re.match(pricePattern, str(price)):  # Überprüfung
            return True
        else:
            return False