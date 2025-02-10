import mysql.connector
import json
import os
import csv
from tkinter import messagebox




class DBManager:

    currentLogData= os.path.dirname(__file__)
    logConfigData= os.path.join(currentLogData, 'configDataDB.json')
    currentCsvPos= os.path.dirname(__file__)
    memberlistCSV= os.path.join(currentCsvPos, 'Mitglieder-Liste.csv') 

    # Verbindung zu MySQL DB
    @classmethod
    def connectionToDB(cls):

        try:
            with open(cls.logConfigData, 'r') as config_file:
                config = json.load(config_file)

            for key, value in config.items():
                if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
                    sliceValue = value[2:-1]
                    config[key] = os.getenv(sliceValue, value)

            connectionToDB = mysql.connector.connect(
                host=config['host'],
                user=config['user'],
                password=config['password'],
                database=config['database'],
                port=config['port']
            )

            if connectionToDB.is_connected():
                print('Verbindung steht')
                return connectionToDB
            
        except mysql.connector.error as err:
            print(f'Fehler: {err}')
            return None
        
    @classmethod   
    def fetchData(cls,query):

        connection=cls.connectionToDB()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                results = cursor.fetchall()
                return results
            except mysql.connector.Error as err:
                print(f'Fehler beim Abrufen der Daten: {err}')
                return None
            finally:
                cursor.close()
                connection.close()

############# Daten in die DB Übertragen ################

    @classmethod
    def insertData(cls, record):

        try:
            if not isinstance(record, dict):
                record = record.__dict__

            connection=cls.connectionToDB()
            cursor = connection.cursor()
            if 'group' in record:
                record['group'] = record['group'].upper()

            allColumns = ['memberID', 'name', 'adress', 'email', 'entryDate', 'administrationBody', 'responsibilities', 'financeArea', 'group']
            completeRecord={col: (int(record[col]) if col == 'memberID' and record.get(col) else record.get(col)) for col in allColumns}
           

            columns = ', '.join(completeRecord.keys())
            placeholders = ', '.join(['%s'] * len(completeRecord))
            query= f'INSERT INTO Member ({columns}) VALUES ({placeholders})'.replace('group', '`group`')
            data=tuple(completeRecord.values())
            print(f"Query: {query}")
            print(f"Daten: {data}")
            cursor.execute(query,data)
            connection.commit()

        except Exception as err:
            print(f'DB Insert Error: {err}')
            messagebox.showerror('Fehler','Verbindung zur DB Fehlgeschlagen') 

    @classmethod
    def updateDataToDB(cls, updateData):
        
        try:
            # Verbindung zur DB herstellen
            connection = cls.connectionToDB()
            cursor = connection.cursor()

            # Nur die Felder, die geändert werden können
            updatableColumns = ['name', 'adress', 'group']
            updateValues = {col: updateData.get(col) for col in updatableColumns if col in updateData}
            
            # Dynamische Erstellung der SET-Klausel
            setClause = ', '.join([f'`{col}` = %s' for col in updateValues.keys()])
            query = f'UPDATE Member SET {setClause} WHERE memberID = %s'
            
            # Query-Werte vorbereiten
            data = list(updateValues.values()) + [updateData['memberID']]

            # SQL-Abfrage ausführen
            cursor.execute(query, data)
            connection.commit()

            messagebox.showinfo('Erfolg', 'Daten wurden erfolgreich aktualisiert.')
        except Exception as err:
            print(f'DB Update Error: {err}')
            messagebox.showerror('Fehler', 'Verbindung zur DB fehlgeschlagen.')
        finally:
            if connection:
                connection.close()