import json
import os
from tkinter import messagebox
from MotorrestedClass import Motorrested,Truck,Car,Motorcycle
from NoneMotorrestedClass import NoneMotorrested,Bicycle
from JsonHandler import JsonHandler



class VehicleManager:

    @staticmethod
    def createVehicle(record):
        vehicleType = record['type']
        
        baseAttribute = {
        "color": record['color'],
        "model": record['model'],
        "brand": record['brand']
    }
        if vehicleType=='Car':
            return Car(**baseAttribute, mark=record['mark'], fuel=record['fuel'],
                   consumption=record['consumption'], mileage=record['mileage'], doors=record['doors'])
        
        elif vehicleType=='Motorcycle':
            return Motorcycle(**baseAttribute, mark=record['mark'], fuel=record['fuel'],
                    consumption=record['consumption'], mileage=record['mileage'], gears=record['gears'])
        
        elif vehicleType == 'Truck':
            return Truck(**baseAttribute, mark=record['mark'], fuel=record['fuel'],
                    consumption=record['consumption'], mileage=record['mileage'], loadingWeight=record['loadingWeight'])
        
        elif vehicleType == 'Bicycle':
            return Bicycle(**baseAttribute, id=record['id'], gears=record['gears']) 

        else:
            raise ValueError(f'Unbekannter Fahrzeugtyp: {vehicleType}')

    @staticmethod
    def addVehicle(record):
        newVehicle= VehicleManager.createVehicle(record)
    
        if isinstance(newVehicle, Motorrested):
            existingMarks = [vehicle['mark'] for vehicle in JsonHandler.allVehicleList['Motorrested']]
            if record['mark'] in existingMarks:
                messagebox.showerror('Fehler', f"Das Kennzeichen '{record['mark']}' existiert bereits.")
                return False
            
            return newVehicle
        
        elif isinstance(newVehicle,NoneMotorrested):
            existingIds = [vehicle['id'] for vehicle in JsonHandler.allVehicleList['NoneMotorrested']]
            if record['id'] in existingIds:
                messagebox.showerror('Fehler', f"Die ID '{record['id']}' existiert bereits.")
                return False
            
            return newVehicle
        
        else:
            raise  ValueError(f"Unbekannter Fahrzeugtyp")

    @classmethod
    def showAllVehicles(cls):
        
        vehicles = []
        vehicles.extend(JsonHandler.allVehicleList['Motorrested'])
        vehicles.extend(JsonHandler.allVehicleList['NoneMotorrested'])
        return [cls.createVehicle(record) for record in vehicles]
    
    @classmethod
    def showMotorrested(cls):
        return [cls.createVehicle(record) for record in JsonHandler.allVehicleList['Motorrested']]
    
    @classmethod
    def showAllCars(cls):
        return [cls.createVehicle(record)for record in JsonHandler.allVehicleList['Motorrested']if record['type'] == 'Car']
    
    @classmethod
    def showAllMotorcycle(cls):
        return [cls.createVehicle(record)for record in JsonHandler.allVehicleList['Motorrested']if record['type'] == 'Motorcycle' ]
    
    @classmethod
    def showAllTruck(cls):
        return [cls.createVehicle(record)for record in JsonHandler.allVehicleList['Motorrested']if record['type'] == 'Truck'] 
    
    @classmethod
    def showNoneMotorrested(cls):
        return [cls.createVehicle(record) for record in JsonHandler.allVehicleList['NoneMotorrested']]
    
    @classmethod
    def showAllBicycle(cls):
        return [ cls.createVehicle(record)for record in JsonHandler.allVehicleList['NoneMotorrested']if record['type'] == 'Bicycle']
