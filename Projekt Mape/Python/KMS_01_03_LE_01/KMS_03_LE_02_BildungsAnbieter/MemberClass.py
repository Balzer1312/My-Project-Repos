import json
import os
import datetime



class People:

    personDataList={'people':[]}

    def __init__(self,id,name,adress,birthdate):
        self.id = id
        self.name = name
        self.adress = adress
        self.birthdate= birthdate

    def createPersonAsObj(personRecord):

        personType = personRecord['type']
        if personType == 'Client':
            return Client(
                personRecord['id'],
                personRecord['name'],
                personRecord['adress'],
                personRecord['birthdate'],
                personRecord['chosenCourse']
            )
        elif personType == 'Tutor':
            return Tutor(
                personRecord['id'],
                personRecord['name'],
                personRecord['adress'],
                personRecord['birthdate'],
                personRecord['specialty']
            )
    

    def __str__(self):
            return (f'\n\nPersonen daten:\n ID: {self.id}\n Name: {self.name}\n Adresse: {self.adress}\n Geb.: {self.birthdate}\n')
        
class Client(People):
    def __init__(self, id, name, adress, birthdate,chosenCourse):
        super().__init__(id, name, adress, birthdate)
        self.chosenCourse = chosenCourse
    
    def __str__(self):
        return (super().__str__() + f' Kurse: {self.chosenCourse}\n'+'#'*40)

class Tutor(People):
    def __init__(self, id, name, adress, birthdate, specialty):
        super().__init__(id, name, adress, birthdate,)
        self.specialty = specialty
    
    def __str__(self):
        return (super().__str__() + f' Lehrer für: {self.specialty}\n'+'#'*40)