

from bankmanager import BankManager




class Validor:

    
    @staticmethod
    def addValidor(record):
        
        for user in BankManager.allAccountslist:
            # Überprüfung der UserID
            if user['userid'] == int(record['userid']):
                return f'Die UserID {record['userid']} existiert bereits!'
            
            # Überprüfung der IBAN
            if user['iban'] == record['iban']:
                return f'Die IBAN {record['iban']} existiert bereits!'
        return 'Valid'
    
    @staticmethod
    def deleteByIdCheck(id):

        for user in BankManager.allAccountslist:
            # Überprüfung der UserID
            if user['userid'] == int(id):
                return True
            
        return f'Die UserID {id} existiert nicht!'
