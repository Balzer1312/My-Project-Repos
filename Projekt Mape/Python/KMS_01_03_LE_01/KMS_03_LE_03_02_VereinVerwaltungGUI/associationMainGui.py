import tkinter as tk
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk
from OrganizationDashboard import OrganizationGUI
from UnionManager import ClubManager

class MainGUI:
    clubManager= ClubManager()
    clubManager.getDataFromDB()

    def __init__(self, root): 
        self.root = root
        self.root.title('Vereinsverwaltung')
        self.root.geometry('900x600')

        self.sidebarFrame=ctk.CTkFrame(self.root,width=200,fg_color="#3d3c3c")
        self.sidebarFrame.pack(side='left',fill='y')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.mainFrame.pack(side='right', expand=True, fill='both')

        self.guiManager=OrganizationGUI(self.mainFrame)
        self.guiManager.displayWelcomeMessage()
        
        self.memberToCsvButton= ctk.CTkButton(self.sidebarFrame,text='CSV der Mitglieder',command=self.guiManager.memberToCsvFrame)
        self.memberToCsvButton.pack(pady=10,padx=10)

        self.addMemberButton= ctk.CTkButton(self.sidebarFrame,text='Mitglieder Hinzufügen',command=self.guiManager.addMember)
        self.addMemberButton.pack(pady=10,padx=10)

        self.managMemberButton=ctk.CTkButton(self.sidebarFrame,text='Mitglieder Verwalten',command=self.guiManager.manageMember)
        self.managMemberButton.pack(pady=10,padx=10)
        


if __name__ == '__main__':
    ctk.set_appearance_mode('Dark')
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()