from datetime import timedelta
from trackclass import Track

class Album:

    def __init__(self,albumTitle,artist):
        self.albumTitle= albumTitle
        self.artist=artist
        self.tracks=[]

    def addTrack(self,track):

        if isinstance(track,Track):
            for existingTrack in self.tracks:
                if existingTrack.title.lower() == track.title.lower():
                    print(f'Der Track "{track.title}" existiert bereits in diesem Album.')
                    return
            self.tracks.append(track)
        else:
            print('Ein Fehler ist aufgetreten.')

    def deleteTrack(self, trackTitle):

        for track in self.tracks:
            if track.title == trackTitle:
                self.tracks.remove(track)
                print(f'Der Track \'{trackTitle}\' wurde gelöscht.')
                return True
        print(f' Der Track \'{trackTitle}\' konnte nicht gefunden werden.')
        return False

    def albumLength(self):

        wholeLength= timedelta()
        for track in self.tracks:
            min, sec = map(int,track.length.split(':'))  
            wholeLength += timedelta(minutes=min,seconds=sec)

        totalSec= int(wholeLength.total_seconds())
        hrs, remainder = divmod(totalSec,3600)
        min, sec = divmod(remainder,60)

        return f'{hrs:02}:{min:02}:{sec:02}'
    
    def __str__(self):

        totalLength= self.albumLength()
        albumInfo = f'Album: {self.albumTitle}\nKünstler: {self.artist}\nGesamt Länge: {totalLength}\n\n'
        trackInfo = '\n'.join([f'  Track {_+1}: {track}' for _, track in enumerate(self.tracks)])
        return albumInfo + trackInfo+'\n'+'*'*40


    