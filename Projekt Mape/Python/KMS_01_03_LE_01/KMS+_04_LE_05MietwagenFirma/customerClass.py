




class Customer:

    def __init__(self,customerID,name,address,email,phoneNumber):
        self.customerID = customerID
        self.name = name
        self.address=address
        self.email = email
        self.phoneNumber = phoneNumber


    @classmethod
    def getCustomerMapping(cls):
         
        customerFields = {
            'Mitglieds-ID': 'customerID',
            'Name': 'name',
            'Adresse': 'address',
            'E-Mail': 'email',
            'tel.: (+43 12345...)': 'phoneNumber',
        }
        return customerFields


    @staticmethod
    def createCustomerObj(record):

        return Customer(
            customerID=record['customerID'],
            name=record['name'],
            address=record['address'],
            email=record['email'],
            phoneNumber=record['phoneNumber']
        )

    def __str__(self):
            return (f'Kunde:\n  Kunden ID: {self.customerID}\n  Name: {self.name}\n  Adresse: {self.address}\n  Email: {self.email}\n  Tel.: {self.phoneNumber}')