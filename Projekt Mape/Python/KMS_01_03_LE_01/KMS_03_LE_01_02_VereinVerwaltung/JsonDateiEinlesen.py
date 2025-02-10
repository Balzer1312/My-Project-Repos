import json
import os
from KMS_1_03_LE_01_02_VereinVerwaltung_Balzer import Chairperson, Player, Treasurer, SportTeamManagerr, Coach,AssociationMember

CurrentFile= os.path.dirname(__file__)
filePath = os.path.join(CurrentFile,'VereinsObjekte.json')

def readJsonFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        return json.load(file)


def createInstancesFromJson(jsonData):
    for item in jsonData:
        class_name = item["class"]
        attributes = item["attributes"]

        if class_name == "Chairperson":
            Chairperson(
                memberID=attributes["memberID"],
                name=attributes["name"],
                email=attributes["email"],
                entryDate=attributes["entryDate"],
                administrationBody=attributes["administrationBody"],
                currentProject=attributes["currentProject"]
            )
        elif class_name == "Player":
            Player(
                memberID=attributes["memberID"],
                name=attributes["name"],
                email=attributes["email"],
                entryDate=attributes["entryDate"],
                teamName=attributes["teamName"],
                playPosition=attributes["playPosition"],
                playerNumber=attributes["playerNumber"]
            )
        elif class_name == "Treasurer":
            Treasurer(
                memberID=attributes["memberID"],
                name=attributes["name"],
                email=attributes["email"],
                entryDate=attributes["entryDate"],
                administrationBody=attributes["administrationBody"],
                financeArea=attributes["financeArea"]
            )
        elif class_name == "SportTeamManagerr":
            SportTeamManagerr(
                memberID=attributes["memberID"],
                name=attributes["name"],
                email=attributes["email"],
                entryDate=attributes["entryDate"],
                administrationBody=attributes["administrationBody"],
                event=attributes["event"]
            )
        elif class_name == "Coach":
            Coach(
                memberID=attributes["memberID"],
                name=attributes["name"],
                email=attributes["email"],
                entryDate=attributes["entryDate"],
                teamName=attributes["teamName"],
                experience=attributes["experience"],
                mantra=attributes["mantra"],
                traninigsDate=attributes["trainingsDate"]
            )



