import os
from tkinter import messagebox
import customtkinter as ctk

from albumManager import AlbumManager

class AlbumDashboard:

    albumManager=AlbumManager()

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

############# Interface Album Anlegen ##############

    def addAlbumDashboard(self):

        self.removeAllWidgets()
        
        taskLabel = ctk.CTkLabel(self.mainFrame, text='Album Anlegen:', font=('Arial', 12))
        taskLabel.pack(pady=5, padx=10)

        
        self.albumNameVar = ctk.StringVar()
        self.artistVar = ctk.StringVar()

        self.errorLabel = ctk.CTkLabel(self.mainFrame, text='', font=('Arial', 10), text_color='red',bg_color='transparent')
        self.errorLabel.pack(pady=5, padx=10)

        # Album Name Label und Entry
        albumNameLabel = ctk.CTkLabel(self.mainFrame, text='Album Name:', font=('Arial', 12))
        albumNameLabel.pack(pady=5, padx=10)
        self.albumNameEntry = ctk.CTkEntry(self.mainFrame,textvariable=self.albumNameVar)
        self.albumNameEntry.pack(pady=5, padx=10)

        # Künstler Label und Entry
        artistLabel = ctk.CTkLabel(self.mainFrame, text='Album Künstler:', font=('Arial', 12))
        artistLabel.pack(pady=5, padx=10)
        self.artistEntry = ctk.CTkEntry(self.mainFrame,textvariable=self.artistVar)
        self.artistEntry.pack(pady=5, padx=10)

        self.saveButton = ctk.CTkButton(
            self.mainFrame,
             text='Speichern',
            state='disabled',                           
            command=lambda: self.albumManager.addAlbum(self.albumNameVar.get().strip(), self.artistVar.get().strip())
        )

        self.saveButton.pack(pady=10)

        self.albumNameVar.trace_add('write',self.inputAlbumMonitoring)
        self.artistVar.trace_add('write',self.inputAlbumMonitoring)

    #Input überwachung 
    def inputAlbumMonitoring(self,*args):

        albumNameInputfill= bool(self.albumNameVar.get().strip())
        artistNameInputfill= bool(self.artistVar.get().strip())

        if albumNameInputfill and artistNameInputfill:
            self.saveButton.configure(state='normal')
        else:
            self.saveButton.configure(state='disabled')

################# Interface Album Löschen #################

    def deletAlbumDashboard(self):

        self.removeAllWidgets()
        
        taskLabel = ctk.CTkLabel(self.mainFrame, text='Album Löschen:', font=('Arial', 12))
        taskLabel.pack(pady=5, padx=10)

        self.deletButton = ctk.CTkButton(self.mainFrame, text='Anzeigen',command=self.showAlbumsWindow) 
        self.deletButton.pack(pady=10)
    
    def showAlbumsWindow(self):

        # Neues CTk-Fenster erstellen
        albumToWindow = ctk.CTkToplevel(self.mainFrame)
        albumToWindow.title('Alben anzeigen')
        albumToWindow.geometry('400x300')

        albumToWindow.lift()
        albumToWindow.attributes('-topmost', True)
        albumToWindow.resizable(False, False)

        
        titleLabel = ctk.CTkLabel(albumToWindow, text='Welches Album wollen sie Löschen:', font=('Arial', 16))
        titleLabel.pack(pady=10)

        
        albumFrame = ctk.CTkFrame(albumToWindow)
        albumFrame.pack(fill='both', expand=True, padx=10, pady=10)

        # Anzeigen aller Alben im neuen Fenster
        for album in AlbumManager.albumList:
            albumButton = ctk.CTkButton(
                albumFrame,
                text=f'{album['title']} by {album['artist']}',
                command=lambda a=album: self.confirmAlbumDelete(a, albumToWindow)
            )
            albumButton.pack(fill='x', pady=5, padx=5)

    def confirmAlbumDelete(self, album, parentWindow):

        # Bestätigungsdialog
        confirm = messagebox.askyesno(
            title='Album löschen',
            message=f'Möchten Sie das Album \'{album['title']}\' von {album['artist']} wirklich löschen?'
        )

        if confirm:
            self.albumManager.deleteAlbum(album)
            messagebox.showinfo('Erfolg', f'Das Album \'{album['title']}\' wurde gelöscht.')
            
            # Aktualisiere die Anzeige
            parentWindow.destroy()
            self.showAlbumsWindow()
                    
