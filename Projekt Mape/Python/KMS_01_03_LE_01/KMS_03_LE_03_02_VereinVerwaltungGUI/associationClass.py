import os
import json
import datetime

class AssociationMember:

    def __init__(self,memberID,name,adress,email,entryDate):
        self.memberID = memberID
        self.name = name
        self.adress=adress
        self.email = email
        self.entryDate = entryDate


    def __str__(self):
            return (f'\n  Mitglieds ID: {self.memberID}\n  Name: {self.name}\n  Adresse: {self.adress}\n  Email: {self.email}\n  Eintrittsdatum: {self.entryDate}')

class Member(AssociationMember):
    def __init__(self, memberID, name,adress, email, entryDate,group):
        super().__init__(memberID, name,adress, email, entryDate)
        self.group = group
    
    @classmethod
    def getMapping(cls):
         
        memberFields = {
            'Mitglieds-ID': 'memberID',
            'Name': 'name',
            'Adresse': 'adress',
            'E-Mail': 'email',
            'Eintrittsdatum (TT.MM.JJJJ)': 'entryDate',
            'Gruppe (z.B.: A,B,....)': 'group',
        }
        return memberFields

    def __str__(self):
        return (f'\nEinfaches Mitglied{super().__str__()}\n  {self.group}')

