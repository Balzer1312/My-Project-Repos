
import customtkinter as ctk

from rentDashboard import RentDashboard
from adminRentClass import RentManager


class MainGUI:

    def __init__(self, root): 
        self.root = root
        self.root.title('Vereinsverwaltung')
        self.root.geometry('900x600')
        self.initializeData()

        self.sidebarFrame=ctk.CTkFrame(self.root,width=200,fg_color='#3d3c3c')
        self.sidebarFrame.pack(side='left',fill='y')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.mainFrame.pack(side='right', expand=True, fill='both')

        self.rentDashboard = RentDashboard(self.mainFrame)
        self.rentDashboard.displayWelcomeMessage()
        
        self.showAllInfoButton= ctk.CTkButton(self.sidebarFrame,text='Liste anzeigen',command=self.rentDashboard.selectInfoControl)
        self.showAllInfoButton.pack(pady=10,padx=10)

        self.saveCsvButton=ctk.CTkButton(self.sidebarFrame,text='Einzelne Daten anzeigen',command=self.rentDashboard.selectSingleInfoControl)
        self.saveCsvButton.pack(pady=10,padx=10)

        self.addCustomerButton= ctk.CTkButton(self.sidebarFrame,text='Fahrzeug Hinzufügen',command=self.rentDashboard.addVehicleDashboard)
        self.addCustomerButton.pack(pady=10,padx=10)

        self.addVehicleButton= ctk.CTkButton(self.sidebarFrame,text='Kunden Hinzufügen',command=self.rentDashboard.addCustomerDashboard) 
        self.addVehicleButton.pack(pady=10,padx=10)

        self.rentButton=ctk.CTkButton(self.sidebarFrame,text='Vermietung',command=self.rentDashboard.addRentalDashboard)
        self.rentButton.pack(pady=10,padx=10)

        self.returnVehButton=ctk.CTkButton(self.sidebarFrame,text='Rückgabe',command=self.rentDashboard.returnVehicleDashboard)
        self.returnVehButton.pack(pady=10,padx=10)

        self.deletVehButton=ctk.CTkButton(self.sidebarFrame,text='Fahrzeug entfernen',command=self.rentDashboard.deleteVehicleDashboard)
        self.deletVehButton.pack(pady=10,padx=10)


#### DB Daten Initialisieren ####

    def initializeData(self):  
        RentManager.loadCustomers()
        RentManager.loadVehicle()
        RentManager.loadRentals()


if __name__ == '__main__':
    ctk.set_appearance_mode('Dark')
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()