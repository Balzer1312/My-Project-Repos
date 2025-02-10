
import os
import json

class AccountService:
    bankAccounts={}
    currentFile= os.path.dirname(__file__)
    jsonFile= os.path.join(currentFile, 'BankAccounts.json')

    @staticmethod
    def loadAccounts():
        if os.path.exists(AccountService.jsonFile):
            try:
                with open(AccountService.jsonFile, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    for iban, accountData in data.items():
                        AccountService.bankAccounts[iban] = BankAccount(
                            accountData['Name'], iban, accountData['Kontostand']
                        )
                print('Konten erfolgreich geladen.')
            except Exception as e:
                print(f'Fehler beim Laden der Kontodaten: {e}')
        else:
            print('Keine vorhandene JSON-Datei gefunden. Neue Datei wird erstellt.')
    
    @staticmethod
    def createAccount(name, iban, balance):
        if iban not in AccountService.bankAccounts:
            AccountService.bankAccounts[iban] = BankAccount(name, iban, balance)
            AccountService.updateAccounts()
            print(f'Konto von {name} mit dem IBAN {iban} wurde erstellt.')
            AccountService.loadAccounts()
        else:
            print('Dieses Konto existiert bereits.')

    @staticmethod
    def deleteAccount(iban):
        iban = iban.strip()
        if iban in AccountService.bankAccounts:
            del AccountService.bankAccounts[iban]
            with open(AccountService.jsonFile, 'w', encoding='utf-8') as file:
                data_to_save = {
                    iban: {
                        'Name': account.name,
                        'IBAN': account.iban,
                        'Kontostand': account.balance
                    }for iban, account in AccountService.bankAccounts.items()    
                }
                json.dump(data_to_save, file, indent=4, ensure_ascii=False)
                

            print(f'Konto mit der IBAN Nummer {iban} wurde gelöscht.')
        else:
            print('Konto mit dieser IBAN existiert nicht.')

    @staticmethod
    def showOneAccount(iban):
        if iban in AccountService.bankAccounts:
            accountData=AccountService.bankAccounts[iban].getAccount()
            print(accountData)
        else:
            print('Dieses Konto existiert nicht.')

    @staticmethod
    def showallAccounts():
        if AccountService.bankAccounts:
            for accounts in AccountService.bankAccounts.values():
                print(accounts.getAccount())
        else:
            print('Keine Konten gefunden.')

    @staticmethod
    def updateAccounts():
        try:
            if os.path.exists(AccountService.jsonFile):
                with open(AccountService.jsonFile, 'r', encoding='utf-8') as file:
                    updateData = json.load(file)
            else:
                updateData = {}

            for iban, account in AccountService.bankAccounts.items():
                updateData[iban] = {
                    'Name': account.name,
                    'IBAN': account.iban,
                    'Kontostand': account.balance
                }

            with open(AccountService.jsonFile, 'w', encoding='utf-8') as file:
                json.dump(updateData, file, indent=4)

            print('Daten erfolgreich gespeichert.')
            AccountService.loadAccounts()
        except Exception as e:
            print(f'Fehler beim Speichern der Daten: {e}')

class BankAccount:
    
    def __init__(self,name,iban,balance):
        self.name = name
        self.iban = iban
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount} € wurden eingezahlt. Neuer Kontostand: {self.balance} €.')
            AccountService.bankAccounts[self.iban] = self
            AccountService.updateAccounts()
        else:
            print('Dein Konto hat zu wenig deckung.')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'{amount} € wurden abgehoben. Neuer Kontostand: {self.balance} €.')
            AccountService.updateAccounts()
        elif amount > self.balance:
            print('Nicht genügend Guthaben!')
        else:
            print('Dein Konto hat zu wenig deckung.')

    def getAccount(self):
        return (f'\nKonto:\nName: {self.name}\nIBAN: {self.iban}\nKontostand: {self.balance}\n'+'x'*40+'\n')

    
    