import os
import csv
from tkinter import messagebox

from DBUtili import DBManager
from bankAccountClass import BankAccount


class BankManager:

    currentCsvPos= os.path.dirname(__file__)
    bankAccountlistCSV= os.path.join(currentCsvPos, 'Bankkonto-Liste.csv') 

    allAccountslist=[]
    
############## Daten werden von DB geladen ###########
    def getDataFromDB(self):
        
        query='SELECT * FROM bankaccount'
        records=DBManager.fetchData(query) 
        if records:
            for row in records:
                id=row[0]

                if id not in [account['userid'] for account in self.allAccountslist]:
                    self.allAccountslist.append({'userid': id,'iban': row[1], 'name': row[2],'balance': row[3]}) 
        else:
            messagebox.showerror('Fehler', 'Keine Daten gefunden')
    
############## Bank Accounts Anzeigen ########################
    # Zeige alle Accounts
    def showAllAccount(self):
        
        showList=[]
        for account in self.allAccountslist:
            showData=BankAccount.accountObjFactory(account)
            showList.append(str(showData))
        return showList
    # Zeige einen gesuchten Account
    def showOneAccount(self,accountID):
        
        print(accountID)
        for account in self.allAccountslist:
            if int(account['userid'])==int(accountID):
                showData=BankAccount.accountObjFactory(account)
                return str(showData)
        return'Kein Account mit dieser ID Gefunden!'
            
############# Bank Konten zur CSV ######################
    def bankaccountToCsv(self):
       
        if not self.allAccountslist:
            messagebox.showerror('Fehler','Die Bankkonto liste ist leer. Kein Export möglich.')
            return
            
        
        try:
            with open(self.bankAccountlistCSV, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['UserID', 'IBAN', 'Name', 'Kontostand'])

                for account in self.allAccountslist:
                    writer.writerow([
                        account['userid'],
                        account['iban'],
                        account['name'],
                        account['balance']
                    ])


                messagebox.showinfo('Erfolg','CSV-Datei erfolgreich exportiert!')
            return 

        except Exception as e:
            messagebox.showerror('Fehler', f'Fehler beim Exportieren: {e}')
            return None