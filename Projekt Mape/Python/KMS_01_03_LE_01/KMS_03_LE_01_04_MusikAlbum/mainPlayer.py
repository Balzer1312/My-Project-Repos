from Libraryclass import AlbumLibary
from trackclass import Track
from Albumclass import Album

def main():
    libary= AlbumLibary()
    libary.loadJson()

    while True:
        print('\nDeine Album Sammlung')
        print('1 für Album Verwaltung ')
        print('2 für Album Anzeigen lassen')
        print('3 für Programm beenden')

        try:
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                albumManagment(libary)
            elif choice == 2:
                albumOutput(libary)
            elif choice == 3:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')


def albumManagment(libary):
    

    while True:
        print('\nWillkomen in der Album Verwaltung')
        print('1 für Album Hinzufügen')
        print('2 für Album Löschen')
        print('3 für Track Hinzufügen')
        print('4 für Track Löschen')
        print('5 für zurück in Hauptmenü')

        try:
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                albumName = str(input('Bitte Album Namen angeben: '))
                artistName= str(input('Bitte Künstler angeben: '))
                libary.addAlbum(Album(albumName, artistName))
                continue
            elif choice == 2:
                albumName = str(input('Bitte den Namen des zu löschenden Albums angeben: '))
                libary.removeAlbum(albumName)
                continue
            elif choice == 3:
                albumName=str(input('Zu welchen Album soll der Track Hinzugefügt werden?: '))
                trackName= str(input('Bitte Track Namen angeben: '))
                trackLength= str(input('Bitte Track Dauer (Bsp.: 03:23) angeben: '))
                album=libary.getAlbum(albumName)
                if album:
                    album.addTrack(Track(trackName,trackLength))
                    libary.saveJson()
                    print(f'Der Track {trackName} wurde dem Album {albumName} hinzugefügt')

                else:
                        print('Album wurde nicht gefunden')
                continue     
            elif choice == 4:
                print('Bitte Album für das löschen des Tracks angeben.\n')
                albumName = str(input('Bitte Album Namen angeben: '))
                trackName = str(input('Bitte Track Namen angeben: '))
                libary.removeTrack(albumName, trackName)
                libary.saveJson()
            elif choice == 5:
                break      
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')


def albumOutput(libary):

    while True:
        print('\nWillkomen zur Album Ausgabe')
        print('1 für Album Sammlung anzeigen')
        print('2 für ein Album anzeigen')
        print('3 für Zurück ins Hauptmenü')

        try:
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                print('\nGesamte Album Sammlung:')
                print(libary.outputLibary())
                continue
            elif choice == 2:
                print('Bitte geben sie 1 ein um fortzufahen oder eine beliebige zahl um abzubrechen')
                choice= int(input('Ihre eingabe: '))
                if choice == 1:
                    albumName= str(input('Welches Album wollen sie Ausgeben: '))
                    album= libary.getAlbum(albumName)
                    if album:
                        print('\n\n')
                        print(album)
                    else:
                        print('Album wurde nicht gefunden')
                else:
                    continue
            elif choice == 3:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')

    

    

if __name__ == '__main__':
    main()