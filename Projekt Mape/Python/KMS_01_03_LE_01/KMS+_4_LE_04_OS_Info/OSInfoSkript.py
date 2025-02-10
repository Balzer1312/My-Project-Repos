import customtkinter as ctk
import platform
import sys
import csv
import os
from tkinter import messagebox
from datetime import datetime


class SystemInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Systeminformationen')
        self.root.geometry('600x750')
        self.root.resizable(False, False)

        currentCsvPos = os.path.dirname(__file__)
        self.infoOSToCsv = os.path.join(currentCsvPos, 'Systeminfo.csv')

        # Systeminformationen auf Deutsch
        self.infoMap = {
            'Zeit': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'System': platform.system(),
            'Rechnername': platform.node(),
            'Veröffentlichung': platform.release(),
            'Version': platform.version(),
            'Maschine': platform.machine(),
            'Prozessor': platform.processor(),
            'Python-Version': sys.version
        }

        # Variablen für Checkboxen
        self.selectedInfoVars = {key: ctk.StringVar(value='0') for key in self.infoMap.keys()}

        # Erstelle GUI-Elemente
        self.mainDashboard()

    def mainDashboard(self):
        # Label und Textbox
        ctk.CTkLabel(self.root, text='Systeminformationen App', font=('Arial', 20)).pack(pady=10)

        # Checkboxen für Mehrfachauswahl
        checkboxFrame = ctk.CTkFrame(self.root)
        checkboxFrame.pack(pady=10)
        for key in self.infoMap.keys():
            ctk.CTkCheckBox(checkboxFrame, text=key, variable=self.selectedInfoVars[key]).pack(anchor='w', padx=10, pady=5)


        self.infoText = ctk.CTkTextbox(self.root, height=200, width=500, state='disabled')
        self.infoText.pack(pady=10)

        # Buttons
        ctk.CTkButton(self.root, text='Auswahl anzeigen', command=self.getSelectedInfo).pack(pady=5)
        ctk.CTkButton(self.root, text='Speichern als CSV', command=self.saveToCsv).pack(pady=5)
        ctk.CTkButton(self.root, text='CSV laden', command=self.loadFromCsv).pack(pady=5)


    def getSelectedInfo(self):
        # Sammle die ausgewählten Informationen
        selectedInfo = {key: value for key, value in self.infoMap.items() if self.selectedInfoVars[key].get() == '1'}

        if not selectedInfo:
            messagebox.showerror('Fehler', 'Bitte wähle mindestens eine Information aus.')
            return

        # Zeige die ausgewählten Informationen in der Textbox
        self.infoText.configure(state='normal')
        self.infoText.delete('1.0', ctk.END)
        for key, value in selectedInfo.items():
            self.infoText.insert(ctk.END, f'{key}: {value}\n')
        self.infoText.configure(state='disabled')

        # Speichere die ausgewählten Informationen
        self.currentInfo = selectedInfo

    def saveToCsv(self):
        if not hasattr(self, 'currentInfo') or not self.currentInfo:
            messagebox.showerror('Fehler', 'Keine Informationen vorhanden, um sie zu speichern.')
            return

        if not self.infoOSToCsv:
            return

        with open(self.infoOSToCsv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Schlüssel', 'Wert'])
            for key, value in self.currentInfo.items():
                writer.writerow([key, value])

        messagebox.showinfo('Erfolg', 'Ausgewählte Systeminformationen als CSV gespeichert.')

    def loadFromCsv(self):
        if not self.infoOSToCsv:
            return

        try:
            with open(self.infoOSToCsv, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Überspringe die Header-Zeile
                loadedCsvInfo = {rows[0]: rows[1] for rows in reader}

            # Lade Info aus CSV in die Textbox
            self.infoText.configure(state='normal')
            self.infoText.delete('1.0', ctk.END)
            for key, value in loadedCsvInfo.items():
                self.infoText.insert(ctk.END, f'{key}: {value}\n')
            self.infoText.configure(state='disabled')

        except Exception as e:
            messagebox.showerror('Fehler', f'CSV konnte nicht geladen werden: {e}')


if __name__ == '__main__':
    root = ctk.CTk()
    ctk.set_appearance_mode('System')
    ctk.set_default_color_theme('blue')
    app = SystemInfoApp(root)
    root.mainloop()