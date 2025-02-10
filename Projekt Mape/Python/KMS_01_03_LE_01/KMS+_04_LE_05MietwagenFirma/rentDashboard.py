from tkinter import messagebox
import customtkinter as ctk
from datetime import datetime

from adminRentClass import RentManager
from DBUtilis import DBManager
from customerClass import Customer
from validClass import Validor
from vehicleClass import Vehicle
from rentClass import Rentals

class RentDashboard:

    rentManager=RentManager()

    def __init__(self,mainFrame):
        self.mainFrame = mainFrame

    #Widgets Für Willkomen Nachricht
    def displayWelcomeMessage(self):
        self.welcomeLabel = ctk.CTkLabel(self.mainFrame, text='Wilkommen zur Konto Verwaltung', font=('Arial', 20))
        self.welcomeLabel.pack(pady=20)

    # Enfernt alle nicht die nicht 
    def removeAllWidgets(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

################### Dashboard für gesamte Verwaltungs Informationen ########################


    def selectInfoControl(self):
        
        self.removeAllWidgets()

        # Label für Auswahl
        filterLabel = ctk.CTkLabel(self.mainFrame, text='Verwaltungs Details Anzeigen:', font=('Arial', 14))
        filterLabel.pack(pady=10)

        # Auswahloptionen
        self.selectionVar = ctk.StringVar()
        comboBox = ctk.CTkComboBox(
            self.mainFrame,
            variable=self.selectionVar,
            values=['Gemietete Fahrzeuge', 'Alle Kunden', 'Alle Fahrzeuge'],
            command=self.selectionChoice
        )
        comboBox.pack(pady=10)
        comboBox.set('Gemietete Fahrzeuge')

        # Anzeigen-Button
        self.showButton = ctk.CTkButton(self.mainFrame, text='Anzeigen')
        self.showButton.pack(side='bottom', pady=10)

        # Standardauswahl
        self.selectionChoice('Gemietete Fahrzeuge')


    def selectionChoice(self, choice):
        
        actions = {
            'Gemietete Fahrzeuge': lambda: self.showButton.configure(
                command=lambda: self.showAllDataWindow('Gemietete Fahrzeuge', RentManager.showAllRentals)),
            'Alle Kunden': lambda: self.showButton.configure(
                command=lambda: self.showAllDataWindow('Alle Kunden', RentManager.showAllCustomers)),
            'Alle Fahrzeuge': lambda: self.showButton.configure(
                command=lambda: self.showAllDataWindow('Alle Fahrzeuge', RentManager.showAllVehicle))
        }

        # Aktion ausführen, falls vorhanden
        action = actions.get(choice)
        if action:
            action()


    def showAllDataWindow(self, title, getDataMethod):
        
        # Daten abrufen
        objData = getDataMethod()

        # Existierendes Datenfenster schließen
        if hasattr(self, 'dataWindow') and self.dataWindow is not None:
            self.dataWindow.destroy()

        # Neues Fenster erstellen
        self.dataWindow = ctk.CTkToplevel(self.mainFrame)
        self.dataWindow.title(title)
        self.dataWindow.geometry('400x300')
        self.dataWindow.resizable(False, False)

        # Titel
        ctk.CTkLabel(self.dataWindow, text=title, font=('Arial', 16)).pack(pady=10)

        # Scrollbarer Frame für die Datenanzeige
        frame = ctk.CTkScrollableFrame(self.dataWindow)
        frame.pack(pady=10, padx=10, fill='x', expand=False)

        # Alle Daten anzeigen
        for obj in objData:
            ctk.CTkLabel(frame, text=str(obj), anchor='w', justify='left', font=('Arial', 12)).pack(fill='x', padx=10, pady=10)

############### Dashboard für einzelne Informationen aus der Verwaltung #####################

    def selectSingleInfoControl(self):
        
        self.removeAllWidgets()

        # Label für Auswahl
        filterLabel = ctk.CTkLabel(self.mainFrame, text='Einzelne Details anzeigen:', font=('Arial', 14))
        filterLabel.pack(pady=10)

        # Dropdown-Menü
        self.selectionVar = ctk.StringVar()
        comboBox = ctk.CTkComboBox(
            self.mainFrame,
            variable=self.selectionVar,
            values=['Einzelner Kunde', 'Einzelnes Fahrzeug', 'Einzelner Verleih'],
            command=self.selectionChoice
        )
        comboBox.pack(pady=10)
        comboBox.set('Einzelner Kunde')

        # Anzeigen-Button
        self.showButton = ctk.CTkButton(self.mainFrame, text='Anzeigen', command=self.openSelectionWindow)
        self.showButton.pack(side='bottom', pady=10)


    def selectionSingleChoice(self, choice):
       
        # Aktionen für die Auswahl
        actions = {
            'Einzelner Kunde': self.setupSingleDataEntry('Kunde', RentManager.getCustomerById),
            'Einzelnes Fahrzeug': self.setupSingleDataEntry('Fahrzeug', RentManager.getVehicleById),
            'Einzelner Verleih': self.setupSingleDataEntry('Verleih', RentManager.getRentalById)
        }

        # Aktion ausführen, falls vorhanden
        action = actions.get(choice)
        if action:
            action()

    def openSelectionWindow(self):
        
       
        selectedType = self.selectionVar.get()

        dataMap = {
            'Einzelner Kunde': ('Kunden', RentManager.customerList, Customer.createCustomerObj),
            'Einzelnes Fahrzeug': ('Fahrzeuge', RentManager.vehicleList, Vehicle.createVehicleObj),
            'Einzelner Verleih': ('Verleih', RentManager.rentList, Rentals.createRentalObj)
        }

        # Hole die passende Datenkonfiguration
        if selectedType not in dataMap:
            return

        title, dataList, createObjMethod = dataMap[selectedType]

        # Neues Fenster erstellen
        selectionWindow = ctk.CTkToplevel(self.mainFrame)
        selectionWindow.title(f'{title} auswählen')
        selectionWindow.geometry('400x400')

        # Titel
        ctk.CTkLabel(selectionWindow, text=f'Bitte wählen Sie eine {title}:', font=('Arial', 16)).pack(pady=10)

        # Keine Daten verfügbar
        if not dataList:
            ctk.CTkLabel(selectionWindow, text='Keine Daten verfügbar.', font=('Arial', 12)).pack(pady=10)
            return

        # Buttons für alle Datensätze erstellen
        for record in dataList:
            # Button-Text basierend auf dem Datensatz erstellen
            if title == 'Kunden':
                buttonText = f'ID {record['customerID']}, {record['name']}'
            elif title == 'Fahrzeuge':
                buttonText = f'ID {record['serialID']}, {record['brand']}, {record['model']}'
            else:
                buttonText = f'ID {record['rentalID']}'

            # Button erstellen
            ctk.CTkButton(
                selectionWindow,
                text=buttonText,
                command=lambda r=record: self.showSingleDataWindow(title, r, createObjMethod)
            ).pack(fill='x', padx=10, pady=5)
                

    def showSingleDataWindow(self, dataType, record, createObjMethod):
        

        # Neues Fenster für Details erstellen
        self.dataWindow = ctk.CTkToplevel(self.mainFrame)
        self.dataWindow.title(f'{dataType} Details')
        self.dataWindow.geometry('400x300')

        # Titel
        ctk.CTkLabel(self.dataWindow, text=f'{dataType} Details:', font=('Arial', 16)).pack(pady=10)

        # Konvertiere den Datensatz in ein Objekt
        obj = createObjMethod(record)

        # Darstellung des Objekts mithilfe der __str__-Methode
        ctk.CTkLabel(
            self.dataWindow,
            text=str(obj),
            anchor='w',
            font=('Arial', 12),
            justify='left'
        ).pack(fill='x', padx=10, pady=10)


################## Dashboard für Fahrzeuge Hinzufügen ###################


    def addVehicleDashboard(self):
        self.removeAllWidgets()
        
        backFrame = ctk.CTkFrame(self.mainFrame)
        backFrame.pack(fill='both', expand=True)
        contentFrame=ctk.CTkFrame(backFrame)
        contentFrame.pack(pady=20, padx=20)
    
        mappingFields=Vehicle.getVehicleMapping()  
        self.inputs={}

    
        def checkInputFields():

            # Button aktivieren, wenn alle Felder gefüllt sind
                if all(entry.get() for entry in self.inputs.values()):
                    addButton.configure(state='normal')
                    addButton.pack(pady=10)
                else:
                    addButton.configure(state='disabled')
                
            
        for text,dbField in mappingFields.items():
        # Label (deutsche Beschreibung des Feldes)
            addCustomerlabel = ctk.CTkLabel(contentFrame,text=f'{text}:', font=('Arial', 12))
            addCustomerlabel.pack(padx=10, pady=5)

            #Input Feld Überwachung
            inputCheck=ctk.StringVar()
            inputCheck.trace_add('write',lambda *args:checkInputFields())

            # Eingabefeld
            AddVehicleInputField = ctk.CTkEntry(contentFrame,textvariable=inputCheck)
            AddVehicleInputField.pack(padx=10, pady=5)
            self.inputs[dbField] = inputCheck

        titleLabel = ctk.CTkLabel(self.mainFrame, text='Bitte füllen Sie alle Felder aus, um ein neues Fahrzeug hinzuzufügen!!', font=('Arial', 18))
        titleLabel.pack(pady=10)

        addButton=ctk.CTkButton(self.mainFrame,text='Hinzufügen',state='disabled',command=self.getVehicleInputData)
        addButton.pack(pady=10)  # Entfernt alle vorhandenen Widgets aus dem Hauptfenster

    def getVehicleInputData(self): 
        

        if hasattr(self, 'errorLabelID') and self.errorLabelID:
            self.errorLabelID.destroy()
            del self.errorLabelID

        if hasattr(self, 'errorLabelPrice') and self.errorLabelPrice:
            self.errorLabelPrice.destroy()
            del self.errorLabelPrice

        

        inputData={key: var.get() for key,var in self.inputs.items()}
        notValid=False

        if not Validor.validVehicleID(inputData):           
            self.errorLabelID = ctk.CTkLabel(self.mainFrame,text='Die Fahrzeug-ID existiert oder ist ungültig!', text_color='red', font=('Arial', 12))
            self.errorLabelID.place(x=500, y=60)
            notValid=True       
                
        if not Validor.valiedPrice(inputData):    
            self.errorLabelPrice = ctk.CTkLabel(self.mainFrame,text='Die E-Mail ist nicht Gültig!', text_color='red', font=('Arial', 12))
            self.errorLabelPrice.place(x=500, y=80)
            notValid=True


        if notValid:
                return
        else:
            DBManager.insertVehicle(inputData)
            self.rentManager.vehicleList.clear()
            self.rentManager.loadVehicle()
                  

################ Dashboard für  Kunden Hinzufügen #####################

    def addCustomerDashboard(self):

        self.removeAllWidgets()
    
        backFrame = ctk.CTkFrame(self.mainFrame)
        backFrame.pack(fill='both', expand=True)
        contentFrame=ctk.CTkFrame(backFrame)
        contentFrame.pack(pady=20, padx=20)
    
        mappingFields=Customer.getCustomerMapping()  
        self.inputs={}

    
        def checkInputFields():

            # Button aktivieren, wenn alle Felder gefüllt sind
                if all(entry.get() for entry in self.inputs.values()):
                    addButton.configure(state='normal')
                    addButton.pack(pady=10)
                else:
                    addButton.configure(state='disabled')
                
            
        for text,dbField in mappingFields.items():
        # Label (deutsche Beschreibung des Feldes)
            addCustomerlabel = ctk.CTkLabel(contentFrame,text=f'{text}:', font=('Arial', 12))
            addCustomerlabel.pack(padx=10, pady=5)

            #Input Feld Überwachung
            inputCheck=ctk.StringVar()
            inputCheck.trace_add('write',lambda *args:checkInputFields())

            # Eingabefeld
            AddVehicleInputField = ctk.CTkEntry(contentFrame,textvariable=inputCheck)
            AddVehicleInputField.pack(padx=10, pady=5)
            self.inputs[dbField] = inputCheck

        titleLabel = ctk.CTkLabel(self.mainFrame, text='Bitte füllen Sie alle Felder aus, um ein neues Mitglied hinzuzufügen!!', font=('Arial', 18))
        titleLabel.pack(pady=10)

        addButton=ctk.CTkButton(self.mainFrame,text='Hinzufügen',state='disabled',command=self.getInputData)
        addButton.pack(pady=10)


    def getInputData(self): 
        

        if hasattr(self, 'errorLabelID') and self.errorLabelID:
            self.errorLabelID.destroy()
            del self.errorLabelID

        if hasattr(self, 'errorLabelPrice') and self.errorLabelPrice:
            self.errorLabelPrice.destroy()
            del self.errorLabelPrice

        

        inputData={key: var.get() for key,var in self.inputs.items()}
        notValid=False

        if not Validor.validID(inputData):           
            self.errorLabelID = ctk.CTkLabel(self.mainFrame,text='Die Kunden-ID existiert oder ist ungültig!', text_color='red', font=('Arial', 12))
            self.errorLabelID.place(x=500, y=60)
            notValid=True       
                
        if not Validor.validEmail(inputData):    
            self.errorLabelPrice = ctk.CTkLabel(self.mainFrame,text='Die E-Mail ist nicht Gültig!', text_color='red', font=('Arial', 12))
            self.errorLabelPrice.place(x=500, y=80)
            notValid=True


        if notValid:
                return
        else:
            DBManager.insertCustomer(inputData)
            self.rentManager.customerList.clear()
            self.rentManager.loadCustomers()
            

################# Dashboard für Vermietungs Eintrag #################### 

    def addRentalDashboard(self):
        self.removeAllWidgets()

# Haupt-Frame erstellen
        frame = ctk.CTkFrame(self.mainFrame)
        frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Naechste rentalID berechnen
        nextRentalID = self.rentManager.getNextRentalID()

        # Heutiges Datum ermitteln
        todayDate = datetime.today().strftime('%d.%m.%Y')

        # Eingabefelder
        labels = ['Kunden ID:', 'Fahrzeug ID:', 'Mietdatum (Automatisch):']
        self.inputs = {}

        for i, label in enumerate(labels):
            # Label für jedes Eingabefeld
            lbl = ctk.CTkLabel(frame, text=label, font=('Arial', 12))
            lbl.grid(row=i, column=0, padx=10, pady=5)

            if label == 'Mietdatum (Automatisch):':
                # Automatisches Datum (nicht editierbar)
                value = ctk.StringVar(value=todayDate)
                entry = ctk.CTkEntry(frame, textvariable=value, state='disabled')

            elif label == 'Kunden ID:':
                # Eingabefeld + Button für Kunden-Auswahl
                value = ctk.StringVar()
                entry = ctk.CTkEntry(frame, textvariable=value)
                btn_select_customer = ctk.CTkButton(
                    frame,
                    text='Kunde auswählen',
                    command=self.openCustomerSelection  # Kunden-Auswahlfenster öffnen
                )
                btn_select_customer.grid(row=i, column=2, padx=10, pady=5)
            elif label == 'Fahrzeug ID:':
                # Eingabefeld + Button für Fahrzeug-Auswahl
                value = ctk.StringVar()
                entry = ctk.CTkEntry(frame, textvariable=value)
                btn_select_vehicle = ctk.CTkButton(
                    frame,
                    text='Fahrzeug auswählen',
                    command=self.openVehicleSelection  # Fahrzeug-Auswahlfenster öffnen
                )
                btn_select_vehicle.grid(row=i, column=2, padx=10, pady=5)
            else:
                # Normales Eingabefeld
                value = ctk.StringVar()
                entry = ctk.CTkEntry(frame, textvariable=value)

            entry.grid(row=i, column=1, padx=10, pady=5)
            self.inputs[label] = value

        # Hinzufuegen-Button
        btn = ctk.CTkButton(
            frame,
            text='Eintrag Hinzufuegen',
            command=self.addRentalEntry
        )
        btn.grid(row=len(labels), columnspan=2, pady=20)


    def openCustomerSelection(self):
        # Neues Fenster erstellen
        customerWindow = ctk.CTkToplevel(self.mainFrame)
        customerWindow.title('Kunde auswählen')
        customerWindow.geometry('400x400')

        # Ueberschrift
        labelTitle = ctk.CTkLabel(
            customerWindow,
            text='Bitte wählen Sie einen Kunden aus:',
            font=('Arial', 16)
        )
        labelTitle.pack(pady=10)

        # Kunden-Buttons hinzufügen
        for customer in self.rentManager.customerList:
            customer_id = customer['customerID']
            customer_name = customer['name']

            # Button mit ID und Name
            btn = ctk.CTkButton(
                customerWindow,
                text=f'{customer_id} - {customer_name}',
                command=lambda cid=customer_id: self.selectCustomer(customerWindow, cid)
            )
            btn.pack(pady=5, fill='x', padx=10)

    def selectCustomer(self, window, customer_id):
        # Kunden-ID in das entsprechende Eingabefeld setzen
        self.inputs['Kunden ID:'].set(customer_id)

        # Fenster schließen
        window.destroy()

    def openVehicleSelection(self):
        
        # Neues Fenster erstellen
        vehicleWindow = ctk.CTkToplevel(self.mainFrame)
        vehicleWindow.title('Fahrzeug auswählen')
        vehicleWindow.geometry('400x400')

        # Überschrift
        titleLabel = ctk.CTkLabel(
            vehicleWindow,
            text='Bitte wählen Sie ein verfügbares Fahrzeug aus:',
            font=('Arial', 16)
        )
        titleLabel.pack(pady=10)

        # Liste der verfügbaren Fahrzeuge filtern
        rentedSerialIds = {rental['serialID'] for rental in self.rentManager.rentList}
        availableVehicles = [
            vehicle for vehicle in self.rentManager.vehicleList
            if vehicle['serialID'] not in rentedSerialIds
        ]

        # Fahrzeug-Buttons hinzufügen
        if not availableVehicles:
            # Keine Fahrzeuge verfügbar
            noVehiclesLabel = ctk.CTkLabel(
                vehicleWindow,
                text='Keine verfügbaren Fahrzeuge',
                font=('Arial', 12)
            )
            noVehiclesLabel.pack(pady=10)
        else:
            for vehicle in availableVehicles:
                serialId = vehicle['serialID']
                brand = vehicle['brand']
                model = vehicle['model']

                # Button mit serialID und Fahrzeuginformationen
                vehicleButton = ctk.CTkButton(
                    vehicleWindow,
                    text=f'{serialId} - {brand} {model}',
                    command=lambda sid=serialId: self.selectVehicle(vehicleWindow, sid)
                )
                vehicleButton.pack(pady=5, fill='x', padx=10)

    def selectVehicle(self, window, serial_id):
       
        # Fahrzeug-ID in das entsprechende Eingabefeld setzen
        self.inputs['Fahrzeug ID:'].set(serial_id)

        # Fenster schließen
        window.destroy()
    
    def addRentalEntry(self):
   
        # Daten aus den Eingabefeldern holen
        customerId = self.inputs['Kunden ID:'].get()
        serialId = self.inputs['Fahrzeug ID:'].get()
        rentalDate = self.inputs['Mietdatum (Automatisch):'].get()

        # Validierung
        if not customerId or not serialId:
            print('Fehler: Kunden-ID und Fahrzeug-ID dürfen nicht leer sein.')
            return

        if not customerId.isdigit() or not serialId.isdigit():
            print('Fehler: Kunden-ID und Fahrzeug-ID müssen numerisch sein.')
            return

        # Daten für registerRental vorbereiten
        rentalRecord = {
            'customerID': int(customerId),
            'serialID': int(serialId),
            'rentalDate': rentalDate
        }

        # Übergabe der Daten an registerRental
        self.rentManager.registerRental(rentalRecord)
        self.rentManager.customerList.clear()
        self.rentManager.vehicleList.clear()
        self.rentManager.rentList.clear()
        self.rentManager.loadCustomers()
        self.rentManager.loadVehicle()
        self.rentManager.loadRentals()

############### Dashboard für Fahrzeug Zurück gebracht ##############

    def returnVehicleDashboard(self):

        self.removeAllWidgets()

        # Haupt-Frame erstellen
        frame = ctk.CTkFrame(self.mainFrame)
        frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Überschrift
        titleLabel = ctk.CTkLabel(
            frame,
            text='Fahrzeug zurückgebracht',
            font=('Arial', 18)
        )
        titleLabel.pack(pady=10)

        # Liste der geliehenen Fahrzeuge filtern (rentList mit None als returnDate)
        rentedVehicles = [
            rental for rental in self.rentManager.rentList if rental['returnDate'] is None
        ]

        # Keine Fahrzeuge geliehen
        if not rentedVehicles:
            noVehiclesLabel = ctk.CTkLabel(
                frame,
                text='Keine Fahrzeuge sind aktuell ausgeliehen.',
                font=('Arial', 12)
            )
            noVehiclesLabel.pack(pady=10)
            return

        # Aktuelles Datum ermitteln
        todayDate = datetime.today().strftime('%d.%m.%Y')

        # Buttons für jedes geliehene Fahrzeug erstellen
        for rental in rentedVehicles:
            rentalId = rental['rentalID']
            customerId = rental['customerID']
            serialId = rental['serialID']
            rentalDate = rental['rentalDate']

            # Button-Text mit Mietinformationen
            buttonText = f'Miete #{rentalId}: Fahrzeug {serialId}, Kunde {customerId}, Datum: {rentalDate}'

            # Button für Fahrzeug erstellen
            rentalButton = ctk.CTkButton(
                frame,
                text=buttonText,
                command=lambda rid=rentalId: self.returnVehicle(rid, todayDate)
            )
            rentalButton.pack(pady=5, fill='x', padx=10)


    def returnVehicle(self, rentalId, returnDate):
    
    
    # Mietdatensatz in rentList finden
        rental = next((r for r in self.rentManager.rentList if r['rentalID'] == rentalId), None)

        if not rental:
            # Falls kein Eintrag gefunden wird
            messagebox.showerror('Fehler', f'Miete mit ID {rentalId} nicht gefunden.')
            return

        # Rückgabedatum setzen
        rental['returnDate'] = returnDate

        # Datenbank aktualisieren
        success = DBManager.updateRental(rental)

        if success:
            # Erfolgsnachricht anzeigen
            messagebox.showinfo('Erfolg', f'Rückgabedatum für Miete #{rentalId} wurde erfolgreich gespeichert.')
            self.rentManager.customerList.clear()
            self.rentManager.vehicleList.clear()
            self.rentManager.rentList.clear()
            self.rentManager.loadCustomers()
            self.rentManager.loadVehicle()
            self.rentManager.loadRentals()
        else:
            # Fehlermeldung anzeigen
            messagebox.showerror('Fehler', f'Rückgabedatum für Miete #{rentalId} konnte nicht gespeichert werden.')

########## Inertface für Fahrzeug entfernen ##########


    def deleteVehicleDashboard(self):
        # Entfernt alle Widgets des Hauptframes
        self.removeAllWidgets()

        # Haupt-Frame erstellen
        frame = ctk.CTkFrame(self.mainFrame)
        frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Überschrift
        labelTitle = ctk.CTkLabel( frame, text='Fahrzeug löschen',font=('Arial', 16))
        labelTitle.pack(pady=10)

        # Liste der verfügbaren Fahrzeuge aus der DB holen
        availableVehicles = self.rentManager.vehicleList

        # Buttons für jedes Fahrzeug erstellen
        for vehicle in availableVehicles:
            vehicle_text = f'ID {vehicle['serialID']} - {vehicle['brand']} {vehicle['model']}'
            
            vehicleButton = ctk.CTkButton( frame, text=vehicle_text,command=lambda v=vehicle: self.deleteVehicle(v) )
            vehicleButton.pack(fill='x', padx=10, pady=5)

    def deleteVehicle(self, vehicle):
        # Bestätigungsdialog
        confirm = messagebox.askyesno(
            'Bestätigung',
            f'Sind Sie sicher, dass Sie das Fahrzeug \'{vehicle['brand']} {vehicle['model']}\' (ID {vehicle['serialID']}) löschen möchten?'
        )

        if not confirm:
            return  # Abbrechen, wenn der Benutzer 'Nein' wählt

        # Fahrzeug aus der Datenbank löschen
        success = DBManager.deleteVehicleFromDB(vehicle['serialID'])

        if success:
            self.rentManager.vehicleList.clear()
            self.rentManager.loadVehicle()
            messagebox.showinfo(
                'Erfolg',
                f'Das Fahrzeug \'{vehicle['brand']} {vehicle['model']}\' wurde erfolgreich gelöscht.'
            )
            # Aktualisierung der Ansicht
            self.deleteVehicleDashboard()
        else:
            messagebox.showerror(
                'Fehler',
                f'Das Fahrzeug \'{vehicle['brand']} {vehicle['model']}\' konnte nicht gelöscht werden.'
            )

          