import tkinter as tk
import os
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk

from DBUtili import DBManager
from validor import Validor
from bankmanager import BankManager

class UserDashboard:
    bankManager=BankManager()

    def __init__(self,mainFrame):
        self.mainFrame = mainFrame

        
############# Interface widgets Funktionen ###############
    #Widgets Für Willkomen Nachricht
    def displayWelcomeMessage(self):
        self.welcomeLabel = ctk.CTkLabel(self.mainFrame, text='Wilkommen zur Konto Verwaltung', font=('Arial', 20))
        self.welcomeLabel.pack(pady=20)

    # Enfernt alle nicht die nicht 
    def removeAllWidgets(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

############# Interface für Konten Anzeigen ###############

    #Widgets Für Account anzeigen
    def accountToDisplay(self):
        self.removeAllWidgets()

        filterLabel = ctk.CTkLabel(self.mainFrame, text='Bank Konten Anzeigen:', font=('Arial', 14))
        filterLabel.pack(pady=10)

       # Combobox für die Auswahl
        self.selectionVar = ctk.StringVar()
        comboBox = ctk.CTkComboBox(self.mainFrame,variable=self.selectionVar ,values=['Alle anzeigen', 'Einen anzeigen'],command=self.selectionChoice)
        comboBox.pack(pady=10)
        comboBox.set('Alle anzeigen') 
        
        self.idInputLabel=ctk.CTkLabel(self.mainFrame,text='Geben Sie eine ID ein:')
        self.idInputLabel.pack_forget()

        self.idInput=ctk.CTkEntry(self.mainFrame, placeholder_text='Bitte ID eingeben:')
        self.idInput.pack_forget()

        self.showButton=ctk.CTkButton(self.mainFrame,text='Anzeigen')
        self.showButton.pack(side='bottom',pady=10)
        self.selectionChoice('Alle anzeigen')
    # Widget Logik für comboBox und ShowButton
    def selectionChoice(self,choice):
        if choice == 'Einen anzeigen':
            self.idInputLabel.pack(pady=10)  # Zeigt das Label an
            self.idInput.pack(pady=10)
            self.showButton.configure(command=lambda:self.showAccontWindow(self.bankManager.showOneAccount(self.idInput.get()))) 
        else:
            self.idInputLabel.pack_forget()  # Versteckt das Label
            self.idInput.pack_forget()
            self.showButton.configure(command=lambda:self.showAccontWindow(self.bankManager.showAllAccount()))
    # Fenster für Ausgabe 
    def showAccontWindow(self,showData):
        
        accountWindow = ctk.CTkToplevel(self.mainFrame)
        accountWindow.title('Kontodaten anzeigen')
        accountWindow.geometry('500x400')
        
        accountWindow.lift()
        accountWindow.attributes('-topmost', True)
        accountWindow.resizable(False, False)


         # Scrollbarer Rahmen
        scrollableFrame = ctk.CTkScrollableFrame(accountWindow, width=380, height=300)
        scrollableFrame.pack(pady=10, padx=10, fill='both', expand=False)

        if isinstance(showData, list):
            for obj in showData:
                textLabel = ctk.CTkLabel(scrollableFrame, text=str(obj), justify='left', font=('Arial', 12))
                textLabel.pack(anchor='w', pady=5, padx=10)
        else:
            textLabel = ctk.CTkLabel(scrollableFrame,text=str(showData),justify='left',font=('Arial', 12))
            textLabel.pack(anchor='w', pady=5, padx=10)
            
            
        # Schließen-Button
        closeButton = ctk.CTkButton(accountWindow, text='Schließen', command=accountWindow.destroy)
        closeButton.pack(pady=10)


############## Interface für Konto Hinzufügen #############
    #Widgets Für Konto Anlegen
    def addDataDashboard(self):
        self.removeAllWidgets()
        
        taskLabel = ctk.CTkLabel(self.mainFrame, text='Konto Anlegen:', font=('Arial', 12))
        taskLabel.pack(pady=5, padx=10)


        #Echtzeit überwachung der Inputs
        self.userIdVar = ctk.StringVar()
        self.ibanVar = ctk.StringVar()
        self.nameVar = ctk.StringVar()
        self.balanceVar = ctk.StringVar()

        
        self.errorLabel = ctk.CTkLabel(self.mainFrame, text='', font=('Arial', 10), text_color='red',bg_color='transparent')
        self.errorLabel.pack(pady=5, padx=10)


        # UserID Label und Entry
        userIdLabel = ctk.CTkLabel(self.mainFrame, text='UserID:', font=('Arial', 12))
        userIdLabel.pack(pady=5, padx=10)
        self.userIdEntry = ctk.CTkEntry(self.mainFrame,textvariable=self.userIdVar)
        self.userIdEntry.pack(pady=5, padx=10)

        # IBAN Label und Entry
        ibanLabel = ctk.CTkLabel(self.mainFrame, text='IBAN:', font=('Arial', 12))
        ibanLabel.pack(pady=5, padx=10)
        self.ibanEntry = ctk.CTkEntry(self.mainFrame,textvariable=self.ibanVar)
        self.ibanEntry.pack(pady=5, padx=10)

        # Name Label und Entry
        nameLabel = ctk.CTkLabel(self.mainFrame, text='Name:', font=('Arial', 12))
        nameLabel.pack(pady=5, padx=10)
        self.nameEntry = ctk.CTkEntry(self.mainFrame,textvariable=self.nameVar)
        self.nameEntry.pack(pady=5, padx=10)

        # Balance Label und Entry
        balanceLabel = ctk.CTkLabel(self.mainFrame, text='Kontostand:', font=('Arial', 12))
        balanceLabel.pack(pady=5, padx=10)
        self.balanceEntry = ctk.CTkEntry(self.mainFrame,textvariable=self.balanceVar)
        self.balanceEntry.pack(pady=5, padx=10)
        
        self.saveButton = ctk.CTkButton(self.mainFrame, text='Speichern',command=self.saveAccount,state='disabled')
        self.saveButton.pack(pady=10)

   
        self.userIdVar.trace_add('write', self.inputMonitoring)
        self.nameVar.trace_add('write',self.inputMonitoring)
        self.ibanVar.trace_add('write',self.inputMonitoring)
        self.balanceVar.trace_add('write', self.inputMonitoring)

    #Input Überwachung
    def inputMonitoring(self,*args):

        #Input Überwachung für ID
        try:
            userID = self.userIdVar.get().strip()
            if not userID.isdigit() or int(userID) <= 0:
                self.saveButton.configure(state='disabled')
                raise ValueError
            else:
                self.errorLabel.configure(text='')
        except ValueError:
            self.errorLabel.configure(text='UserID muss eine ganze Zahl sein!')
            self.saveButton.configure(state='disabled')
            return
        

        # Input überwachung für Iban
        iban = self.ibanVar.get().strip()
        if not self.ibanVar.get().strip():
            self.saveButton.configure(state='disabled')
            return
        if not iban[:2].isalpha() or not iban[2:].isdigit() or not (2 <= len(iban[:3]) <= 3): # Überprüfung, ob die ersten 2-3 Zeichen Buchstaben sind
            self.errorLabel.configure(text='IBAN muss mit 2-3 Buchstaben beginnen!')
            self.saveButton.configure(state='disabled')
            return
        else:
            self.errorLabel.configure(text='')
        
        # Input überwachung für namen
        if not self.nameVar.get().strip():
            self.saveButton.configure(state='disabled')
            return   
        if any(char.isdigit() for char in self.nameVar.get()):  # Überprüfung auf Zahlen im Namen
            self.errorLabel.configure(text='Name darf keine Zahlen enthalten!')
            self.saveButton.configure(state='disabled')
            return
        else:
            self.errorLabel.configure(text='')
        # Input überwachung für Kontostant
        try:
            if self.balanceVar.get().strip():
                balance = float(self.balanceVar.get())
                if round(balance, 2) != balance:
                    raise ValueError
            else:
                self.saveButton.configure(state='disabled')
                return
        except ValueError:
            self.errorLabel.configure(text='Balance muss ein 2-stelliger sein!')
            self.saveButton.configure(state='disabled')
            return

        # Keine Fehler und alle Felder befüllt -> Button aktivieren
        self.errorLabel.configure(text='')
        self.saveButton.configure(state='normal')

    #Account wird der DB übertragen
    def saveAccount(self,*args):
        #Mapping 
        record = {
        'userid': self.userIdVar.get().strip(),
        'iban': self.ibanVar.get().strip(),
        'name': self.nameVar.get().strip(),
        'balance': self.balanceVar.get().strip(),
    }
        #Valedierung für Existens der ID und IBAN 
        result=Validor.addValidor(record)
        print(f'{result}')
        if result != 'Valid':
            self.errorLabel.configure(text= str(result))
            return
        
        dbResponse = DBManager.insertDB(record)
        if dbResponse:
            messagebox.showinfo('Erfolg', 'Konto erfolgreich angelegt!')
            self.bankManager.getDataFromDB()
        else:
            messagebox.showerror('Datenbankfehler', 'Die Daten wurden nicht übertragen')

        
############### Konto enfernen #################

    # Haupt-Interface
    def deletDataDashboard(self):

        self.removeAllWidgets()

        headlineLabel = ctk.CTkLabel(self.mainFrame, text='Bank Konto Löschen', font=('Arial', 16))
        headlineLabel.pack(pady=10)

        self.errorIDLabel = ctk.CTkLabel(self.mainFrame, text='', font=('Arial', 10), text_color='red',bg_color='transparent')
        self.errorIDLabel.pack(pady=5, padx=10)

        self.idCheckVar = ctk.StringVar()
        
        self.idCheckInputLabel=ctk.CTkLabel(self.mainFrame,text='Geben Sie die Konto ID ein zum Löschen:', font=('Arial', 14))
        self.idCheckInputLabel.pack(pady=10)
        self.idCheckInput=ctk.CTkEntry(self.mainFrame, placeholder_text='Bitte ID eingeben:',textvariable=self.idCheckVar)
        self.idCheckInput.pack(pady=10)

        self.deletButton = ctk.CTkButton(self.mainFrame, text='Löschen', command=self.deletAccount,state='disabled')
        self.deletButton.pack(pady=10)

        self.idCheckVar.trace_add('write', self.inputCheck)

    #Input Überwachung
    def inputCheck(self,*args):

        #Input Überwachung für ID
        try:
            deletID = self.idCheckVar.get().strip()
            if not deletID.isdigit() or int(deletID) <= 0:
                self.deletButton.configure(state='disabled')
                self.errorIDLabel.configure(text='UserID muss eine ganze Zahl sein!')
                return
            else:
                self.errorIDLabel.configure(text='')
        except ValueError:
            self.deletButton.configure(state='disabled')
            return
            
        self.deletButton.configure(state='normal')

    # Löschen des Kontos in der DB
    def deletAccount(self,*args):
        
        deletID = self.idCheckVar.get().strip()
        result=Validor.deleteByIdCheck(deletID)
        if result is True:
            DBManager.deletWereUser(deletID)
            messagebox.showinfo('Erfolg', 'Konto erfolgreich gelöscht!')
            self.bankManager.getDataFromDB()
            return
        else:
            self.errorIDLabel.configure(text=result)

############## Konto verwahltung für Einzahlen Auszahlen #####################
        
    
    def accountManagerDashboard(self):

        self.removeAllWidgets()

        taskLabel = ctk.CTkLabel(self.mainFrame, text='Kontoverwaltung', font=('Arial', 16))
        taskLabel.pack(pady=10)

        self.accountIdVar = ctk.StringVar()
        accountIdLabel = ctk.CTkLabel(self.mainFrame, text='Konto-ID:', font=('Arial', 12))
        accountIdLabel.pack(pady=5)
        self.accountIdEntry = ctk.CTkEntry(self.mainFrame, width=200,textvariable=self.accountIdVar)
        self.accountIdEntry.pack(pady=5)

        self.amountVar = ctk.StringVar()
        amountLabel = ctk.CTkLabel(self.mainFrame, text='Betrag:', font=('Arial', 12))
        amountLabel.pack(pady=5)
        self.amountEntry = ctk.CTkEntry(self.mainFrame, width=200,textvariable=self.amountVar)
        self.amountEntry.pack(pady=5)

        self.depositButton = ctk.CTkButton(self.mainFrame, text='Geld einzahlen',command=lambda: self.handleTransaction('deposit'))
        self.depositButton.pack(pady=10)

        self.withdrawButton = ctk.CTkButton(self.mainFrame, text='Geld abheben',command=lambda: self.handleTransaction('withdraw'))
        self.withdrawButton.pack(pady=10)

        self.balanceButton = ctk.CTkButton(self.mainFrame, text='Kontostand anzeigen',command=lambda:self.bankManager.showOneAccount(self.accountIdEntry.get()))
        self.balanceButton.pack(pady=10)

        # Rückgabe einer Statusmeldung
        self.errorStatusLabel = ctk.CTkLabel(self.mainFrame, text='', font=('Arial', 12), text_color='red')
        self.errorStatusLabel.pack(pady=5)

        self.accountIdVar.trace_add('write', self.inputCheckForAccManag)
        self.amountVar.trace_add('write', self.inputCheckForAccManag)

    #Input Überwachung
    def inputCheckForAccManag(self,*args):

        accountID = self.accountIdVar.get().strip()
        amount = self.amountVar.get().strip()
        

        if not accountID.isdigit() or int(accountID) <= 0:
            self.depositButton.configure(state='disabled')
            self.withdrawButton.configure(state='disabled')
            self.errorStatusLabel.configure(text='Konto-ID muss eine gültige Zahl sein!')
            return
        else:
            self.errorStatusLabel.configure(text='')

        # Überprüfung des Betrags
        
        try:
            amountFloat = float(amount)
            if amountFloat <= 0:
                raise ValueError
        except ValueError:
            self.depositButton.configure(state='disabled')
            self.withdrawButton.configure(state='disabled')
            self.errorStatusLabel.configure(text='Betrag muss eine gültige Zahl größer als 0 sein!')
            return
        
        self.depositButton.configure(state='normal')
        self.withdrawButton.configure(state='normal')
        self.errorStatusLabel.configure(text='')
   
     # Kontostand ändern
    def handleTransaction(self, action):
        try:
            accountID = int(self.accountIdVar.get().strip())
            amount = float(self.amountVar.get().strip())
            
            if action == 'deposit':
                response = DBManager.depositAccount(accountID, amount)
            elif action == 'withdraw':
                response = DBManager.withdrawAccount(accountID, amount)

            # Rückmeldung anzeigen
            if 'erfolgreich' in response.lower():
                self.errorStatusLabel.configure(text=response, text_color='green')
                self.bankManager.getDataFromDB()
            else:
                self.errorStatusLabel.configure(text=response, text_color='red')

        except ValueError:
            self.errorStatusLabel.configure(
                text='Ungültige Eingabe. Bitte überprüfen Sie die Konto-ID und den Betrag.',
                text_color='red'
            )

    def accountsToCSV(self):

        self.removeAllWidgets()

        memberTypeLabel = ctk.CTkLabel(self.mainFrame, text='Bankkontos als CSV datei exportieren:',font=('Arial', 16))
        memberTypeLabel.pack(pady=10)

        exportToCsvButton= ctk.CTkButton(self.mainFrame,text='Exportieren',command=self.bankManager.bankaccountToCsv)
        exportToCsvButton.pack(pady=10,padx=10)

    
        