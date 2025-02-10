import csv
import os
from tkinter import messagebox

from AdministrationClass import Administration,Chairperson,Treasurer,Manager
from associationClass import AssociationMember,Member
from DBUtilis import DBManager




class ClubManager:

    currentCsvPos= os.path.dirname(__file__)
    memberlistCSV= os.path.join(currentCsvPos, 'Mitglieder-Liste.csv')  


    allMemberlist=[]

############## Daten werden von DB geladen ###########
    def getDataFromDB(self):
        
        query='SELECT * FROM Member'
        records=DBManager.fetchData(query)
        memberIDs= [member[0] for member in self.allMemberlist]
        if records:
            for row in records:
                if row[0] in memberIDs:
                    pass
                else:
                    self.allMemberlist.append(row)
            messagebox.showinfo('Erfolg,Daten wurden Geladen')
        else:
            messagebox.showerror('Fehler','Keine Daten gefunden') 
    
############## CSV Funktionen ###########
    
    def memberToCsvExport(self):
        
        if not ClubManager.allMemberlist:
            messagebox.showerror('Fehler','Die Mitgliederliste ist leer. Kein Export möglich.')
            return
        
        
        try:
            # CSV-Datei schreiben
            with open(self.memberlistCSV, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                headers = ['memberID', 'name', 'adress', 'email', 'entryDate', 'administrationBody', 'responsibilities', 'financeArea', 'group']
                writer.writerow(headers)
                writer.writerows(self.allMemberlist)
                messagebox.showinfo('Erfolg','CSV-Datei erfolgreich exportiert!')
                return True
        except Exception as e:
                    messagebox.showerror('Fehler', f'Fehler beim Exportieren: {e}')
                    return None

    @classmethod
    def fromCsvToDB(cls):
         
        try:
            
            with open(cls.memberlistCSV, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                newEntries = []
                for row in reader:
                    # Überprüfen, ob der Eintrag bereits existiert
                    existingMember = next((m for m in cls.allMemberlist if str(m[0]) == row['memberID']), None)
                    
                    if not existingMember:
                        newEntries.append(row)


            for entry in newEntries:
                newData=ClubManager.memberToObjektFactory(entry)
                DBManager.insertData(newData)
            if newEntries:
                messagebox.showinfo('Erfolg', f'{len(newEntries)} neue Mitglieder erfolgreich hinzugefügt.')
            else:
                messagebox.showinfo('Hinweis', 'Keine neuen Einträge gefunden.')

        except Exception as e:
            print(f'Fehler beim Importieren der CSV: {e}')
            messagebox.showerror('Fehler', 'Beim Einlesen der CSV-Datei ist ein Fehler aufgetreten.')              

############## Obejekt Factory  ########## 
    @staticmethod
    def memberToObjektFactory(record):
                
            baseAttributes = {
                'memberID': record['memberID'],
                'name': record['name'],
                'adress': record['adress'],
                'email': record['email'],
                'entryDate': record['entryDate']
            }

        # Erstelle das spezifische Objekt basierend auf dem `administrationBody`
            administration_body = record.get('administrationBody')
            if administration_body == 'Chairperson':
                return Chairperson(**baseAttributes, administrationBody=administration_body ,responsibilities=record.get('responsibilities'))
            elif administration_body == 'Treasurer':
                return Treasurer(**baseAttributes, administrationBody=administration_body ,financeArea=record.get('financeArea'))
            elif administration_body == 'Manager':
                return Manager(**baseAttributes, administrationBody=administration_body ,group=record.get('group'))
            else:
                return Member(**baseAttributes, group=record.get('group', None))
                
                  
        

        