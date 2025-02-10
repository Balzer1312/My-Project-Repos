from courseAdministrationclass import providerManagement, Course
from  MemberClass import People


providerManagement.persoLoadJson()
providerManagement.courseLoadJson() 




#providerManagement.saveFilteredToCsv(
#    filterKey='type',
#    filterValue='Client',
#)


providerManagement.persoSaveToCsv()

def main():
    
    providerManagement.persoLoadJson()
    providerManagement.courseLoadJson()  
   
    while True:
        print('\nVerwaltung für Kurs Anbieter')
        print('1 für Verwaltung der Mitglieder und Kurse')
        print('2 für Ausgabe der Mitglieder')
        print('3 für Mitglieder Datei erstellen')
        print('4 für Programm beenden')

        try:
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                managmantForMembers()
            elif choice == 2:
                showMember()
            elif choice == 3:
                saveMemberData()
            elif choice == 4:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')


def managmantForMembers():
    
    while True:
        print('\nVerwaltung für Mitglieder ')
        print('1 für Kunden(Schüler) und Mitarbeiter Hinzufügen oder Entfernen')
        print('2 für Kurse Hinzufügen oder Entfernen')
        print('3 für Zurück zum Hauptmenü')


        try:
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                personRegistration()
            elif choice == 2:
                coursManagmant()
            elif choice == 3:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')
           

def personRegistration():


    print('\nHandelt es sich um einen Kunden oder einem Mitarbeiter?')
    print('1 für Mitarbeiter')
    print('2 für Kunden(Schüler)')
    print('3 für Mitglied entfernen')
    print('4 für zurück zur Verwaltung')

    try:
        choice = int(input('Ihre Eingabe: '))
        newID= max(person['id']for person in People.personDataList['people'])+1 
        if choice == 1:
            membertype= 'Tutor'
            personType={
               'type': membertype,
               'id': newID,
               'name': input('Bitte Vollständigen Namen eingeben: '),
               'adress': input('Bitte Adresse angeben: '),
               'birthdate': input('Bitte Gebursdatum eingeben (DD.MM.YYYY: '),
               'specialty': input('Bitte Ihr Leherfach angeben: ')
            }
            providerManagement.addPerson(personType)

        elif choice == 2:
            membertype= 'Client'
            personType={
               'type': membertype,
               'id': newID,
               'name': input('Bitte Vollständigen Namen eingeben: '),
               'adress': input('Bitte Adresse angeben: '),
               'birthdate': input('Bitte Gebursdatum eingeben (DD.MM.YYYY): '),
               'chosenCourse': []
            }
            
            print('Geben Sie die Kurse an, die der Kunde belegen möchte. Geben Sie eine Zahl ein, um zu beenden.')
            while True:
                course = input('Kursname: ')
                if course.isdigit():
                    break
                personType['chosenCourse'].append(course)
            providerManagement.addPerson(personType)
        elif choice==3:
            id=int(input('Bitte geben sie die ID von Mitarbeiter und ihn zu entfernen: '))
            providerManagement.removeFromJson(id, People.personDataList['people'], providerManagement.persJsonFile,'id')
        elif choice == 4:
            return
        else:
            print('Ungültige Eingabe')
    except ValueError:
        print('Bitte geben Sie eine Zahl ein.')
    

def coursManagmant():

    print('\nWollen sie einen Kurs entfernen oder Hinzugügen?')
    print('1 für Hinzufügen')
    print('2 für entfernen')
    print('3 für zurück zur Verwaltung')

    try:
        choice = int(input('Ihre Eingabe: '))
        newID= max(person['courseID']for person in Course.courses)+1 
        if choice == 1:
            newCourse={
                'courseID': newID,
                'courseName': input('Bitte Kurs Namen angeben: ')
            }
            providerManagement.addCourse(newCourse)
        elif choice == 2:
            id=int(input('Bitte geben sie die Kurs ID ein den sie Löschen wollen: '))
            providerManagement.removeFromJson(id, Course.courses, providerManagement.courseJsonFile,'courseID')
        elif choice == 3:
            return
        else:
            print('Ungültige Eingabe')

    except ValueError:
        print('Bitte geben Sie eine Zahl ein.')


def showMember():
        print('\nAusgabe der Mitglieder')
        print('1 für alle Mitglieder anzeigen')
        print('2 für Mitglieder nach Typ filtern (Client/Tutor)')
        print('3 für Zurück zum Hauptmenü')

        choice = int(input('Ihre Eingabe: '))
        if choice == 1:
            providerManagement.showAllPerson()
        elif choice == 2:
            print('1 für Clienten oder 2 Für Tutor Ausgabe')
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                providerManagement.showFilteredPeople('Client')
            elif choice == 2:
                providerManagement.showFilteredPeople('Tutor')
        elif choice == 3:
            return
        else:
            print('Ungültige Eingabe')

def saveMemberData():
    print('\nMitglieder Daten speichern')
    print('1 für alle Daten in CSV speichern')
    print('2 für Gefilterte Daten in CSV speichern')
    print('3 für Gefilterte CSV einlesen')
    print('4 für zurück in Hauptmenü')
    
    try:
        choice = int(input('Ihre Eingabe: '))
        if choice == 1:
            providerManagement.persoSaveToCsv()
            print('Alle Daten wurden erfolgreich gespeichert.')
        elif choice == 2:
            print('1 für Clienten oder 2 Für Tutor CSV erstellen')
            choice = int(input('Ihre Eingabe: '))
            if choice == 1:
                providerManagement.saveFilteredToCsv('Client')
            elif choice == 2:
                providerManagement.saveFilteredToCsv('Tutor')
        elif choice==3:
            providerManagement.readFilteredCsvData()
        elif choice==4:
            return
         
        else:
            print('Ungültige Eingabe')
    except ValueError:
        print('Bitte geben Sie eine Zahl ein.')

if __name__ == '__main__':
    main()
