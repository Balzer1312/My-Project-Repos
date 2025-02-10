import tkinter as tk
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk

from dashboardManager import UserDashboard
from bankmanager import BankManager


class MainGUI:
    bankManager=BankManager()
    bankManager.getDataFromDB()


    def __init__(self, root): 
        self.root = root
        self.root.title('Vereinsverwaltung')
        self.root.geometry('900x600')

        self.sidebarFrame=ctk.CTkFrame(self.root,width=200,fg_color="#3d3c3c")
        self.sidebarFrame.pack(side='left',fill='y')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.mainFrame.pack(side='right', expand=True, fill='both')

        self.dashboardManager=UserDashboard(self.mainFrame)
        self.dashboardManager.displayWelcomeMessage()
        
        self.memberToDisplayButton= ctk.CTkButton(self.sidebarFrame,text='Konto Anzeigen',command=self.dashboardManager.accountToDisplay)
        self.memberToDisplayButton.pack(pady=10,padx=10)

        self.addMemberButton= ctk.CTkButton(self.sidebarFrame,text='Konto Anlegen',command=self.dashboardManager.addDataDashboard)
        self.addMemberButton.pack(pady=10,padx=10)

        self.deletMemberButton= ctk.CTkButton(self.sidebarFrame,text='Konto Löschen',command=self.dashboardManager.deletDataDashboard)
        self.deletMemberButton.pack(pady=10,padx=10)

        self.managMemberButton=ctk.CTkButton(self.sidebarFrame,text='Konto Verwaltung',command=self.dashboardManager.accountManagerDashboard)
        self.managMemberButton.pack(pady=10,padx=10)

        self.managMemberButton=ctk.CTkButton(self.sidebarFrame,text='Konto zu CSV',command=self.dashboardManager.accountsToCSV)
        self.managMemberButton.pack(pady=10,padx=10)
        


if __name__ == '__main__':
    ctk.set_appearance_mode('Dark')
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()