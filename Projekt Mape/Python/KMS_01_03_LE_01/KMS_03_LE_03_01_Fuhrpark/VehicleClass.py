import json
import os
from tkinter import messagebox
from JsonHandler import JsonHandler


class Vehicle: 
    def __init__(self, type, color, model, brand):
        self.type = type
        self.color = color
        self.model = model
        self.brand = brand
   

    def __str__(self):
        return (f' Farbe: {self.color}\n Modell: {self.model}\n Marke: {self.brand}\n')  