import re
from datetime import datetime 

from UnionManager import ClubManager




class Validator():
   
    ############# Valedierung für Eingabefelder (Mitglieder Hinzufügen) ################

    # ID Validierung
    @staticmethod
    def validID(record):
        memberIDs= [member[0] for member in ClubManager.allMemberlist]
        if not str(record['memberID']).isdigit() or record['memberID'] in str(memberIDs):
                return False
        else:
            return True
        
    # E-Mail Validierung        
    @staticmethod
    def validEmail(record):
        
        # Einfacher Ausdruck für die E-Mail Validierung
        emailPattern = (
            r'^[a-zA-Z0-9](?!.*--)(?!.*\.\.)[a-zA-Z0-9._%+-]*[a-zA-Z0-9]'  # Lokaler Teil
            r'@[a-zA-Z0-9](?!.*--)[a-zA-Z0-9.-]*[a-zA-Z0-9]\.[a-zA-Z]{2,}$'  # Domäne
        )
        
        # Match mit regulärem Ausdruck
        if re.match(emailPattern, record['email']):
            return True  
        else:
            return False 
        
    # Datum Validierung
    @staticmethod
    def validEntryDate(record):

        try:
            # Datumsformat direkt mit `strptime` überprüfen
            parsedDate = datetime.strptime(record['entryDate'], "%d.%m.%Y")
            return True  # Wenn kein Fehler, ist das Datum gültig
        except ValueError:
            return False
         
    # Gruppen Validierung      
    @staticmethod
    def validGroup(record):
    
        if len(record['group']) == 1 and record['group'].isalpha():
            return True
        else:
            return False

    


            