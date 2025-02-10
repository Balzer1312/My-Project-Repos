import mysql.connector
import json
import os
from tkinter import messagebox




class DBManager:
    
    currentLogData= os.path.dirname(__file__)
    logConfigData= os.path.join(currentLogData, 'configDataDB.json')

    # Verbindung zu MySQL DB
    @classmethod
    def connectionToDB(cls):


        try:
            with open(cls.logConfigData, 'r') as configFile:
                config = json.load(configFile)

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
            except :
                return None
            finally:
                cursor.close()
                connection.close()
########## Account  Anlegen ##########
    @classmethod
    def insertDB(cls,record):

        connection = cls.connectionToDB()

        try:
            cursor=connection.cursor()
            insertQuery = 'INSERT INTO bankaccount (userid, iban, name, balance)VALUES (%s, %s, %s, %s)'
            cursor.execute(insertQuery, (record['userid'], record['iban'], record['name'], record['balance']))
            connection.commit()
            return True
        except:
            return False

        finally:
            connection.close()
######### Account aus der DB Löschen ###########
    @classmethod
    def deletWereUser(cls,id):

        connection = cls.connectionToDB()


        try:
            cursor = connection.cursor()
            deleteQuery = 'DELETE FROM bankaccount WHERE userid = %s'
            cursor.execute(deleteQuery, (id,))
            connection.commit()
            return True
        except:
            return None
    
        finally:
            connection.close()

########## Account Kontostan ändern ##############
    @classmethod
    def withdrawAccount(cls,id,amount):
        connection = cls.connectionToDB()


        try:
            cursor = connection.cursor()

            # Überprüfen, ob das Konto existiert
            check_query = 'SELECT balance FROM bankaccount WHERE userid = %s'
            cursor.execute(check_query, (id,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror('Fehler','Die ID existiert nicht!')
                return

            currentBalance = result[0]

            # Überprüfen, ob genügend Guthaben vorhanden ist
            if currentBalance < amount:
                messagebox.showerror('Fehler','Dein Konto hat zu wenig Deckung!')
                return 

            # Guthaben aktualisieren
            update_query = 'UPDATE bankaccount SET balance = balance - %s WHERE userid = %s'
            cursor.execute(update_query, (amount, id))
            connection.commit()

            return f'Auszahlung erfolgreich! Neuer Kontostand: {currentBalance - amount}'

        except mysql.connector.Error as err:
            return f'Fehler beim Aktualisieren des Kontos: {err}'

        finally:
            connection.close()

    @classmethod
    def depositAccount(cls,id,amount):
        connection = cls.connectionToDB()

        try:
            cursor = connection.cursor()

            # Überprüfen, ob das Konto existiert
            check_query = 'SELECT balance FROM bankaccount WHERE userid = %s'
            cursor.execute(check_query, (id,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror('Fehler','Die ID existiert nicht!')
                return 

            currentBalance = result[0]

            # Guthaben aktualisieren
            update_query = 'UPDATE bankaccount SET balance = balance + %s WHERE userid = %s'
            cursor.execute(update_query, (amount, id))
            connection.commit()

            return f'Einzahlung erfolgreich! Neuer Kontostand: {currentBalance + amount}'

        except mysql.connector.Error as err:
            return f'Fehler beim Aktualisieren des Kontos: {err}'

        finally:
            connection.close()