############## Interface Track Hinzufügen ################                                         
            
    def addTrackDashboard(self):
        # Entferne vorhandene Widgets
        self.removeAllWidgets()
        
        
        titleLabel = ctk.CTkLabel(self.mainFrame, text='Track zum Album hinzufügen', font=('Arial', 16))
        titleLabel.pack(pady=10)
        
        # Auswahl für ein Album
        albumLabel = ctk.CTkLabel(self.mainFrame, text='Wähle ein Album:', font=('Arial', 12))
        albumLabel.pack(pady=5)
        
        self.selectedAlbumVar = ctk.StringVar()
        albumOptions = [f'{album['id']} - {album['title']}' for album in self.albumManager.albumList]
        albumDropdown = ctk.CTkOptionMenu(self.mainFrame, values=albumOptions, variable=self.selectedAlbumVar)
        albumDropdown.pack(pady=5)

        
        trackNameLabel = ctk.CTkLabel(self.mainFrame, text='Track Name:', font=('Arial', 12))
        trackNameLabel.pack(pady=5)
        self.trackNameVar = ctk.StringVar()
        trackNameEntry = ctk.CTkEntry(self.mainFrame, textvariable=self.trackNameVar)
        trackNameEntry.pack(pady=5)

        
        trackLengthLabel = ctk.CTkLabel(self.mainFrame, text='Track Länge (MM:SS):', font=('Arial', 12))
        trackLengthLabel.pack(pady=5)
        self.trackLengthVar = ctk.StringVar()
        trackLengthEntry = ctk.CTkEntry(self.mainFrame, textvariable=self.trackLengthVar)
        trackLengthEntry.pack(pady=5)


        self.addTrackButton = ctk.CTkButton(self.mainFrame,text='Hinzufügen',state='disabled',command=self.saveTrackToDB)
        self.addTrackButton.pack(pady=10)

        self.trackLengthVar.trace_add("write", self.inputTrackMonitoring)

    def inputTrackMonitoring(self,*args):

        trackLength = self.trackLengthVar.get().strip()
        trackName = self.trackNameVar.get().strip()

        try:
            if ':' in trackLength:
                minutes, seconds = map(int, trackLength.split(':'))
                if minutes >= 0 and 0 <= seconds < 60:
                    self.addTrackButton.configure(state='normal' if trackName else 'disabled')
                    return
        except ValueError:
            pass

        self.addTrackButton.configure(state='disabled')

    def saveTrackToDB(self):
        
        albumChoice = self.selectedAlbumVar.get()
        trackName = self.trackNameVar.get().strip()
        trackLength = self.trackLengthVar.get().strip()

        # Album-ID extrahieren
        albumID = int(albumChoice.split(' - ')[0])

        # Track hinzufügen
        self.albumManager.addTrack(albumID, trackName, trackLength)

############# Interface Track Löschen ############

    def deleteTrackDashboard(self):
        
        self.removeAllWidgets()

        titleLabel = ctk.CTkLabel(self.mainFrame, text='Track löschen', font=('Arial', 16))
        titleLabel.pack(pady=10)

        albumLabel = ctk.CTkLabel(self.mainFrame, text='Wähle ein Album:', font=('Arial', 12))
        albumLabel.pack(pady=5)

        self.selectedAlbumVar = ctk.StringVar()
        albumOptions = [f"{album['id']} - {album['title']}" for album in self.albumManager.albumList]
        albumDropdown = ctk.CTkOptionMenu(self.mainFrame, values=albumOptions, variable=self.selectedAlbumVar, command=self.updateTrackDropdown)
        albumDropdown.pack(pady=5)

        trackLabel = ctk.CTkLabel(self.mainFrame, text='Wähle einen Track:', font=('Arial', 12))
        trackLabel.pack(pady=5)

        self.selectedTrackVar = ctk.StringVar()
        self.trackDropdown = ctk.CTkOptionMenu(self.mainFrame, variable=self.selectedTrackVar)
        self.trackDropdown.pack(pady=5)

        
        deleteTrackButton = ctk.CTkButton(self.mainFrame, text='Löschen',command=self.confirmTrackDeletion)
        deleteTrackButton.pack(pady=10)

    def updateTrackDropdown(self, selectedAlbum):
        # Aktualisiere die Dropdown-Liste für Tracks basierend auf dem ausgewählten Album
        albumID = int(selectedAlbum.split(' - ')[0])
        tracks = next(album['tracks'] for album in self.albumManager.albumList if album['id'] == albumID)
        trackOptions = [f"{track['id']} - {track['title']}" for track in tracks]
        self.trackDropdown.configure(values=trackOptions)
        self.selectedTrackVar.set('') 
        
    def confirmTrackDeletion(self):
    
        selectedTrack = self.selectedTrackVar.get()
        if not selectedTrack:
            messagebox.showerror('Fehler', 'Kein Track ausgewählt!')
            return
        trackID = int(selectedTrack.split(' - ')[0])
        self.albumManager.deletTrack(trackID)

