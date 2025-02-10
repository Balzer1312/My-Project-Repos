from datetime import datetime
import re
def main():
    records = [
        'ID:4327131297|Vorname:Keevin|Nachname:Ballzer|Geburtstag:13.12.97|Telefonnummer:436645221213|Adresse:Musterweg 18',
        '(V)|Vorname:Muster|Nachname:Mann|Telefonnummer:431211221212|Adresse:Musterstraße 60',
        'ID:6089131297|Vorname:Erik|Nachname:Gruber|Geburtstag:14.06.92|Telefonnummer:4366452156213|Adresse:Mustergasse 54',
        '(V)|Vorname:Gunter|Nachname:Wald|Telefonnummer:43121626672|Adresse:Musterberg 32'
    ]
    print('Willkommen zur Personen erfassung')
    while True:
        print('\nSind sie ein Mitarbeiter oder ein Besucher?\nDrücken sie: ')
        userInput = input('(1)Für Mitarbeiter/Besucher einlesen oder Daten bearbeiten.\n(2)Für Ausgabe der Mitarbeiter/Besucher Liste:\n ')
        print(userInput)
        if int(userInput) == 1:
            while True:
                print('\nWillkommen!\nWollen sie Besucher oder Mitarbeiter einlesen?\nDrücken Sie: \n(1)Für Mitarbeiter/Besucher einlesen.\n(2)Für Mitarbeiter Daten ändern.\n(3)Um zurück ins Hauptmenü zu kommen.')
                userInput = int(input('Ihre Eingabe: '))
                if userInput not in [1,2,3]:
                    print('Falsche eingabe')
                elif userInput==3:
                    break
######################### Mitarbeiter oder Besucher einlesen ######################################
                if userInput== 1:
                    captureChoice=0
                    while True:
                        print('\nWollen sie ein Besucher oder Mitarbeiter daten Anlegen?\nDrücken Sie: \n(1)Für Mitarbeiter\n(2)Für Besucher\n(3)Um zurück ins Menü zu kommen')
                        userInput=int(input('Ihre Eingabe: '))
                        if userInput not in [1,2,3]:
                            print('Falsche Eingabe')
                        elif userInput==1:
                            captureChoice=1
                        elif userInput==2:
                            captureChoice=0
                        elif userInput==3:
                            break
                        if userInput==1 or userInput==2:
                            while True:
                                fistname=input('Bitte Vornamen eingeben: ')
                                result=re.search(r'[0-9!§$%&()=?\[\]{};@#~<>|^°+*ÄäÖöÜüẞß]',fistname)    #Validierung des Vornamen
                                if result:
                                    print('Falsche Eingabe')
                                else:
                                    break
                            while True:
                                lastname=input('Bitte Nachnamen eingeben: ')
                                result = re.search(r'[0-9!§$%&()=?\[\]{};@#~<>|^°+*ÄäÖöÜüẞß]', lastname)  #Validierung des Nachnamen
                                if result:
                                    print('Falsche Eingabe')
                                else:
                                    break
                            while True:
                                location=input('Bitte Adresse eingeben:')
                                result=re.search(r'[!§$%&()=?\[\]{};@#~<>|^°+*]', location)   #Validierung der Adresse
                                if result:
                                    print('Falsche Eingabe')
                                else:
                                    break
                            while True :
                                contact=input('Bitte Telefonnummer eingeben: ')
                                result=re.search(r'[!§$%&()=?\[\]{};@#~<>| ^°+*A-Za-zÄäÖöÜüẞß]',contact)   #Validierung der Telefonnummer
                                if result:
                                    print('Falsche Eingabe')
                                else:
                                    break
                            if captureChoice==1:
                                while True :
                                    birthday= input('Bitte Geburtstag eingeben(tt.mm.jj) :')
                                    try:
                                        datetime.strptime(birthday,"%d.%m.%y")  # Validierung des Formats des Geb. datums
                                        break
                                    except ValueError:
                                        print('Bitte geben sie das richtige format ein:(TT.MM.JJ)!')
                                while True:
                                    sozialNumb= input('Bitte Sozial Versicherungsnummer: ')
                                    result= re.search(r'[!§$%&()=?\[\]{};@#~<>|^°+*A-Za-zÄäÖöÜüẞß]',sozialNumb)  #Validierung der Sozial-Versicherungsnummer
                                    if result:
                                        print('Falsche Eingabe')
                                    else:
                                        break
                            if captureChoice==1:
                                print('\nSie Haben jetzt ein Mitarbeiter konto!\n')
                                records.append(f'ID:{sozialNumb}|Vorname:{fistname}|Nachname:{lastname}|Geburtstag:{birthday}|Telefonnummer:{contact}|Adresse:{location}')  #Erstellen eines Datensatzes(String) für Mitarbeiter
                            elif captureChoice==0:
                                print('\nSie Haben sich als Besucher eingetragen\n')
                                records.append(f'(V)|Vorname:{fistname}|Nachname:{lastname}|Telefonnummer:{contact}|Adresse:{location}') #Erstellen eines Datensatzes(String) für Besucher

