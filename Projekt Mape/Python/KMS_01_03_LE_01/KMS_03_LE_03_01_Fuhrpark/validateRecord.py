import re
from tkinter import messagebox
import customtkinter as ctk
from JsonHandler import JsonHandler


class Validate:
 
    @staticmethod
    def validateLicensePlate(vehicleType, licensePlate):
        
        if vehicleType in ['PKW', 'Motorrad', 'LKW']:

            # Motorisierte Fahrzeuge: Kennzeichen muss mit 'AT' beginnen und gefolgt von Buchstaben/Zahlen
            if not re.match(r'^AT\d{3,}$', licensePlate):
                messagebox.showerror(
                     '\'Validierungsfehler\'',
                       f'Das Kennzeichen {licensePlate} ist ungültig. Es muss mit \'AT\' beginnen und Zahlen enthalten.'
                    )
                return False
            
        elif vehicleType == 'Fahrrad':

            # Nicht motorisierte Fahrzeuge: ID muss eine eindeutige Zahl sein
            try:
                idValue = int(licensePlate)

            except ValueError:
                messagebox.showerror(
                        '\'Validierungsfehler\'',
                        f' Die ID {licensePlate} muss eine gültige ganze Zahl sein.'
                    )
                return False
            
            # Prüfen, ob die ID bereits verwendet wurde
            if idValue in JsonHandler.allVehicleList['NoneMotorrested']:   
                   messagebox.showerror(
                        '\'Validierungsfehler\'',
                        f'Die ID {licensePlate} ist bereits vergeben. Bitte wählen Sie eine andere ID.'
                    )
                   return False
                                
        return True

    @staticmethod
    def noEmptyField(inputFields, submitButton):
        # Überprüfen, ob alle Felder gültige Werte haben
        for field, widget in inputFields.items():
            value = widget.get() if isinstance(widget, ctk.CTkEntry) else widget.get()

            if not value.strip():  # Leere Felder nicht zulassen
                submitButton.configure(state='disabled')
                return
        submitButton.configure(state='normal')