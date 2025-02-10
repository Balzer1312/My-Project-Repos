import tkinter as tk
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from validateRecord import Validate
from JsonHandler import JsonHandler
from VehicleClassManager import VehicleManager
from MotorrestedClass import Motorrested,Car,Motorcycle,Truck
from NoneMotorrestedClass import NoneMotorrested,Bicycle



class GuiManager:

    def __init__(self, mainFrame):
        self.mainFrame = mainFrame
        self.canvas = None

    def displayWelcomeMessage(self):
        self.clearMainFrame()
        welcomeLabel = ctk.CTkLabel(self.mainFrame, text='Willkommen zur Fahrzeugverwaltung!', font=('Arial', 18))
        welcomeLabel.pack(pady=20)

    def clearMainFrame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def displayAddVehicleForm(self):
        self.clearMainFrame()

       
        vehicleTypeLabel = ctk.CTkLabel(self.mainFrame, text='Fahrzeugtyp auswählen:')
        vehicleTypeLabel.pack(pady=10)

        self.vehicleTypeVariable = tk.StringVar(value='PKW')
        vehicleTypeDropdown = ctk.CTkOptionMenu(
            self.mainFrame, values=['PKW', 'Motorrad', 'LKW', 'Fahrrad'], variable=self.vehicleTypeVariable,
            command=self.updateVehicleForm
        )
        vehicleTypeDropdown.pack(pady=10)

        self.formFrame = ctk.CTkFrame(self.mainFrame)
        self.formFrame.pack(fill='both', expand=True, padx=20, pady=10)

        self.updateVehicleForm(self.vehicleTypeVariable.get())

    def updateVehicleForm(self, vehicleType):
        for widget in self.formFrame.winfo_children():
            widget.destroy()

        commonFields = ['Farbe', 'Modell', 'Marke']
        specificFields = []

        if vehicleType == 'PKW':
            specificFields = ['Kennzeichen', 'Kraftstoff', 'Verbrauch', 'Kilometerstand', 'Türen']
        elif vehicleType == 'Motorrad':
            specificFields = ['Kennzeichen', 'Kraftstoff', 'Verbrauch', 'Kilometerstand', 'Gänge']
        elif vehicleType == 'LKW':
            specificFields = ['Kennzeichen', 'Kraftstoff', 'Verbrauch', 'Kilometerstand', 'Ladungsgewicht']
        elif vehicleType == 'Fahrrad':
            specificFields = ['ID', 'Gänge']

        self.inputFields = {}

        formGrid = ctk.CTkFrame(self.formFrame)
        formGrid.pack(fill='both', expand=True, padx=20, pady=10)

        row = 0
        for field in commonFields + specificFields:
            label = ctk.CTkLabel(formGrid, text=f'{field}:')
            label.grid(row=row, column=0, padx=10, pady=5, sticky='w')

            if field == 'Kraftstoff':
                # Combobox für Kraftstoff
                fuelOptions = ['Diesel', 'Benzin', 'Strom']
                comboBox = ctk.CTkComboBox(formGrid, values=fuelOptions,state='readonly')
                comboBox.grid(row=row, column=1, padx=10, pady=5, sticky='w')
                comboBox.bind("<<ComboboxSelected>>", lambda e: Validate.noEmptyField(self.inputFields, self.submitButton))
                self.inputFields[field] = comboBox

            else:
                entry = ctk.CTkEntry(formGrid)
                entry.grid(row=row, column=1, padx=10, pady=5, sticky='w')
                entry.bind("<KeyRelease>", lambda e: Validate.noEmptyField(self.inputFields, self.submitButton))
                self.inputFields[field] = entry

            row += 1

        self.validationMessage = ctk.CTkLabel(
            self.formFrame,
            text="Bitte füllen Sie alle Felder aus, um ein Fahrzeug hinzuzufügen.",
            text_color="white"
        )
        self.validationMessage.pack(pady=10)

        self.submitButton = ctk.CTkButton(self.formFrame, text='Hinzufügen', command=self.addVehicle)
        self.submitButton.pack(pady=20)
        
        Validate.noEmptyField(self.inputFields, self.submitButton)


    def addVehicle(self):
        try:
            # Eingabewerte aus den Formularfeldern sammeln
            inputData = {field: self.inputFields[field].get() for field in self.inputFields}
            selectedVehicleType = self.vehicleTypeVariable.get()

            # Mapping von Fahrzeugtypen
            vehicleTypeMapping = {
                'PKW': 'Car',
                'Motorrad': 'Motorcycle',
                'LKW': 'Truck',
                'Fahrrad': 'Bicycle'
            }

            # Mapping von Formularfeldern zu JSON-Schlüsseln
            fieldMapping = {
                'Farbe': 'color',
                'Modell': 'model',
                'Marke': 'brand',
                'Kennzeichen': 'mark',
                'Kraftstoff': 'fuel',
                'Verbrauch': 'consumption',
                'Kilometerstand': 'mileage',
                'Türen': 'doors',
                'Gänge': 'gears',
                'Ladungsgewicht': 'loadingWeight',
                'ID': 'id'
            }

            # JSON-Datensatz erstellen
            jsonData = {'type': vehicleTypeMapping[selectedVehicleType]}
            for key, value in inputData.items():
                if key in fieldMapping and value.strip():
                    mappedKey = fieldMapping[key] 

                    if selectedVehicleType in ['PKW', 'Motorrad', 'LKW']:  # Motorisierte Fahrzeuge
                        if mappedKey in ['mileage', 'doors', 'gears', 'loadingWeight']:
                            jsonData[mappedKey] = int(value.strip())  # Integer-Felder
                        elif mappedKey == 'consumption':
                            jsonData[mappedKey] = float(value.strip())  # Float-Feld
                        else:
                            jsonData[mappedKey] = value.strip()  # String-Felder

                    elif selectedVehicleType == 'Fahrrad':  # Nicht-motorisierte Fahrzeuge
                        if mappedKey in ['id', 'gears']:
                            jsonData[mappedKey] = int(value.strip())  # Integer-Felder
                        else:
                            jsonData[mappedKey] = value.strip()

            # Validierung: Struktur der Felder überprüfen 
            if not Validate.validateLicensePlate(selectedVehicleType, jsonData.get('mark', jsonData.get('id'))):
                return           
            
            # Fahrzeugobjekt erstellen und in die Json Datei speichern
            newVehicle = VehicleManager.addVehicle(jsonData)      
            if not newVehicle:
                return 
            JsonHandler.updateJson(jsonData, 'Motorrested' if isinstance(newVehicle, Motorrested) else 'NoneMotorrested')
            JsonHandler.loadJson()
            # Erfolgsmeldung anzeigen
            messagebox.showinfo('Erfolg', 'Das Fahrzeug wurde erfolgreich hinzugefügt!')
            self.displayWelcomeMessage()

        except Exception as error:
            messagebox.showerror('Fehler', f'Fehler beim Hinzufügen: {str(error)}')       

    def displayVehicleFrame(self):
        self.clearMainFrame()

        filterLabel = ctk.CTkLabel(self.mainFrame, text='Fahrzeuge anzeigen nach Kategorie:', font=('Arial', 14))
        filterLabel.pack(pady=10)

        self.vehicleFilterVariable = tk.StringVar(value='Alle Fahrzeuge')
        vehicleFilterDropdown = ctk.CTkOptionMenu(
            self.mainFrame, values=[
                'Alle Fahrzeuge',
                'Motorisierte Fahrzeuge',
                'Nicht motorisierte Fahrzeuge',
                'PKWs',
                'Motorräder',
                'LKWs',
                'Fahrräder'
            ], variable=self.vehicleFilterVariable
        )
        vehicleFilterDropdown.pack(pady=10)

        showButton = ctk.CTkButton(self.mainFrame, text='Anzeigen', command=self.displayFilteredVehicles)
        showButton.pack(pady=10)

    def displayFilteredVehicles(self):
        self.clearMainFrame()
        filterChoice = self.vehicleFilterVariable.get()

        scrollableFrame = ctk.CTkScrollableFrame(self.mainFrame)
        scrollableFrame.pack(fill='both', expand=True, padx=20, pady=20)

        try:
            if filterChoice == 'Alle Fahrzeuge':
                vehicles = VehicleManager.showAllVehicles()
            elif filterChoice == 'Motorisierte Fahrzeuge':
                vehicles =  VehicleManager.showMotorrested()
            elif filterChoice == 'Nicht motorisierte Fahrzeuge':
                vehicles =  VehicleManager.showNoneMotorrested()
            elif filterChoice == 'PKWs':
                vehicles =  VehicleManager.showAllCars()
            elif filterChoice == 'Motorräder':
                vehicles =  VehicleManager.showAllMotorcycle()
            elif filterChoice == 'LKWs':
                vehicles =  VehicleManager.showAllTruck()
            elif filterChoice == 'Fahrräder':
                vehicles =  VehicleManager.showAllBicycle()
            else:
                vehicles = []

            if vehicles:
                for vehicle in vehicles:
                    label = ctk.CTkLabel(scrollableFrame, text=str(vehicle), anchor='w', justify='left')
                    label.pack(fill='x', padx=10, pady=5)
            else:
                noDataLabel = ctk.CTkLabel(scrollableFrame, text='Keine Fahrzeuge gefunden.', anchor='w')
                noDataLabel.pack(pady=20)

        except Exception as error:
            messagebox.showerror('Fehler', f'Fehler beim Anzeigen: {str(error)}')

    def showRefuelOptions(self):
        self.clearMainFrame()

        titleLabel = ctk.CTkLabel(self.mainFrame, text='Wählen Sie ein Fahrzeug zum Tanken:', font=('Arial', 14))
        titleLabel.pack(pady=10)

        searchFrame = ctk.CTkFrame(self.mainFrame)
        searchFrame.pack(pady=10)

        searchLabel = ctk.CTkLabel(searchFrame, text='Nach Kennzeichen suchen:')
        searchLabel.grid(row=0, column=0, padx=10, pady=5)

        searchEntry = ctk.CTkEntry(searchFrame)
        searchEntry.grid(row=0, column=1, padx=10, pady=5)

        vehicleListFrame = ctk.CTkFrame(self.mainFrame)
        vehicleListFrame.pack(fill='both', expand=True, padx=10, pady=10)

        def updateVehicleList():
            for widget in vehicleListFrame.winfo_children():
                widget.destroy()

            searchText = searchEntry.get().lower()
            motorizedVehicles = JsonHandler.allVehicleList['Motorrested']

            for vehicle in motorizedVehicles:
                if searchText in vehicle['mark'].lower():
                    vehicleButton = ctk.CTkButton(
                        vehicleListFrame,
                        text=f'{vehicle['brand']} {vehicle['model']} ({vehicle['mark']}) - {vehicle['fuel']}',
                        command=lambda v=vehicle: self.refuelWindow(v)
                    )
                    vehicleButton.pack(pady=5)

        searchButton = ctk.CTkButton(searchFrame, text='Suchen', command=updateVehicleList)
        searchButton.grid(row=0, column=2, padx=10, pady=5)

        updateVehicleList()

    def refuelWindow(self, vehicle):
        # Neues Fenster für die Tankeingabe
        refuelWindow = ctk.CTkToplevel(self.mainFrame)
        refuelWindow.title('Fahrzeug Tanken')
        refuelWindow.geometry('400x500')

        vehicleLabel = ctk.CTkLabel(refuelWindow, text=f'Fahrzeug: {vehicle['brand']} {vehicle['model']} ({vehicle['mark']})', font=('Arial', 14))
        vehicleLabel.pack(pady=10)

        fuelTypeLabel = ctk.CTkLabel(refuelWindow, text=f'Treibstoffart: {vehicle['fuel']}')
        fuelTypeLabel.pack(pady=10)

        monthLabel = ctk.CTkLabel(refuelWindow, text='Monat:')
        monthLabel.pack(pady=10)
        monthCombo = ctk.CTkComboBox(refuelWindow, values=['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'])
        monthCombo.pack(pady=5)

        yearLabel = ctk.CTkLabel(refuelWindow, text='Jahr:')
        yearLabel.pack(pady=10)
        yearCombo = ctk.CTkComboBox(refuelWindow, values=['2024', '2025'])
        yearCombo.pack(pady=5)

        amountLabel = ctk.CTkLabel(refuelWindow, text='Menge (Liter/kWh):')
        amountLabel.pack(pady=10)
        amountEntry = ctk.CTkEntry(refuelWindow)
        amountEntry.pack(pady=5)

        def saveRefuelData():
            month = monthCombo.get()
            year = yearCombo.get()
            amount = amountEntry.get()
            if not month or not year or not amount:
                messagebox.showerror('Fehler', 'Bitte alle Felder ausfüllen!')
                return

            try:
                Motorrested.refuel(vehicle['mark'], year, month, vehicle['fuel'], float(amount))
                messagebox.showinfo('Erfolg', f'{amount} l {vehicle['fuel']} wurden erfolgreich getankt im Monat {month} {year}.')
                refuelWindow.destroy()
            except Exception as e:
                messagebox.showerror('Fehler', str(e))

        saveButton = ctk.CTkButton(refuelWindow, text='Speichern', command=saveRefuelData)
        saveButton.pack(pady=20)

    def showFuelReport(self):
        self.clearMainFrame()

        yearLabel = ctk.CTkLabel(self.mainFrame, text='Jahr:')
        yearLabel.pack(pady=10)
        self.yearCombo = ctk.CTkComboBox(self.mainFrame, values=['2024', '2025','2026'])
        self.yearCombo.pack(pady=5)

        monthLabel = ctk.CTkLabel(self.mainFrame, text='Monat:')
        monthLabel.pack(pady=10)
        self.monthCombo = ctk.CTkComboBox(self.mainFrame, values=['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'])
        self.monthCombo.pack(pady=5)

        showButton = ctk.CTkButton(self.mainFrame, text='Anzeigen', command=self.plotMonthlyStatistics)
        showButton.pack(pady=20)

    def plotMonthlyStatistics(self):
        year = self.yearCombo.get()
        month = self.monthCombo.get()

        data=Motorrested.refuelJsonData()
        if year not in data['refuels'] or month not in data['refuels'][year]:
            messagebox.showerror('Fehler', f'Keine Daten für {month} {year} verfügbar.')
            return
        
        monthData = data['refuels'][year][month]
        fuelTypes = list(monthData.keys())
        fuelAmounts = list(monthData.values())
        
        fuelTypeLabels = []
        for fuel in fuelTypes:
            unit = 'kWh' if fuel == 'Elektrisch' else 'Liter'
            fuelTypeLabels.append(f'{fuel} ({unit})')
        
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        
        chartObject, axis = plt.subplots()
        axis.bar(fuelTypeLabels, fuelAmounts, color=['blue', 'green', 'orange'])
        axis.set_title(f'Treibstoffverbrauch im {month} {year}')
        axis.set_xlabel('Treibstoffart')
        axis.set_ylabel('Verbrauch (Liter/kWh)')

        self.canvas = FigureCanvasTkAgg(chartObject, master=self.mainFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)