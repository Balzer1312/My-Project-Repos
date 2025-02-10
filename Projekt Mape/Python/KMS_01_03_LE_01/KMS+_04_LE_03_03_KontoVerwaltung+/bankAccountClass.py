



class BankAccount:
    
    def __init__(self,userid,iban,name,balance):
        self.userid=userid
        self.iban = iban
        self.name = name
        self.balance = balance

    def __str__(self):
        return (f'Bank Konto:\nID: {self.userid}\n Name: {self.name}\n IBAN: {self.iban}\n Kontostand: {self.balance}\n')
    
    @staticmethod
    def accountObjFactory(record):   
        return BankAccount(userid=record['userid'],iban=record['iban'],name=record['name'], balance=record['balance'])
           