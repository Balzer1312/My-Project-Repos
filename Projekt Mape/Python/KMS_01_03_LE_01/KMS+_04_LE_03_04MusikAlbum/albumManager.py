import os
import csv
from tkinter import messagebox

from DButilis import DBManager
from albumClass import Album


class AlbumManager():

    albumList=[]
    freeIDs=[]

############## Daten werden von DB geladen ###########
    def getAlbumWithTracks(cls):
        cls.albumList.clear()

        albumQuery = 'SELECT id, title, artist FROM albums'
        albums = DBManager.fetchData(albumQuery)

        trackQuery = 'SELECT id, title, length, album_id FROM tracks'
        tracks = DBManager.fetchData(trackQuery) 

        if not albums or not tracks:
            messagebox.showerror('Fehler', 'Keine Daten gefunden')
            return
        
        for album in albums:
            albumID, title, artist = album
            albumTracks = [
                {'id': track[0], 'title': track[1], 'length': track[2]}
                for track in tracks if track[3] == albumID
            ]
            
            cls.albumList.append({
                    'id': albumID,
                    'title': title,
                    'artist': artist,
                    'tracks': albumTracks
                })

################ verfügbarkeit der IDs für Ablben Prüfen ##################           
 
    @classmethod
    def availableID(cls):
        # Prüfe, ob eine freigegebene ID verfügbar ist
        if cls.freeIDs:
            return cls.freeIDs.pop(0)  # Nimm die erste freie ID
        # Falls keine freie ID verfügbar ist, generiere eine neue
        if not cls.albumList:
            return 1  # Starte mit 1, wenn die Liste leer ist
        return max(album['id'] for album in cls.albumList) + 1 

################ Anlegen und Löschen von Alben #################

    #Album Anlegen
    @classmethod
    def addAlbum(cls, title,artist):
        
        newID = cls.availableID()
        
        newAlbum={
            'id':newID,
            'title':title,
            'artist':artist,
            'tracks':[]
        }

        result=DBManager.pushToDataBase(newAlbum) 
        if result:
            cls.albumList.append(newAlbum)
            messagebox.showinfo('Erfolg','Album erfolgreich in die DB geladen!')
            cls.getAlbumWithTracks
            return
        messagebox.showerror('Fehler', f'Fehler beim übertragen!')
        return 
    
    #Album Löschen
    @classmethod
    def deleteAlbum(cls, album):
    
        for albumID in cls.albumList:
                if albumID['id'] == album['id']:
                    cls.albumList.remove(albumID)
                    cls.freeIDs.append(albumID)
    
        result= DBManager.deletAlbumFromDB(album)
        if result:
            cls.getAlbumWithTracks
            return
        messagebox.showerror('Fehler', f'Fehler beim übertragen!')
        return

############# Track Löschen und Hinzufügen #################
   #Track Hinzufügen
    @classmethod
    def addTrack(cls,albumID,title,length):

        
        checkTrackIDs = [
            track['id'] for album in cls.albumList for track in album['tracks']
        ]
        trackID = max(checkTrackIDs, default=0) + 1

        newTrack={
            'id': trackID,
            'title': title,
            'length': length,
            'album_id': albumID
        }

        result= DBManager.addTrackToDB(newTrack)
        if result:
            messagebox.showinfo('Erfolg','Track erfolgreich in die DB geladen!')
            cls.getAlbumWithTracks
            return
        messagebox.showerror('Fehler', f'Fehler beim übertragen!')
        return
    
    #Track Löschen
    @classmethod
    def deletTrack(cls,trackID):

        for album in cls.albumList:
            for track in album['tracks']:
                if track['id'] == trackID:
                    album['tracks'].remove(track) 

        result= DBManager.deleteTrackFromDB(trackID)
        if result:
            messagebox.showinfo('Erfolg','Track erfolgreich von der DB gelöscht!')
            cls.getAlbumWithTracks
            return
        messagebox.showerror('Fehler', f'Fehler beim übertragen!')
        return
    
################# Alben am Display Darstellen ######################

    #Alle ablen Zeigen 
   

    @classmethod
    def showAllAlbums(cls):
        # Alle Alben in AlbumObjekte konvertieren
        albumsAsObjects = [Album.albumObjFactory(album) for album in cls.albumList]
        return albumsAsObjects

    @classmethod
    def showOneAlbum(cls, albumID):
        # Finde das Album mit der gegebenen ID und erstelle ein Objekt
        albumData = next((album for album in cls.albumList if album['id'] == albumID), None)
        return Album.albumObjFactory(albumData)
        
