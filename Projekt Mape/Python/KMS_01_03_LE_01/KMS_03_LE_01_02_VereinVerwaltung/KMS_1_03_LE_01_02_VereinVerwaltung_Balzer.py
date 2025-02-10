
#Die Erstellten Fuktionen sind nur als Beispiele gedacht und haben nur den zweck etwas Auszugeben
import os
import datetime

class AssociationMember:
    allMemberContainer=[]

    def __init__(self,memberID,name,email,entryDate):
        self.memberID = memberID
        self.name = name
        self.email = email
        self.entryDate = entryDate
        AssociationMember.allMemberContainer.append(self)

    def showMember(self):
        print(f"\nName:{self.name}, MitgliedID: {self.memberID}, E-Mail: {self.email}, Eintritts Datum: {self.entryDate}")

    @classmethod
    def showAllMembers(cls):  
        for member in(cls).allMemberContainer:    # Das cls ist die Referenz auf meine Klasse(AssociationMember), mit der ich auf die Liste allMemberContainer zugreifen kann. Diese Liste enthält alle Instanzen(objekte), und ich kann mit diesen Instanzen arbeiten.
            print(f"\n\nMitglied: {member.__class__.__name__}")
            print(f"  ID: {member.memberID}")
            print(f"  Name: {member.name}")
            print(f"  E-Mail: {member.email}")
            print(f"  Eintrittstag: {member.entryDate}")
        
            if isinstance(member, Chairperson):
                print(f"  Verwaltungs Organ: {member.administrationBody}")
                print(f"  Aktives Projekt: {member.currentProject}")
                print("x" * 40 +'\n\n') 

            elif isinstance(member, Treasurer):
                print(f"  Verwaltungs Organ: {member.administrationBody}")
                print(f"  Finanzbereich: {member.financeArea}")
                print("x" * 40 +'\n\n') 

            elif isinstance(member, SportTeamManagerr):
                print(f"  Verwaltungs Organ: {member.administrationBody}")
                print("x" * 40 +'\n\n') 

            elif isinstance(member, Coach):
                print(f"  Team: {member.teamName}")
                print(f"  Erfahrung: {member.experience}")
                print(f"  Mantra: {member.mantra}")
                print("x" * 40 +'\n\n') 
                
            elif isinstance(member, Player):
                print(f"  Team: {member.teamName}")
                print(f"  Position: {member.playPosition}")
                print(f"  Spieler Nummer: {member.playerNumber}")
                print("x" * 40 +'\n\n') 

class Administration(AssociationMember):
    def __init__(self,memberID,name,email,entryDate,administrationBody):
        super().__init__(memberID,name, email,entryDate)
        self.administrationBody = administrationBody

class SportsClup(AssociationMember):
    def __init__(self, memberID, name, email, entryDate,teamName):
        super().__init__(memberID, name, email, entryDate)
        self.teamName= teamName

class Chairperson(Administration):
    def __init__(self, memberID, name, email, entryDate, administrationBody,currentProject):
        super().__init__(memberID, name, email, entryDate, administrationBody)
        self.currentProject = currentProject 

    def setMeeting(self):
        print(f"\nEs wurde ein Metting geplant für das Projekt, {self.currentProject}\n")

class Treasurer(Administration):
    def __init__(self, memberID, name, email, entryDate, administrationBody,financeArea):
        super().__init__(memberID, name, email, entryDate, administrationBody)
        self.financeArea = financeArea

    def generateReport(self):
        print(f"\nDer Finanz Bericht wurde für den Bereich {self.financeArea} bereitgestellt.\n")

class SportTeamManagerr(Administration):
    def __init__(self, memberID, name, email, entryDate, administrationBody, event):
        super().__init__(memberID, name, email, entryDate, administrationBody)
        self.event = event 

    def setSportEvent(self):
        print(f"\nEs wurde das {self.event} Event geplant.\n")
 
class Coach(SportsClup):
    def __init__(self, memberID, name, email, entryDate, teamName,experience,mantra,traninigsDate):
        super().__init__(memberID, name, email, entryDate, teamName)
        self.experience = experience
        self.mantra = mantra
        self.trainingsDate = traninigsDate

    def setTrainingPlan(self):
        print(f"\nDer Trainier {self.name} hat am {self.traninigsDate} ein Trainig gepalant und das mit dem Mantra:\"{self.mantra}\".\n ")

class Player(SportsClup):
    def __init__(self, memberID, name, email, entryDate, teamName,playPosition,playerNumber):
        super().__init__(memberID, name, email, entryDate, teamName)
        self.playPosition = playPosition
        self.playerNumber= playerNumber

    def SetInjured(self):
        print(f"\nDer Spieler {self.name}  mit der Nummer {self.playerNumber} hat sich Leider Verletzt.\n")



