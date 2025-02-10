import os 
import json


class JsonHandler:
    currenJsonVehiclePos= os.path.dirname(__file__)
    vehicleJsonlist= os.path.join(currenJsonVehiclePos, 'vehicleDB.json')

    allVehicleList={'Motorrested':[],'NoneMotorrested':[]}

    @classmethod
    def updateJson(cls, newRecord, vehicleType):
        try:
            with open(cls.vehicleJsonlist, 'r', encoding='utf-8') as file:
                records = json.load(file)
        except FileNotFoundError:
            records = {'Vehicle': {'Motorrested': [], 'NoneMotorrested': []}}

        # Fahrzeug hinzufügen, wenn es noch nicht existiert
        if newRecord not in records['Vehicle'][vehicleType]:
            records['Vehicle'][vehicleType].append(newRecord)

        # JSON-Datei aktualisieren
        with open(cls.vehicleJsonlist, 'w', encoding='utf-8') as file:
            json.dump(records, file, indent=4)


    @classmethod
    def loadJson(cls):
        try:
            with open(cls.vehicleJsonlist, 'r', encoding='utf-8') as file:
                records = json.load(file)

            # Liste zurücksetzen, um doppelte Einträge zu vermeiden
            cls.allVehicleList = {'Motorrested': [], 'NoneMotorrested': []}

            for record in records['Vehicle']['Motorrested']:
                cls.allVehicleList['Motorrested'].append(record)

            for record in records['Vehicle']['NoneMotorrested']:
                cls.allVehicleList['NoneMotorrested'].append(record)

        except FileNotFoundError:
            raise FileNotFoundError(f"Die Datei \"{cls.vehicleJsonlist}\" wurde nicht gefunden.")