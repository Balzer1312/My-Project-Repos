from datetime import datetime
import re

def main():

       personnel={}
       visitor={}
       count=0
       invalidName = r'[!"§$%&/()=?0-9\[\]{}\\,.;:@#~<>|^°+*]'
       invalidChar = r'[!§$%&()=?\[\]{}\\;@#~<>|^°+*]'
       invalidSoizalNumb =r'[!§$%&()=?\[\]{}\/;@#~<>|^°+*\'A-Za-zÄäÖöÜüẞß]'

       print('Willkommen im Musterunternehmen!')

       while True:

           print('Sind Sie ein Besucher oder ein Mitarbeiter?\n1. für Mitarbeiter\n2.Für Besucher\n3.für Ausgabe der Mitarbeiter\n4.für Ausgabe Besucher\nAlles andere für beenden\n\n\n')
           userInput = int(input('Bitte um Ihre eingabe: '))

           #Mitarbeiter Menü
           if userInput==1:
               while True:
                   #Benutzer wird gefragt, ob er schon ein Konto besitzt
                   print('\nHaben sie schon ein Benutzer konto?\n1.für Ja\n2.für Nein\n3. um Zurück ins Menü zu kommen\n\n')
                   userInput = int(input('Bitte um Ihre eingabe:'))
                   if userInput == 1:  #Benutzer hat schon ein konto

                       while True:
                           print('\nWillkommen Mitarbeiter\nWenn sie zurück ins Menü wollen, dann geben Sie \"3\" ein.\nBitte geben sie ihre Sozialversicherungsnummer an:')
                           userInput = input('Bitte um Eingabe: ')
                           if userInput in personnel:
                               userId = userInput
                               userInfo = personnel[userInput]
                               while True:
                                   print(f'Willkommen {userInfo['name']}!\n Wollen sie ihre Daten anzeigen oder bearbeiten?\n1. für anzeigen lassen.\n2. für bearbeiten.\n3. für zurück ins Menü.\n\n')
                                   userInput=input('Ihre Eingabe: ')
                                   if int(userInput)==1:
                                       print(f'Hier ihre Daten : \n\nID: {userId}\nName: {userInfo['name']}\nGeb.Datum: {userInfo['birthDate']}\nAdresse: {userInfo['location']}\nTel.: +{userInfo['contact']}\n---------------------\n\n')

                                   elif int(userInput)==2:
                                       while True:
                                           print('Was möchten sie Bearbeiten:\n1. für Namen\n2. für Adresse\n3. für Telefonnummer\n3. für zurück in Menü\n\n')
                                           userInput=input('Ihre eingabe: ')
                                           result=re.search(invalidChar, userInput)
                                           if int(userInput)==1:
                                               while True:
                                                   name = input('Bitte geben sie ihren neuen Namen ein:')
                                                   result = re.search(invalidName, name)  # Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                                                   if result:
                                                       print('Bitte einen gültigen Namen Eingeben(Vorname Nachname)')
                                                   elif len(name.strip()) == 0:  # Überprüft die eingabe leer ist
                                                       print('Bitte einen gültigen Namen Eingeben(Vorname Nachname)')
                                                   else:
                                                       print('Ist der Name Korrekt ?\n1. für Ja\nAlles andere für Nein \n')
                                                       print(f'Prüfung: {name}\n\n')  # Der Benutzer wird nochmal gefaragt, ob die eingabe korrekt ist
                                                       userInput = int(input('Bitte um Bestätigung: '))
                                                       if userInput == 1:
                                                           personnel[userId]['name']= name
                                                           break
                                           elif int(userInput)==2:
                                               while True:
                                                   # Die Adresse wird eingelesen und überprüft
                                                   location = input('Bitte geben sie ihre adresse ein:')
                                                   result = re.search(invalidChar,location)  # Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                                                   if result:
                                                       print('Bitte geben sie eine gültige Adresse ein ')
                                                   elif len(location.strip()) == 0:  # Überprüft die eingabe leer ist
                                                       print('Bitte geben sie eine gültige Adresse ein')
                                                   else:
                                                       print('Ist die eingegebene Adresse Korrekt ?\n1. für Ja\nAlles andere für Nein \n')
                                                       print(f'Prüfung: {location}\n\n')  # Der Benutzer wird nochmal gefaragt, ob die eingabe korrekt ist
                                                       userInput = int(input('Bitte um Bestätigung: '))
                                                       if userInput == 1:
                                                           personnel[userId]['location']=location
                                                           break

                                           elif int(userInput)==3:
                                               while True:
                                                   # Telefon nummer wir eingelesen und überprüft
                                                   contact = input('Bitte geben sie ihre Telefonnummer ein mit Länder Vorwahl (436641234567):')
                                                   result = re.search(invalidChar, contact)
                                                   if result:  # Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                                                       print('Bitte geben sie eine Gültige Telefonnummer ein')
                                                   elif len(contact.strip()) == 0 or len(
                                                           contact) > 15:  # Überprüft ob der Variable (contact) leer ist oder zu viele Ziffern eingegeben wurde
                                                       print('Bitte geben sie eine Gültige Telefonnummer ein')
                                                   else:
                                                       print('Ist die eingegebene Tel.Nummer Korrekt ?\n1. für Ja\nAlles andere für Nein ')
                                                       print(f'Prüfung: +{contact}\n\n')
                                                       userInput = int(input('Bitte um Bestätigung: '))
                                                       if userInput == 1:
                                                           personnel[userId]['contact']= contact
                                                           break
                                           elif userInput==3:
                                               break
                                   else:
                                       break
                           elif int(userInput) == 3:
                               break
                           elif not userInput in personnel:
                              print('\nBitte geben sie eine Gültige ID ein!!\n\n')

                   elif userInput==2:
                       #Mitarbeiter einlesen
                       print('Willkommen zur Registrierung ')

                       while 1:
                           # Die Sozialversicherungsnummer wird eingelesen, überprüft und wird als Hauptschlüsselwort für die Liste eingesetzt
                           id = input('Bitte geben sie ihre Sozial-Versicherungs Nummer(ID/Geb) ein:')
                           result= re.search(invalidSoizalNumb, id)
                           if result:
                               print('\nBitte geben sie eine Gültige Sozial-Versicherungs Nummer')
                           elif id in personnel:
                               print('\nDie Nummer ist schon vergeben')
                           elif len(id) == 10: #überprüft die Länge der Sozialversicherungsnummer
                               print('Ist die Sozial-Versicherungs Nummer Korrekt ?\n1. für Ja\nAlles andere für Nein \n')
                               print(f'Prüfung: {id}\n\n')    #Der Benutzer wird nochmal gefaragt, ob die eingabe korrekt ist
                               userInput = int(input('Bitte um Bestätigung: '))
                               if userInput == 1:
                                   break
                           else:
                               print('Bitte geben sie eine Gültige Sozial-Versicherungs Nummer ein!')

                       while 1:
                           # Das Geburtsdatum wird eingelesen und überprüft
                           birthDate = input('Bitte geben sie ihr Geburtsdatum (TT.MM.JJ) ein:')
                           try:
                               datetime.strptime(birthDate,"%d.%m.%y")  # Überprüft, ob das Format des Geb. datum korrekt ist
                               break

                           except ValueError:
                               print('Bitte geben sie das richtige format ein:(DD.MM.YY)!')

                       while 1:
                           #Der Name wird eingelesen und überprüft
                           name = input('Bitte geben sie ihren Namen ein:')
                           result=re.search(invalidName, name)# Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                           if result:
                               print('Bitte einen gültigen Namen Eingeben(Vorname Nachname)')

                           elif len(name.strip()) == 0:  # Überprüft die eingabe leer ist
                               print('Bitte einen gültigen Namen Eingeben(Vorname Nachname)')

                           else:
                               print('Ist der Name Korrekt ?\n1. für Ja\nAlles andere für Nein \n')
                               print(f'Prüfung: {name}\n\n')   #Der Benutzer wird nochmal gefaragt, ob die eingabe korrekt ist
                               userInput = int(input('Bitte um Bestätigung: '))
                               if userInput == 1:
                                   break

                       while 1:
                           #Die Adresse wird eingelesen und überprüft
                           location = input('Bitte geben sie ihre adresse ein:')
                           result= re.search(invalidChar, location) # Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                           if result:
                               print('Bitte geben sie eine gültige Adresse ein ')
                           elif len(location.strip()) == 0:  # Überprüft die eingabe leer ist
                               print('Bitte geben sie eine gültige Adresse ein')
                           else:
                               print('Ist die eingegebene Adresse Korrekt ?\n1. für Ja\nAlles andere für Nein \n')
                               print(f'Prüfung: {location}\n\n')   #Der Benutzer wird nochmal gefragt, ob die eingabe korrekt ist
                               userInput = int(input('Bitte um Bestätigung: '))
                               if userInput == 1:
                                   break
                       while 1:
                           # Telefon nummer wir eingelesen und überprüft
                           contact = input('Bitte geben sie ihre Telefonnummer ein mit Länder Vorwahl (436641234567):')
                           result = re.search(invalidChar, contact)
                           if result:  # Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                               print('Bitte geben sie eine Gültige Telefonnummer ein')
                           elif len(contact.strip()) == 0 or len(
                                   contact) > 15:  # Überprüft ob der Variable (contact) leer ist oder zu viele Ziffern eingegeben wurde
                               print('Bitte geben sie eine Gültige Telefonnummer ein')
                           else:
                               print('Ist die eingegebene Tel.Nummer Korrekt ?\n1. für Ja\nAlles andere für Nein ')
                               print(f'Prüfung: +{contact}\n\n')
                               userInput = int(input('Bitte um Bestätigung: '))
                               if userInput == 1:
                                   break
                       # Das Schlüsselwort für die "id" wird von der Sozialversicherungsnummer initialisiert
                       personnel[id] = {'name': name, 'birthDate': birthDate, 'location': location,'contact': contact}  # Das Erstellen eines Listen Blocks mit eingegeben daten.

                   elif userInput==3:
                       break
           #Besucher Daten einlesen
           elif userInput==2:
               count += 1  #Besucher Id wird durch einem counter initialisiert
               print('Willkommen Besucher')
               print('Bitte geben sie ihr Daten ein.')

               while True:
                   birthDate = input('Bitte geben sie ihr Geburtsdatum ein (DD.MM.YY):')
                   try:
                       datetime.strptime(birthDate, "%d.%m.%y")   # Überprüft, ob das Format des Geb. datum korrekt ist
                       break
                   except ValueError:
                       print('Bitte geben sie das richtige format ein:(DD.MM.YY)!')
               while True:
                   name = input('Bitte geben sie ihren Namen ein:')
                   result= re.search(invalidName, name)
                   if result:  # Überprüft, ob ein nicht erlaubtes Symbol in diesem string vorhanden ist
                       print('Bitte einen gültigen Namen Eingeben(Vorname Nachname)')
                   elif len(name.strip()) == 0:  # Überprüft ob der Variable (name) leer
                       print('Bitte einen gültigen Namen Eingeben(Vorname Nachname)')
                   else:
                       print('Ist der Name Korrekt ?\n1. für Ja\nAlles andere für Nein \n')
                       print(f'Prüfung: {name}\n\n')
                       userInput = int(input('Bitte um Bestätigung: '))
                       if userInput == 1:
                           break
               #Das schlüsselwort für die "id" wird vom counter initialisiert und dient einfach zu Nummerierung der Besucher
               visitor[count] = {'name': name,'birthDate': birthDate}  # Das Erstellen eines Listen Blocks mit eingegeben daten.

           #Darstellung der Mitarbeiter die in der liste "personnel" gespeichert sind
           elif userInput==3:
               print('Wollen sie nur einen mitarbeiter ausgeben oder alle.\n1.für einen Mitarbeiter\n2.für alle\n\n')
               userInput=int(input('Ihre Eingabe: '))
               if userInput==1:
                   print('\nSie Haben sich für einen Mitarbeiter entschieden.\nBitte Geben sie die ID(SVN) des Mitarbeiter ein.')
                   userInput = input('Ihre Eingabe: ')
                   if userInput in personnel:
                       userId= userInput
                       userInfo = personnel[userInput]
                       print( f'Hier ihre Daten : \n\nID: {userId}\nName: {userInfo['name']}\nGeb.Datum: {userInfo['birthDate']}\nAdresse: {userInfo['location']}\nTel.: +{userInfo['contact']}\n---------------------\n\n')

               elif userInput==2:
                   print('\nHier sind die Mitarbeiter\n\n')
                   for person_id, data in personnel.items():  # Die For-schleife ruft die Schlüsselwörter einzeln mit "personnel.item()" auf.
                       print(f'ID: {person_id}')
                       print(f'Name: {data['name']}')
                       print(f'Geb.datum: {data['birthDate']}')
                       print(f'Adresse: {data['location']}')
                       print(f'Tel.Nummer: +{data['contact']}')
                       print("-------------\n\n")

                       # Darstellung der Besucher die in der liste "visitor" gespeichert sind
           elif userInput==4:

               print('Das sind die Besucher:\n')

               for visitor_id, data in visitor.items():  # Die For-schleife ruft die Schlüsselwörter einzeln mit "visitor.item()" auf.
                   print(f'ID: {visitor_id}')
                   print(f'Name: {data['name']}')
                   print(f'Geb.datum: {data['birthDate']}')
                   print('-------------\n\n')
           else:
              break

if __name__ == "__main__":
    main()