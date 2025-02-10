import mysql.connector
import json
import os
from tkinter import messagebox




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
            except mysql.connector.Error as err:
                print(f'Fehler beim Abrufen der Daten: {err}')
                return None
            finally:
                cursor.close()
                connection.close()

############# Album in die DB übertragen #############

    @classmethod
    def pushToDataBase(cls,newAlbum):

        
        connection = DBManager.connectionToDB()
        cursor = connection.cursor()

        try:
            
            insertQuery = '''
            INSERT INTO albums (id, title, artist)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE title = VALUES(title), artist = VALUES(artist)
            '''
            cursor.execute(insertQuery, (newAlbum['id'], newAlbum['title'], newAlbum['artist']))
            connection.commit()

        except Exception as err:
            print(f'Fehler erkannt: {err}')
            return False

        finally:
            cursor.close()
            connection.close()
            return True
        
############ Alben von DB Löschen ############ 

    @classmethod
    def deletAlbumFromDB(cls,album):
        
        albumID= album['id']


        connection = DBManager.connectionToDB()
        cursor = connection.cursor()

        try:
            
            cursor.execute('DELETE FROM tracks WHERE album_id = %s', (albumID,))     
            cursor.execute('DELETE FROM albums WHERE id = %s', (albumID,))
            connection.commit()
            return True

        except Exception as err:
            print(f'Fehler erkannt: {err}')
            return False

        finally:
            cursor.close()
            connection.close()

########## Track in die DB übertragen #########

    @classmethod
    def addTrackToDB(cls, newTrack):
        connection = cls.connectionToDB()
        cursor = connection.cursor()

        try:
            query = '''
            INSERT INTO tracks (id, title, length, album_id)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            title = VALUES(title), length = VALUES(length), album_id = VALUES(album_id)
            '''
            cursor.execute(query, (newTrack['id'], newTrack['title'], newTrack['length'], newTrack['album_id']))
            connection.commit()
            return True
        
        except Exception as err:
            print(f'Fehler erkannt: {err}')
            return False
        
        finally:
            cursor.close()
            connection.close()


########## Track von DB Löschen ###########
    
    @classmethod
    def deleteTrackFromDB(cls, trackID):
        connection = cls.connectionToDB()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM tracks WHERE id = %s", (trackID,))
            connection.commit()
            return True
        except Exception as err:
            print(f'Fehler erkannt: {err}')
            return False
        finally:
            cursor.close()
            connection.close()