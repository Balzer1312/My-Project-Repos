from tkinter import messagebox
import mysql.connector
import json
import os



class DBManager:

    currentLogData= os.path.dirname(__file__)
    logConfigData= os.path.join(currentLogData, 'configDataDB.json')

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
            
        except mysql.connector.Error as err:
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
            except  mysql.connector.Error as err:
                print(f'Fehler beim Abrufen der Daten: {err}')
                return None
            
            finally:
                cursor.close()
                connection.close()

############### Neues Fahrzeug in die DB übertragen ############

    @classmethod
    def insertVehicle(cls,record):
            

         # SQL Query vorbereiten
        insert_query = (
            'INSERT INTO vehicles (serialID, brand, model, rentalPrice) '
            'VALUES (%s, %s, %s, %s)'
        )
        values = (
            record['serialID'],
            record['brand'],
            record['model'],
            record['rentalPrice']
        )

        # Verbindung zur Datenbank herstellen
        connection = cls.connectionToDB()
        
        try:
            cursor = connection.cursor()
            cursor.execute(insert_query, values)
            connection.commit()  # Aenderungen bestaetigen
            messagebox.showinfo('Erfolg', 'Daten wurden erfolgreich in die Datenbank eingefügt!')
            return True
        except Exception as err:
            print(f'Fehler erkannt: {err}')
            return False
        finally:
            cursor.close()
            connection.close()
                

###############  Neuen Kunden in die DB übertragen ############

    @classmethod
    def insertCustomer(cls, record):

        
        insertQuery = '''
        INSERT INTO customers (customerID, name, address, email, phoneNumber)
        VALUES (%s, %s, %s, %s, %s)
        '''
        values = (
            record['customerID'],
            record['name'],
            record['address'],
            record['email'],
            record['phoneNumber']
        )

        # Verbindung zur Datenbank herstellen
        connection = cls.connectionToDB()
        try:
            cursor = connection.cursor()
            cursor.execute(insertQuery, values)
            connection.commit()
            messagebox.showinfo('Erfolg', 'Daten wurden erfolgreich in die Datenbank eingefügt!')  
            return True
        except Exception:
            messagebox.showerror('Fehler','Verbindung zur DB Fehlgeschlagen') 
            return False
        
        finally:
            cursor.close()
            connection.close()
    
            
            
            
############### Neuen Vermietung eintrag in die DB übertragen ############

    @classmethod
    def insertRental(cls, record):

        
        insert_query = (
        'INSERT INTO rentals (rentalID, customerID, serialID, rentalDate, returnDate) '
        'VALUES (%s, %s, %s, %s, %s)'
        )
        values = (
            record['rentalID'],
            record['customerID'],
            record['serialID'],
            record['rentalDate'],
            record['returnDate']  # Kann None sein
        )

        # Verbindung zur Datenbank herstellen
        connection = cls.connectionToDB()
        
        try:
            cursor = connection.cursor()
            cursor.execute(insert_query, values)
            connection.commit()  # Änderungen bestätigen
            messagebox.showinfo('Erfolg', 'Daten wurden erfolgreich in die Datenbank eingefügt!')
            return True
        except Exception as err:
            print(f'Fehler erkannt: {err}')
            messagebox.showerror('Fehler','Verbindung zur DB Fehlgeschlagen') 
            return False
        
        finally:
            cursor.close()
            connection.close()


################# Fahrzeug wurde Zurück gebracht #################

    @classmethod
    def updateRental(cls, record):
        
        # SQL Query vorbereiten
        update_query = (
            'UPDATE rentals '
            'SET returnDate = %s '
            'WHERE rentalID = %s'
        )
        values = (record['returnDate'], record['rentalID'])
        connection = cls.connectionToDB()
        
        try:
            cursor = connection.cursor()
            cursor.execute(update_query, values)
            connection.commit()  # Änderungen bestätigen
            messagebox.showinfo('Erfolg', 'Daten wurden erfolgreich in der Datenbank Aktualisiert !')
            return True
        except Exception as err:
            print(f'Fehler erkannt: {err}')
            messagebox.showerror('Fehler','Verbindung zur DB Fehlgeschlagen') 
            return False
        
        finally:
            cursor.close()
            connection.close()
    

############# Fahrzeug aus DB enfernen #########

    @classmethod
    def deleteVehicleFromDB(cls, vehicleID):
        connection = cls.connectionToDB()
        cursor = connection.cursor()
        try:
            cursor.execute('DELETE FROM vehicles WHERE serialID = %s', (vehicleID,))
            connection.commit()
            return True
        except Exception as err:
            print(f'Fehler erkannt: {err}')
            return False
        finally:
            cursor.close()
            connection.close()
