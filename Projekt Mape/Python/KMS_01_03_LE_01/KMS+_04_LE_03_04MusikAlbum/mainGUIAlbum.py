import tkinter as tk
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk
 
from albumDashboard import AlbumDashboard
from albumManager import AlbumManager

class MainGUI:
    albumManager=AlbumManager()
    albumManager.getAlbumWithTracks()


    def __init__(self, root): 
        self.root = root
        self.root.title('Vereinsverwaltung')
        self.root.geometry('900x600')

        self.sidebarFrame=ctk.CTkFrame(self.root,width=200,fg_color='#3d3c3c')
        self.sidebarFrame.pack(side='left',fill='y')

        self.mainFrame = ctk.CTkFrame(self.root)
        self.mainFrame.pack(side='right', expand=True, fill='both')

        self.albumDashboard =AlbumDashboard(self.mainFrame)
        self.albumDashboard.displayWelcomeMessage()
        
        self.addAlbumButton= ctk.CTkButton(self.sidebarFrame,text='Album Anlegen',command=self.albumDashboard.addAlbumDashboard)
        self.addAlbumButton.pack(pady=10,padx=10)

        self.addMemberButton= ctk.CTkButton(self.sidebarFrame,text='Album Löschen',command=self.albumDashboard.deletAlbumDashboard)
        self.addMemberButton.pack(pady=10,padx=10)

        self.deletMemberButton= ctk.CTkButton(self.sidebarFrame,text='Tracks Hinzufügen',command=self.albumDashboard.addTrackDashboard)
        self.deletMemberButton.pack(pady=10,padx=10)

        self.deletAlbumButton=ctk.CTkButton(self.sidebarFrame,text='Tracks Löschen',command=self.albumDashboard.deleteTrackDashboard)
        self.deletAlbumButton.pack(pady=10,padx=10)

        self.showAlbumButton=ctk.CTkButton(self.sidebarFrame,text='Album Ausgeben',command=self.albumDashboard.albumToDisplay)
        self.showAlbumButton.pack(pady=10,padx=10)
        


if __name__ == '__main__':
    ctk.set_appearance_mode('Dark')
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()