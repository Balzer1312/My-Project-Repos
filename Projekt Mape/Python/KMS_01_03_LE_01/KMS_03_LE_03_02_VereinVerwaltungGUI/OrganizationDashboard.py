import tkinter as tk
import os
from tkinter import ttk,messagebox
import customtkinter as ctk
from customtkinter import CTk

from associationClass import AssociationMember,Member
from AdministrationClass import Chairperson,Treasurer,Manager
from UnionManager import ClubManager
from addValidor import Validator
from DBUtilis import DBManager



class OrganizationGUI:
    clubManager=ClubManager()
    validator=Validator()

    def __init__(self,mainFrame):
        self.mainFrame = mainFrame
        self.dynamicFrame = None


############# Interface widgets Funktionen ###############

    def displayWelcomeMessage(self):
        self.welcomeLabel = ctk.CTkLabel(self.mainFrame, text='Wilkommen zur Vereins Verwaltung', font=('Arial', 20))
        self.welcomeLabel.pack(pady=20)
    # Enfernt alle nicht die nicht 
    def removeAllWidgets(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()



########## Mitglieder als CSV abspeichern Interface  ############

    def memberToCsvFrame(self):
        self.removeAllWidgets()
        

        memberTypeLabel = ctk.CTkLabel(self.mainFrame, text='Mitglieder als CSV datei exportieren:',font=('Arial', 16))
        memberTypeLabel.pack(pady=10)

        exportToCsvButton= ctk.CTkButton(self.mainFrame,text='Exportieren',command=self.clubManager.memberToCsvExport)
        exportToCsvButton.pack(pady=10,padx=10)
        
        openCsvFolderButton = ctk.CTkButton(self.mainFrame, text='CSV öffnen', command=lambda: os.startfile(ClubManager.memberlistCSV),state='disabled')
        openCsvFolderButton.pack(pady=10,padx=10)

        readCsvFolderButton = ctk.CTkButton(self.mainFrame, text='CSV Einlesen', command=lambda: self.clubManager.fromCsvToDB(),state='disabled')
        readCsvFolderButton.pack(pady=10,padx=10)

        self.checkCsvFile(openCsvFolderButton, readCsvFolderButton)
    # Überprüfung ob CSV File Existiert
    def checkCsvFile(self, openCsvFolderButton, readCsvFolderButton):

        fileExisting= self.clubManager.memberlistCSV
        if not openCsvFolderButton.winfo_exists():
            if hasattr(self,'afterID'):
                self.mainFrame.after_cancel(self.afterID)
            return
        
        if os.path.exists(fileExisting):
            openCsvFolderButton.configure(state='normal')
            readCsvFolderButton.configure(state='normal')

        else:
            openCsvFolderButton.configure(state='disabled')
            readCsvFolderButton.configure(state='disabled')
        
        self.afterID =self.mainFrame.after(1000,lambda: self.checkCsvFile(openCsvFolderButton,readCsvFolderButton))



##################### Mitglieder Hinzufügen Interface ######################

    def addMember(self):
        self.removeAllWidgets()
        
        backFrame = ctk.CTkFrame(self.mainFrame)
        backFrame.pack(fill='both', expand=True)
        contentFrame=ctk.CTkFrame(backFrame)
        contentFrame.pack(pady=20, padx=20)

        mappingFields=Member.getMapping()  
        self.inputs={}

        def checkInputFields():

        # Button aktivieren, wenn alle Felder gefüllt sind
            if all(entry.get() for entry in self.inputs.values()):
                addButton.configure(state='normal')
                addButton.pack(pady=10)
            else:
                addButton.configure(state='disabled')
            
        
        for text,dbField in mappingFields.items():
        # Label (deutsche Beschreibung des Feldes)
            addMemberlabel = ctk.CTkLabel(contentFrame,text=f'{text}:', font=('Arial', 12))
            addMemberlabel.pack(padx=10, pady=5)

            #Input Feld Überwachung
            inputCheck=tk.StringVar()
            inputCheck.trace_add('write',lambda *args:checkInputFields())

            # Eingabefeld
            AddMemberInputField = ctk.CTkEntry(contentFrame,textvariable=inputCheck)
            AddMemberInputField.pack(padx=10, pady=5)
            self.inputs[dbField] = inputCheck

        title_label = ctk.CTkLabel(self.mainFrame, text='Bitte füllen Sie alle Felder aus, um ein neues Mitglied hinzuzufügen!!', font=('Arial', 18))
        title_label.pack(pady=10)

        addButton=ctk.CTkButton(self.mainFrame,text='Hinzufügen',state='disabled',command=self.getInputData)
        addButton.pack(pady=10)
             
    # Mitglieder input Valedierung und übertragung der Daten in die DB     
    def getInputData(self): 
        

        if hasattr(self, 'errorLabelID') and self.errorLabelID:
            self.errorLabelID.destroy()
            del self.errorLabelID

        if hasattr(self, 'errorLabelMail') and self.errorLabelMail:
            self.errorLabelMail.destroy()
            del self.errorLabelMail

        if hasattr(self, 'errorLabelEntryD') and self.errorLabelEntryD:
            self.errorLabelEntryD.destroy()
            del self.errorLabelEntryD

        if hasattr(self, 'errorLabelGroup') and self.errorLabelGroup:
            self.errorLabelGroup.destroy()
            del self.errorLabelGroup

        inputData={key: var.get() for key,var in self.inputs.items()}
        notValid=False


        if not Validator.validID(inputData):           
            self.errorLabelID = ctk.CTkLabel(self.mainFrame,text='Die Mitglieds-ID existiert oder ist ungültig!', text_color='red', font=('Arial', 12))
            self.errorLabelID.place(x=500, y=60)
            notValid=True       
                
        if not Validator.validEmail(inputData):    
            self.errorLabelMail = ctk.CTkLabel(self.mainFrame,text='Die E-Mail ist nicht Gültig!', text_color='red', font=('Arial', 12))
            self.errorLabelMail.place(x=500, y=80)
            notValid=True
           
        if not Validator.validEntryDate(inputData):
            self.errorLabelEntryD = ctk.CTkLabel(self.mainFrame,text='Ungültiges Datum!', text_color='red', font=('Arial', 12))
            self.errorLabelEntryD.place(x=500, y=100)
            notValid=True

        if not Validator.validGroup(inputData):
            self.errorLabelGroup = ctk.CTkLabel(self.mainFrame,text='Ungültige Gruppe!', text_color='red', font=('Arial', 12))
            self.errorLabelGroup.place(x=500, y=120)
            notValid=True
                      
        if notValid:
            return
        else:
            DBManager.insertData(inputData)
            self.clubManager.getDataFromDB()
            
               
###################### Mitglieder Verwaltung Interface #############

    def manageMember(self):

        self.removeAllWidgets()

        titleLabel = ctk.CTkLabel(self.mainFrame, text='Bitte geben sie die ID für das Bearbeiten ein:', font=('Arial', 14))
        titleLabel.pack(pady=10)

        searchFrame = ctk.CTkFrame(self.mainFrame)
        searchFrame.pack(pady=10)

        searchLabel = ctk.CTkLabel(searchFrame, text='Nach ID suchen:')
        searchLabel.grid(row=0, column=0, padx=10, pady=5)

        searchEntry = ctk.CTkEntry(searchFrame)
        searchEntry.grid(row=0, column=1, padx=10, pady=5)

        self.listFrame = ctk.CTkFrame(self.mainFrame)
        self.listFrame.pack(fill='both', expand=True, padx=10, pady=10)

        searchButton = ctk.CTkButton(searchFrame, text='Suchen',command= lambda:self.populateMemberFields(searchEntry.get()))
        searchButton.grid(row=0, column=2, padx=10, pady=5)

    def populateMemberFields(self, memberID):


    # Löscht vorhandene Widgets im dynamischen Frame
        if not hasattr(self, 'dynamicFrame') or not self.dynamicFrame:
            self.dynamicFrame = ctk.CTkFrame(self.listFrame)
            self.dynamicFrame.pack(pady=10)
        else:
            for widget in self.dynamicFrame.winfo_children():
                widget.destroy()

        # Mitglied in allMemberlist suchen
        columns = ['memberID', 'name', 'adress', 'email', 'entryDate', 'administrationBody', 'responsibilities', 'financeArea', 'group']
        member = next((dict(zip(columns, m)) for m in self.clubManager.allMemberlist if str(m[0]) == memberID),None)
        

        if not member:
            # Fehlermeldung anzeigen, falls die ID nicht existiert
            ctk.CTkLabel(self.dynamicFrame, text='Mitglied nicht gefunden!', font=('Arial', 16)).pack(pady=10)
            return

        memberObj=ClubManager.memberToObjektFactory(member)  

        # Dynamische Felder für das Mitglied anzeigen
        inputValues = {}
        editableFields = ['name', 'adress',]

        for idx, field in enumerate(editableFields):
    # Attribute im Objekt sind in Kleinbuchstaben, hier wird Groß-/Kleinschreibung für Darstellung angepasst
            attr_name = field.lower()
            ctk.CTkLabel(self.dynamicFrame, text=field + ':').grid(row=idx, column=0, padx=10, pady=5)
            input_var = ctk.StringVar(value=getattr(memberObj, attr_name))  # Holt den aktuellen Wert aus dem Objekt
            inputValues[attr_name] = input_var
            ctk.CTkEntry(self.dynamicFrame, textvariable=input_var).grid(row=idx, column=1, padx=10, pady=5)

        # Zusätzliche Felder nur anzeigen
        if isinstance(memberObj, Chairperson):
            ctk.CTkLabel(self.dynamicFrame, text='Verantwortung:').grid(row=len(editableFields), column=0, padx=10, pady=5)
            responsibility_var = ctk.StringVar(value=memberObj.responsibilities)
            ctk.CTkLabel(self.dynamicFrame, textvariable=responsibility_var).grid(row=len(editableFields), column=1, padx=10, pady=5)

        elif isinstance(memberObj, Treasurer):
            ctk.CTkLabel(self.dynamicFrame, text='Finanzbereich:').grid(row=len(editableFields), column=0, padx=10, pady=5)
            finance_area_var = ctk.StringVar(value=memberObj.financeArea)
            ctk.CTkLabel(self.dynamicFrame, textvariable=finance_area_var).grid(row=len(editableFields), column=1, padx=10, pady=5)

        elif isinstance(memberObj, Manager):
            ctk.CTkLabel(self.dynamicFrame, text='Gruppe:').grid(row=len(editableFields), column=0, padx=10, pady=5)
            events_var = ctk.StringVar(value=memberObj.group)  # Manager hat 'group' als 'Geplante Events'
            inputValues['group'] = events_var
            ctk.CTkEntry(self.dynamicFrame, textvariable=events_var).grid(row=len(editableFields), column=1, padx=10, pady=5)

        elif isinstance(memberObj, Member):
            ctk.CTkLabel(self.dynamicFrame, text='Gruppe:').grid(row=len(editableFields), column=0, padx=10, pady=5)
            group_var = ctk.StringVar(value=memberObj.group)
            inputValues['group'] = group_var
            ctk.CTkEntry(self.dynamicFrame, textvariable=group_var).grid(row=len(editableFields), column=1, padx=10, pady=5)

        # Rolle anzeigen (nicht bearbeitbar)
        ctk.CTkLabel(self.dynamicFrame, text='Rolle:').grid(row=len(editableFields) + 1, column=0, padx=10, pady=5)
        role_var = ctk.StringVar(value=type(memberObj).__name__)  # Typ des Objekts als Rolle
        ctk.CTkLabel(self.dynamicFrame, textvariable=role_var).grid(row=len(editableFields) + 1, column=1, padx=10, pady=5)

        # Speichern-Button
        ctk.CTkButton(self.dynamicFrame,text='Änderungen speichern',command=lambda: self.saveChanges(memberObj, inputValues)).grid(row=len(editableFields) + 2, column=0, columnspan=2, pady=20)

        # Daten werden umgewandelt und der DB zu Updaten übergeben

    def saveChanges(self, memberObj, inputValues):


        # Aktualisiere die Werte im Member-Objekt
        for field, var in inputValues.items():
            setattr(memberObj, field, var.get())  # Aktualisiere die Attribute im Objekt
            
            # Bereite die Daten für das Update vor
        updateData = {
            'memberID': memberObj.memberID,
            'name': memberObj.name,
            'adress': memberObj.adress
        }
            
        if not updateData.get('name') or not updateData.get('adress'):
            messagebox.showerror('Fehler', 'Name und Adresse dürfen nicht leer sein.')
            return

            # Füge spezifische Felder für Rollen hinzu
        if isinstance(memberObj, Manager) or isinstance(memberObj, Member):
                updateData['group'] = memberObj.group

            # Sende die Daten an die Datenbank
        DBManager.updateDataToDB(updateData)
                    
                    
                    
            
                 
                   