######################################## Mitarbeiter Daten ändern #########################################################################################################
                elif userInput==2:
                    while True:
                        print('\nBitte geben sie Ihre ID an\nDrücken Sie: \n(1)Für zurück ins Hauptmenü\n')
                        userInput = input('Ihre Eingabe: ')  # Der Mitarbeiter muss seine id angeben, um den datensatz zu finden
                        if int(userInput)==1:
                            break
                        exitloops = True
                        while exitloops:
                            for record in records:  # die schleifen geht die datensätze durch
                                if not re.search(f'ID:{userInput}',record) or len(userInput)!=10:  # Sucht, ob die ID in den Datensätzen nicht existiert, um in dem fall einen fehler ausgibt
                                    print('\nEingabe Ungültig')
                                    exitloops = False
                                    break
                                else:
                                    employID = userInput
                                    print('\nLass uns die Daten verändern\n\n')
                                    for i, record in enumerate(records):
                                        if re.search(f'ID:{employID}', record):
                                            print("\nAktueller Datensatz:")
                                            print(record)
                                            if input("Vorname ändern? (j/n): ").lower() == 'j':
                                                while True:
                                                    firstname = input("Neuer Vorname: ")
                                                    result = re.search(r'[0-9!§$%&()=?\[\]{};@#~<>|^°+*ÄäÖöÜüẞß]', firstname)  # Validierung des neuen Vornamen
                                                    if result:
                                                        print('Falsche Eingabe')
                                                    else:
                                                        record = re.sub(r'Vorname:[A-Za-z]+',f'Vorname:{firstname}',record)  # Ersetzt den alten Vornamen mit den neuen
                                                        break
                                            if input("Nachname ändern? (j/n): ").lower() == 'j':
                                                while True:
                                                    lastname = input("Neuer Nachname: ")
                                                    result = re.search(r'[0-9!§$%&()=?\[\]{};@#~<>|^°+*ÄäÖöÜüẞß]',lastname)  # Validierung des neuen Nachnamen
                                                    if result:
                                                        print('Falsche Eingabe')
                                                    else:
                                                        record = re.sub(r'Nachname:[A-Za-z]+',f'Nachname:{lastname}',  record)  # Ersetzt den alten Nachnamen mit dem neuen
                                                        break
                                            if input("Telefonnummer ändern? (j/n): ").lower() == 'j':
                                                while True:
                                                    contact = input("Neue Telefonnummer: ")
                                                    result = re.search( r'[!§$%&()=?\[\]{};@#~<>| ^°+*A-Za-zÄäÖöÜüẞß]', contact)  # Validierung der neuen Adresse
                                                    if result:
                                                        print('Falsche Eingabe')
                                                    else:
                                                        record = re.sub(r'Telefonnummer:\d+', f'Telefonnummer:{contact}', record)  # Ersetzt die alte Telefonnummer mit der neuen
                                                        break
                                            if input("Adresse ändern? (j/n): ").lower() == 'j':
                                                while True:
                                                    location = input("Neue Adresse: ")
                                                    result = re.search(r'[!§$%&()=?\[\]{};@#~<>|^°+*]', location)  # Validierung der neuen Adresse
                                                    if result:
                                                        print('Falsche Eingabe')
                                                    else:
                                                        record = re.sub(r'Adresse:.+', f'Adresse:{location}',record)  # Ersetzt die alte Adresse mit der neuen
                                                        break
                                            records[i] = record
######################################## Ausgabe der Mitarbeiter und der Besucher ###################################################################
        elif int(userInput)==2:
            if not records:
                break
            print('\nWillkommen zur Ausgabe\n\nDrücken Sie: \n(1)Für alle Mitarbeiter ausgeben\n(2)Für alle Besucher ausgeben\n')
            userInput=int(input('Ihre Eingabe: '))
            if userInput not in [1,2]:
                print('Falsche Eingabe')
            elif int(userInput) ==1:
                employRecords = [record for record in records if re.search(r'ID:\d+', record)]  #Die Liste(records) wird durchsucht, um die datensätze mit einer ID zu filtern und employRecords(Liste) mit dem strings zu initialisieren
                for record in employRecords: #Die Schleife geht jeden datensatz jeh nach iterationen im EmployRecords durch
                    idMatch = re.search(r'ID:(\d+)', record)  #re.search(r'ID:(\d+)', record) sucht die richtige anordnung im string und speichert den string in idMatch.
                    birthdate = re.search(r'Geburtstag:(\d{2}\.\d{2}\.\d{2})', record)
                    firstnameMatch = re.search(r'Vorname:([A-Za-z]+)', record)
                    lastnameMatch = re.search(r'Nachname:([A-Za-z]+)', record)
                    contactMatch =re.search(r'Telefonnummer:(\d+)', record)
                    locationMatch = re.search(r'Adresse:(.+)', record)
                    #Ausgabe der Mitarbeiter
                    print(f'\n\nID: {idMatch.group(1)}\nVorname: {firstnameMatch.group(1)}\nNachname: {lastnameMatch.group(1)}\nGeburtstag: {birthdate.group(1)}\nTelefonnummer: +{contactMatch.group(1)}\nAdresse: {locationMatch.group(1)}\n--------------------------')
            elif userInput==2:
                visitorRecords=[record for record in records if not re.search(r'ID:\d+', record)] #Die Liste(records) wird durchsucht, um die datensätze ohne einer ID zu filtern und visitorRecords(Liste) mit dem strings zu initialisieren
                visitorCount = 0
                for record in visitorRecords: #Die Schleife geht jeden datensatz jeh nach iterationen im visitorRecords durch
                    visitorCount +=1
                    firstnameMatch = re.search(r'Vorname:([A-Za-z]+)', record)
                    lastnameMatch = re.search(r'Nachname:([A-Za-z]+)', record)
                    contactMatch = re.search(r'Telefonnummer:(\d+)', record)
                    locationMatch = re.search(r'Adresse:(.+)', record)
                    #Ausgabe der Besucher
                    print(f'\n\nBesucher: {visitorCount}\nVorname: {firstnameMatch.group(1)}\nNachname: {lastnameMatch.group(1)}\nTelefonnummer: +{contactMatch.group(1)}\nAdresse: {locationMatch.group(1)}\n--------------------------')
                visitorCount=0
        else:
            print('Programm wird Beendet')
            break





if __name__ == "__main__":
    main()