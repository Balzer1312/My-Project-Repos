import os
from JsonDateiEinlesen import readJsonFile, createInstancesFromJson
from KMS_1_03_LE_01_02_VereinVerwaltung_Balzer import (
    Chairperson, Player, Treasurer, SportTeamManagerr, Coach, AssociationMember
)

def main_menu():
    while True:
        print('\nHauptmenü:')
        print('1. Neues Mitglied erstellen')
        print('2. Alle Mitglieder anzeigen')
        print('3. Weitere Funktionen')
        print('4. Programm beenden')

        try:
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                addNewMember()
            elif choice == 2:
                AssociationMember.showAllMembers()
            elif choice == 3:
                classFunction()
            elif choice==4:
                print('Programm wird beendet.')
                break
            else:
                print('Ungültige Eingabe. Bitte erneut versuchen.')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')

def addNewMember():
    print('\nNeues Mitglied erstellen:')
    print('1. Vorsitzender')
    print('2. Spieler')
    print('3. Schatzmeister')
    print('4. Teammanager')
    print('5. Trainer')
    
    try:
        choice = int(input('Wählen Sie die Klasse des neuen Mitglieds: '))
        if choice == 1:
            newMember = Chairperson(
                memberID=int(input('Mitglieds-ID: ')),
                name=input('Name: '),
                email=input('E-Mail: '),
                entryDate=input('Eintrittsdatum (DD.MM.YYYY): '),
                administrationBody=input('Verwaltungsorgan: '),
                currentProject=input('Aktuelles Projekt: ')
            )
        elif choice == 2:
            newMember = Player(
                memberID=int(input('Mitglieds-ID: ')),
                name=input('Name: '),
                email=input('E-Mail: '),
                entryDate=input('Eintrittsdatum (DD.MM.YYYY): '),
                teamName=input('Teamname: '),
                playPosition=input('Spielposition: '),
                playerNumber=int(input('Spielernummer: '))
            )
        elif choice == 3:
            newMember = Treasurer(
                memberID=int(input('Mitglieds-ID: ')),
                name=input('Name: '),
                email=input('E-Mail: '),
                entryDate=input('Eintrittsdatum (DD.MM.YYYY): '),
                administrationBody=input('Verwaltungsorgan: '),
                financeArea=input('Finanzbereich: ')
            )
        elif choice == 4:
            newMember = SportTeamManagerr(
                memberID=int(input('Mitglieds-ID: ')),
                name=input('Name: '),
                email=input('E-Mail: '),
                entryDate=input('Eintrittsdatum (DD.MM.YYYY): '),
                administrationBody=input('Verwaltungsorgan: '),
                event=input('Event: ')
            )
        elif choice == 5:
            newMember = Coach(
                memberID=int(input('Mitglieds-ID: ')),
                name=input('Name: '),
                email=input('E-Mail: '),
                entryDate=input('Eintrittsdatum (DD.MM.YYYY): '),
                teamName=input('Teamname: '),
                experience=int(input('Erfahrung (in Jahren): ')),
                mantra=input('Mantra: '),
                trainingsDate=input('Trainingsdatum (DD.MM.YYYY): ')
            )
        else:
            print('Ungültige Auswahl. Zurück zum Hauptmenü.')
            return
        
        print('\nNeues Mitglied erfolgreich erstellt:')
        newMember.showMember()

    except ValueError:
        print('Ungültige Eingabe. Bitte erneut versuchen.')

def classFunction():
    print('\nWas wollen Sie ausgeben?')
    print('1. Meeting setzen')
    print('2. Finanzbericht')
    print('3. Sport Event')
    print('4. Trainingsplan')
    print('5. Verletzte')

    try:
        choice = int(input('Wählen Sie eine Funktion: '))
        
        if choice == 1:
            for member in AssociationMember.allMemberContainer:
                if isinstance(member, Chairperson):
                    member.setMeeting()
        
        elif choice == 2:
            for member in AssociationMember.allMemberContainer:
                if isinstance(member, Treasurer):
                    member.generateReport()
        
        elif choice == 3:
            for member in AssociationMember.allMemberContainer:
                if isinstance(member, SportTeamManagerr):
                    member.setSportEvent()
        
        elif choice == 4:
            for member in AssociationMember.allMemberContainer:
                if isinstance(member, Coach):
                    member.setTrainingPlan()
        
        elif choice == 5:
            print('\nVerfügbare Spieler:')
            for member in AssociationMember.allMemberContainer:
                if isinstance(member, Player):
                    print(f'ID: {member.memberID}, Name: {member.name}')
            
            try:
                player_id = int(input('\nGeben Sie die ID des Spielers ein, den Sie als verletzt melden möchten: '))
                player_found = False
                for member in AssociationMember.allMemberContainer:
                    if isinstance(member, Player) and member.memberID == player_id:
                        member.SetInjured()
                        player_found = True
                        break
                
                if not player_found:
                    print('Kein Spieler mit dieser ID gefunden.')
            except ValueError:
                print('Ungültige Eingabe. Bitte eine gültige ID eingeben.')
        
        else:
            print('Ungültige Auswahl. Zurück zum Hauptmenü.')
    
    except ValueError:
        print('Ungültige Eingabe. Bitte erneut versuchen.')



if __name__ == '__main__':
    # JSON-Daten laden und Instanzen erstellen
    currentFile = os.path.dirname(__file__)
    jsonFilePath = os.path.join(currentFile, 'VereinsObjekte.json')
    jsonData = readJsonFile(jsonFilePath)
    createInstancesFromJson(jsonData)

    # Hauptmenü starten
    main_menu()


