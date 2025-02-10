from datetime import timedelta


class Album:

    def __init__(self,albumTitle,artist):
        self.albumTitle= albumTitle
        self.artist=artist
        self.tracks=[]
    

    @classmethod
    def albumObjFactory(cls, albumData):
        album = cls(albumData['title'], albumData['artist'])
        # Tracks hinzufügen
        for track in albumData.get('tracks', []):
            album.tracks.append((track['id'], track['title'], track['length']))
        return album



    def calculateTotalLength(self):
    # Berechnung der Gesamtlänge in Sekunden
        totalSeconds = 0
        for track in self.tracks:
            try:
                minutes, seconds = map(int, track[2].split(":"))  # Zugriff auf track[2], nicht track["length"]
                totalSeconds += minutes * 60 + seconds
            except (ValueError, IndexError):
                print(f"Fehlerhafte Länge für Track: {track}")
                continue

        # Umrechnung in Minuten und Sekunden
        total_duration = timedelta(seconds=totalSeconds)
        return str(total_duration)[2:]  # Format MM:SS (Entfernt Mikrosekunden)Mi


    def __str__(self):
     
        totalLength = self.calculateTotalLength() if self.tracks else '00:00'
        albumInfo = f'Album: {self.albumTitle}\nKünstler: {self.artist}\nGesamt Länge: {totalLength}\n'
        trackInfo = '\n'.join([f'  Track {_+1}: {track}' for _, track in enumerate(self.tracks)])
        return albumInfo + trackInfo+'\n'+'*'*40