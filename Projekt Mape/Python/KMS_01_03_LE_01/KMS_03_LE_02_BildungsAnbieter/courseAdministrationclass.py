import json
import os
import csv
from MemberClass import People,Client,Tutor


class Course:
    courses=[]
    def __init__(self, courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName
    

class providerManagement:
    persCurrentJsonFile= os.path.dirname(__file__)
    persJsonFile= os.path.join(persCurrentJsonFile, 'PersonRegistry.json')
    persCurrentCsvFile= os.path.dirname(__file__)
    persCsvFile=os.path.join(persCurrentCsvFile,'PersonenDaten.csv')
    
    CurrentFilteredDataFile=os.path.dirname(__file__)
    filteredCsvFile = os.path.join(persCurrentJsonFile,'GefilterteDaten.csv' )

    courseCurrentJsonFile= os.path.dirname(__file__)
    courseJsonFile= os.path.join(courseCurrentJsonFile, 'coursData.json')
    courseCurrentCsvFile= os.path.dirname(__file__)
    coursecsvFile=os.path.join(courseCurrentCsvFile,'Kursinfo.csv')


    @staticmethod
    def addCourse(courseData):
        if any(course['courseID'] == courseData['courseID'] for course in Course.courses):
            print(f'Kurs mit der ID {courseData['courseID']} existiert bereits!')
            return
         
        Course.courses.append(courseData)
        providerManagement.saveJson(Course.courses,providerManagement.courseJsonFile)
        print(f'Kurs wurde hinzugefügt')
        


    @staticmethod
    def addPerson(record):
        if any(p['id'] == record['id'] for p in People.personDataList['people']):
            print(f'Person mit der ID {record['id']} existiert bereits!')
            return
        
        
        People.personDataList['people'].append(record)
        providerManagement.saveJson(People.personDataList ,providerManagement.persJsonFile)
        print('Person wurde hinzugefügt')

    @staticmethod
    def removeFromJson(itemID, dataList, jsonfile, KeyWord):
        removeItem = next((item for item in dataList if item[KeyWord] == itemID), None)

        if not removeItem:
            print(f'Element mit der ID {itemID} nicht gefunden.')
            return

        dataList.remove(removeItem)
        providerManagement.saveJson(dataList, jsonfile)
        print(f'Element mit der ID {itemID} wurde entfernt.')
    
    @staticmethod
    def showAllPerson():
        if not People.personDataList['people']:
            print('Keine Daten Gefunden')
            return
        
        for people in People.personDataList['people']:
                record= People.createPersonAsObj(people)
                print(record)

    @staticmethod
    def showFilteredPeople(filterData):
        if not People.personDataList['people']:
            print('Keine Daten Gefunden')
            return
        
        for people in People.personDataList['people']:
            record=People.createPersonAsObj(people)

            if filterData == type(record).__name__:
                print(record)

    def showOnePerson(searchID):
        if not People.personDataList['people']:
            print('Keine Daten Gefunden')
            return
        
        for people in People.personDataList['people']:
            record=People.createPersonAsObj(people)

            if searchID == record.id:
                print(record)
                return 

    @staticmethod
    def saveJson(data, JsonFile):
        with open(JsonFile,'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def persoLoadJson(persJsonFile=persJsonFile):

        try:
            with open(persJsonFile,'r') as file:
                People.personDataList=json.load(file)

        except FileNotFoundError:
            People.personDataList= {'people':[]}


    @staticmethod
    def courseLoadJson(courseJsonFile=courseJsonFile):
            
        try:
            with open(courseJsonFile, 'r') as file:
                Course.courses = json.load(file)
                
    
        except FileNotFoundError:
            Course.courses=[]

            
    @staticmethod            
    def persoSaveToCsv():
         
        existFile=os.path.exists(providerManagement.persCsvFile)
        existingIDs = []

        if not existFile:
                with open(providerManagement.persCsvFile,mode='w', newline='', encoding='utf-8')as file:
                    writer = csv.writer(file)
                    writer.writerow(['type', 'id', 'name', 'adress', 'birthdate', 'chosenCourse', 'specialty'])
        else:
            with open(providerManagement.persCsvFile,mode='r')as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row)>1:
                        existingIDs.append(row[1])

        with open(providerManagement.persCsvFile,mode='a',newline='',encoding='utf-8')as file:
                writer = csv.writer(file)
                for record in People.personDataList['people']:
                    if str(record['id']) in existingIDs:
                        continue

                    if record['type']== 'Client':
                        writer.writerow([
                            record['type'],
                            record['id'],
                            record['name'],
                            record['adress'],
                            record['birthdate'],
                            record['chosenCourse']
                        ])
                    elif record['type']=='Tutor':
                            writer.writerow([
                            record['type'],
                            record['id'],
                            record['name'],
                            record['adress'],
                            record['birthdate'],
                            record['specialty']
                        ])

    @staticmethod
    def saveFilteredToCsv(filterValue):
        csvFilePath = providerManagement.filteredCsvFile
        

        existFile=os.path.exists(csvFilePath)
        filteredData = [
            People.createPersonAsObj(record)
            for record in People.personDataList['people']    
                if record.get('type') == filterValue
        ]

        if not filteredData:
            print('Keine Daten gefunden, die dem Filter entsprechen.')
            return
        if not existFile:
            with open(csvFilePath,mode='w')as file:
                        writer = csv.writer(file)

        headers = ['type', 'id', 'name', 'adress', 'birthdate']
        if isinstance(filteredData[0], Client):
            headers.append('chosenCourse')
        elif isinstance(filteredData[0], Tutor):
            headers.append('specialty')
        
        with open(csvFilePath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)


            for record in filteredData:
                if isinstance(record, Client):
                    writer.writerow([
                        'Client',
                        record.id,
                        record.name,
                        record.adress,
                        record.birthdate,
                        record.chosenCourse,  
                    ])
                elif isinstance(record, Tutor):
                    writer.writerow([
                        'Tutor',
                        record.id,
                        record.name,
                        record.adress,
                        record.birthdate,
                        record.specialty
                    ])

        print(f'Gefilterte Daten wurden in {providerManagement.filteredCsvFile} gespeichert.')

    @staticmethod
    def readFilteredCsvData():
        csvFilePath = providerManagement.filteredCsvFile
        

        if not os.path.exists(csvFilePath):
            print(f' Die Datei \'{csvFilePath}\' wurde nicht gefunden.')
            return
        
        try:
            providerManagement.persoLoadJson()
            existingIDs = {person['id'] for person in People.personDataList['people']}

            with open(csvFilePath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['id'] = int(row['id'])
            
                    if row['id'] not in existingIDs:
                        if row['type'] == 'Client':
                            row['chosenCourse'] = eval(row['chosenCourse'])  # String in Liste konvertieren
                        People.personDataList['people'].append(row)
                        existingIDs.add(row['id'])

            providerManagement.saveJson(People.personDataList,providerManagement.persJsonFile)
            print('Gefilterte Daten erfolgreich hinzugefügt und gespeichert.')
            
        except Exception as e:
            print(f'Fehler beim Einlesen der CSV-Datei: {e}')

        

        