############# Interface Album Ausgeben ################

    def albumToDisplay(self):
            
        self.removeAllWidgets()

           
        filterLabel = ctk.CTkLabel(self.mainFrame, text='Album Anzeigen:', font=('Arial', 14))
        filterLabel.pack(pady=10)

            
        self.selectionVar = ctk.StringVar()
        comboBox = ctk.CTkComboBox(
            self.mainFrame,
            variable=self.selectionVar,
            values=['Alle anzeigen', 'Ein Album anzeigen'],
            command=self.selectionChoice
        )
        comboBox.pack(pady=10)
        comboBox.set('Alle anzeigen')  

            
        self.showButton = ctk.CTkButton(self.mainFrame, text='Anzeigen')
        self.showButton.pack(side='bottom', pady=10)

            
        self.selectionChoice('Alle anzeigen')

    def selectionChoice(self, choice):
            
        if choice == 'Alle anzeigen':
            self.showButton.configure(
                command=lambda: self.showAlbumWindow(self.albumManager.showAllAlbums())
            )
        elif choice == 'Ein Album anzeigen':
            self.showButton.configure(
                command=self.albumsForShowWindow
            )

    def albumsForShowWindow(self):
       
        albumToWindow = ctk.CTkToplevel(self.mainFrame)
        albumToWindow.title('Album auswählen')
        albumToWindow.geometry('400x300')

        
        albumToWindow.lift()
        albumToWindow.attributes('-topmost', True)
        albumToWindow.resizable(False, False)

        
        titleLabel = ctk.CTkLabel(albumToWindow, text='Welches Album möchten Sie anzeigen?', font=('Arial', 16))
        titleLabel.pack(pady=10)

        
        albumFrame = ctk.CTkFrame(albumToWindow)
        albumFrame.pack(fill='both', expand=True, padx=10, pady=10)

       
        for albumData in self.albumManager.albumList:
            albumButton = ctk.CTkButton(
                albumFrame,
                text=f'{albumData["title"]} von {albumData["artist"]}',
                command=lambda album_id=albumData['id']: self.showAlbumWindow(self.albumManager.showOneAlbum(album_id))
            )
            albumButton.pack(fill='x', pady=5, padx=5)

    def showAlbumWindow(self, showData):
            
        albumWindow = ctk.CTkToplevel(self.mainFrame)
        albumWindow.title('Albumdaten anzeigen')
        albumWindow.geometry('500x400')

            
        albumWindow.lift()
        albumWindow.attributes('-topmost', True)
        albumWindow.resizable(False, False)

            
        scrollableFrame = ctk.CTkScrollableFrame(albumWindow, width=380, height=300)
        scrollableFrame.pack(pady=10, padx=10, fill='both', expand=False)

            
        if isinstance(showData, list):
            for album in showData:
                textLabel = ctk.CTkLabel(scrollableFrame, text=str(album), justify='left', font=('Arial', 12))
                textLabel.pack(anchor='w', pady=5, padx=10)
        else:
            textLabel = ctk.CTkLabel(scrollableFrame, text=str(showData), justify='left', font=('Arial', 12))
            textLabel.pack(anchor='w', pady=5, padx=10)

            
        closeButton = ctk.CTkButton(albumWindow, text='Schließen', command=albumWindow.destroy)
        closeButton.pack(pady=10)
