import json
import os
from trackclass import Track
from Albumclass import Album


class AlbumLibary:
    

    def __init__(self):
        self.albumLibary=[]

    def addAlbum(self,album):
        for existingAlbum in self.albumLibary:
            if existingAlbum.albumTitle.lower() == album.albumTitle.lower():
                print(f'Das Album "{album.albumTitle}" existiert bereits.')
                return
        self.albumLibary.append(album)
        self.saveJson()

    def removeTrack(self,albumTitle,trackTitle):
        album = self.getAlbum(albumTitle)
        if album:
            album.deleteTrack(trackTitle)
            return None
        else:
            print(f'\nDas Album \'{albumTitle}\' konnte nicht gefunden werden\n')
            return None

    def removeAlbum(self, albumTitle):
        for album in self.albumLibary:
            if album.albumTitle.strip().lower() == albumTitle.strip().lower():
                self.albumLibary.remove(album)
                print(f'Das Album "{albumTitle}" wurde erfolgreich gelöscht.')
                self.saveJson() 
        print(f'Das Album "{albumTitle}" wurde nicht gefunden.')
        return None

    def getAlbum(self,albumTitle):
        for album in self.albumLibary:
            if album.albumTitle.strip().lower() == albumTitle.strip().lower():
                return album

    def loadJson(self):
        currentFile= os.path.dirname(__file__)
        jsonFile= os.path.join(currentFile, 'MusicLibary.json')
        with open(jsonFile,'r') as file:
            albumData=json.load(file)
        for album_data in albumData:
            album = Album(album_data['albumTitle'], album_data['artist'])
            for track_data in album_data['tracks']:
                album.addTrack(Track(track_data['title'],track_data['length']))
            self.addAlbum(album)

    def saveJson(self):
        currentFile= os.path.dirname(__file__)
        jsonFile= os.path.join(currentFile, 'MusicLibary.json')
        saveData=[]
        for album in self.albumLibary:
            albumData={
                'albumTitle': album.albumTitle,
                'artist' : album.artist,
                'tracks':[
                    {'title':track.title,'length':track.length} for track in album.tracks
                ]
            }
            saveData.append(albumData)
        with open(jsonFile, 'w') as file:
            json.dump(saveData, file, indent=4)
        print('Wurde der Bibliothek Hinzugefügt')

    def outputLibary(self):
        if not self.albumLibary:
            return 'Keine Alben in der Bibliothek.'
        return '\n\n'.join([str(album) for album in self.albumLibary])
