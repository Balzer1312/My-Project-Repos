import tkinter as tk
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from VehicleClass import Vehicle
from VehicleGUIManagment import GuiManager
from JsonHandler import JsonHandler

class mainGUIFrame:
    def __init__(self, root):
        JsonHandler.loadJson()  
        self.root = root
        self.canvas = None
        self.root.title('Fuhrpark Verwaltung')
        self.root.geometry('900x600')

        # Layout setup
        self.sidebarFrame = ctk.CTkFrame(self.root, width=200)
        self.sidebarFrame.pack(side='left', fill='y')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.mainFrame.pack(side='right', expand=True, fill='both')

        self.guiManager=GuiManager(self.mainFrame)
        

        # Sidebar Buttons
        self.addVehicleButton = ctk.CTkButton(self.sidebarFrame, text='Fahrzeug hinzufügen', command=self.guiManager.displayAddVehicleForm)
        self.addVehicleButton.pack(pady=10, padx=10)

        self.displayVehiclesButton = ctk.CTkButton(self.sidebarFrame, text='Fahrzeuge anzeigen', command=self.guiManager.displayVehicleFrame)
        self.displayVehiclesButton.pack(pady=10, padx=10)

        self.refuelVehicleButton = ctk.CTkButton(self.sidebarFrame, text='Tanken', command=self.guiManager.showRefuelOptions)
        self.refuelVehicleButton.pack(pady=10, padx=10)

        self.showFuelReportButton = ctk.CTkButton(self.sidebarFrame, text='Treibstoff-Bericht', command=self.guiManager.showFuelReport)
        self.showFuelReportButton.pack(pady=10, padx=10)

        self.guiManager.displayWelcomeMessage()


if __name__ == '__main__':
    ctk.set_appearance_mode('Dark')
    root = ctk.CTk()
    app = mainGUIFrame(root)
    root.mainloop()
