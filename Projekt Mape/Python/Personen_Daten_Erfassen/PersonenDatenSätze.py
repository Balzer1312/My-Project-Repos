from datetime import datetime
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

months = ['Geb.Monat filtern','Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']

######################   Personen Daten werden von der CSV eingelesen und gefiltert ####################
def csvToRecords():
    data = pd.read_csv("Data.csv")
    filter = ['Mitarbeiter', 'Besucher']
    sortRecords = {row['ID']: row.to_dict() for _, row in data.iterrows() if row['Type'] in filter}
    return sortRecords

#####################   Neue Personen Daten werden in die Data.csv gespeichert ###################
def entryNewData(newData):
    for person, info in newData.items():
        data = [info['ID'], info['Vorname'], info['Nachname'], info['Geburtstag'], info['Telefonnummer'], info['E-mail'], info['Adresse'], info['Type']]
    newEntry = pd.DataFrame([data])
    newEntry.to_csv("Data.csv", mode='a', index=False, header=False)

#####################   Prüft, ob eine ID bereits in der CSV-Datei existiert ###################
def idExistsInCSV(id):
    try:
        data = pd.read_csv("Data.csv", dtype={'ID': str})
        return id in data['ID'].values
    except FileNotFoundError:
        return False

#################   Das wechseln der Interfaces   #############################
def showFrame(frame):
    mainFrame.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame.pack(fill='both')

########################### Personen Daten ändern ################################
def getData(idEntry):
    userId = idEntry.get().strip()
    records = csvToRecords()
    for person, data in records.items():
        if str(person) == userId:
            dataId.config(state='normal')
            dataId.delete(0, tk.END)
            dataId.insert(0, data['ID'])
            dataId.config(state='readonly')
            dataFirstname.delete(0, tk.END)
            dataFirstname.insert(0, data['Vorname'])
            dataLastname.delete(0, tk.END)
            dataLastname.insert(0, data['Nachname'])
            databirth.delete(0, tk.END)
            databirth.insert(0, data['Geburtstag'])
            dataContact.delete(0, tk.END)
            dataContact.insert(0, data['Telefonnummer'])
            dataLocation.delete(0, tk.END)
            dataLocation.insert(0, data['Adresse'])
            dataEmail.delete(0, tk.END)
            dataEmail.insert(0, data['E-mail'])
            return
    messagebox.showerror('Suche Fehlgeschlagen', 'Diese ID ist nicht vergeben')
    idEntry.delete(0, tk.END)

#  Bestehender Daten satz wird Aktualisiert
def saveUpdatedData():
    entryFields = {
        'ID': dataId.get().strip(),
        'Vorname': dataFirstname.get().strip(),
        'Nachname': dataLastname.get().strip(),
        'Geburtstag': databirth.get().strip(),
        'Telefonnummer': dataContact.get().strip(),
        'E-mail': dataEmail.get().strip(),
        'Adresse': dataLocation.get().strip()
    }
    if not validInputs(entryFields, False, 'frame2'):  # Validierung für frame2 aufrufen
        messagebox.showerror("Fehler", "Einige Eingaben sind ungültig. Bitte korrigieren.")
        return

    updatedData = {
        'ID': dataId.get().strip(),
        'Vorname': dataFirstname.get().strip(),
        'Nachname': dataLastname.get().strip(),
        'Geburtstag': databirth.get().strip(),
        'Telefonnummer': dataContact.get().strip(),
        'E-mail': dataEmail.get().strip(),
        'Adresse': dataLocation.get().strip()
    }

    # Lesen des CSV Datensatzes und Ersetzen des Datensatzes mit der passenden ID
    data = pd.read_csv("Data.csv", dtype={'ID': str, 'Telefonnummer': str})
    data.set_index('ID', inplace=True)

    if updatedData['ID'] in data.index:
        for key, value in updatedData.items():
            if key != 'ID':
                data.at[updatedData['ID'], key] = value
        data.reset_index(inplace=True)
        data.to_csv("Data.csv", index=False)
        messagebox.showinfo("Speichern Erfolgreich", "Die geänderten Daten wurden erfolgreich gespeichert.")
    else:
        messagebox.showerror("Fehler", "Die ID wurde nicht im Datensatz gefunden.")

    # Eingabefelder leeren nach erfolgreicher Speicherung
    clearFields(frame='frame2')

############################  Validierung der Eingaben   ###################################
def validInputs(entryFields, showErrors, frame):
    isValid = True

    def showError(error, frame, widget, message=None):
        if frame == "frame1":
            error.place(x=380, y=widget.winfo_y())
        elif frame == "frame2" and showErrors:
            messagebox.showerror("Fehler", message)

    # ID Validierung nur für Mitarbeiter (nicht für Besucher)
    if frame == 'frame1' and pickType.get() == 'Mitarbeiter':
        if not entryFields.get('ID') or not re.match(r'^\d{10}$', entryFields.get('ID')) or idExistsInCSV(entryFields.get('ID')):
            showError(errorId, frame, entryId, "Die ID ist ungültig oder bereits vergeben.")
            entryId.delete(0, tk.END)
            isValid = False
        else:
            errorId.place_forget()

    # Vorname Validierung
    if not entryFields.get('Vorname') or re.search(r'[!"§$%&/()=?0-9\[\]{}\\,.;:@#~<>|^°+*]', entryFields.get('Vorname')):
        showError(errorFirstname, frame, entryFirstname, "Vorname enthält ungültige Zeichen.")
        entryFirstname.delete(0, tk.END)
        isValid = False
    elif frame == "frame1":
        errorFirstname.place_forget()

    # Nachname Validierung
    if not entryFields.get('Nachname') or re.search(r'[!"§$%&/()=?0-9\[\]{}\\,.;:@#~<>|^°+*]', entryFields.get('Nachname')):
        showError(errorLastname, frame, entryLastname, "Nachname enthält ungültige Zeichen.")
        entryLastname.delete(0, tk.END)
        isValid = False
    elif frame == "frame1":
        errorLastname.place_forget()

    # Geburtsdatum Validierung
    try:
        datetime.strptime(entryFields.get('Geburtstag'), "%d.%m.%y")
        if frame == "frame1":
            errorBirth.place_forget()
    except ValueError:
        showError(errorBirth, frame, entrybirth, "Geburtsdatum ist im falschen Format.")
        entrybirth.delete(0, tk.END)
        isValid = False

    # Telefonnummer Validierung
    if not re.match(r'^\d{10,15}$', entryFields.get('Telefonnummer')):
        showError(errorContact, frame, entryContact, "Telefonnummer ist ungültig.")
        entryContact.delete(0, tk.END)
        isValid = False
    elif frame == "frame1":
        errorContact.place_forget()

    # Adresse Validierung
    if not entryFields.get('Adresse') or re.search(r'[!§$%&()=?\[\]{}\\;@#~<>|^°+*]', entryFields.get('Adresse')):
        showError(errorLocation, frame, entryLocation, "Adresse enthält ungültige Zeichen.")
        entryLocation.delete(0, tk.END)
        isValid = False
    elif frame == "frame1":
        errorLocation.place_forget()

    # E-Mail Validierung
    if not re.match(r'^[a-zA-Z0-9]+(?:[\._-][a-zA-Z0-9]+)*@[a-zA-Z\d-]+(?:\.[a-zA-Z]{2,})+$', entryFields.get('E-mail')):
        showError(errorEmail, frame, entryEmail, "E-Mail ist ungültig.")
        entryEmail.delete(0, tk.END)
        isValid = False
    elif frame == "frame1":
        errorEmail.place_forget()

    return isValid

############## Funktion wird von saveButton als command aufgerufen. Zuerst wird die Validierung gestartet und bei Erfolg in die "Data.csv" zu speichern ###############
def saveData():
    entryFields = {
        'ID': entryId.get().strip() if pickType.get() == 'Mitarbeiter' else "",
        'Vorname': entryFirstname.get().strip(),
        'Nachname': entryLastname.get().strip(),
        'Geburtstag': entrybirth.get().strip(),
        'Telefonnummer': entryContact.get().strip(),
        'E-mail': entryEmail.get().strip(),
        'Adresse': entryLocation.get().strip(),
        'Type': pickType.get().strip()
    }

    if not validInputs(entryFields, True, 'frame1'):
        return

    personData = {}
    if pickType.get().strip() == 'Mitarbeiter':
        personData = {entryId.get().strip(): entryFields}
    else:
        visitorCount = sum(1 for person in csvToRecords().values() if person['Type'] == 'Besucher') + 1
        entryFields['ID'] = visitorCount  # Generierte ID für Besucher
        personData = {visitorCount: entryFields}

    entryNewData(personData)
    clearFields(frame='frame1')

def clearFields(frame):
    if frame == 'frame1':
        entryFirstname.delete(0, tk.END)
        setTxtEntry(entryFirstname,'z.B.: >  Max  <')
        entryLastname.delete(0, tk.END)
        setTxtEntry(entryLastname, 'z.B.: >  Mustermann  <')
        entrybirth.delete(0, tk.END)
        setTxtEntry(entrybirth, '>  (TT.MM.JJ)  < ')
        entryContact.delete(0, tk.END)
        setTxtEntry(entryContact, 'z.B.: >  436601234567  <')
        entryEmail.delete(0, tk.END)
        setTxtEntry(entryEmail,'z.B.: >  Muster@mail.com  <')
        entryLocation.delete(0, tk.END)
        setTxtEntry(entryLocation, 'z.B.:>  Musterstraße 12  <')
        entryId.delete(0, tk.END)
        setTxtEntry(entryId, 'Bitte 10 stellige zahl eingeben ')
    elif frame == 'frame2':
        dataFirstname.delete(0, tk.END)
        dataLastname.delete(0, tk.END)
        databirth.delete(0, tk.END)
        dataContact.delete(0, tk.END)
        dataLocation.delete(0, tk.END)
        dataEmail.delete(0, tk.END)
        dataId.config(state='normal')
        dataId.delete(0, tk.END)
        dataId.config(state='readonly')
    hideErrors()

def hideErrors():
    for error in [errorFirstname, errorLastname, errorBirth, errorContact, errorLocation, errorEmail, errorId]:
        error.place_forget()
def showPersonData():
    selectOutput = selectType.get()
    selectedMonth = selectbirth.get()
    records = csvToRecords()

    outputData.config(state='normal')
    outputData.delete('1.0', tk.END)

    for id, person in records.items():
        # Filter für Typ (Mitarbeiter/Besucher) anwenden
        if selectOutput == 'Alle' or person['Type'] == selectOutput:
            birthday = person.get('Geburtstag')

            # Filter für Geburtsmonat, wenn ein spezifischer Monat ausgewählt ist
            if selectedMonth != 'Geb.Monat filtern':
                try:
                    birth_date = datetime.strptime(birthday, "%d.%m.%y")
                    if birth_date.month != months.index(selectedMonth):  # Nur weiter, wenn Monat übereinstimmt
                        continue
                    # Berechne Tage bis zum nächsten Geburtstag
                    today = datetime.today()
                    next_birthday = birth_date.replace(year=today.year)
                    if next_birthday < today:
                        next_birthday = next_birthday.replace(year=today.year + 1)
                    days_to_birthday = (next_birthday - today).days
                    birthday_info = f"Tage bis zum nächsten Geburtstag: {days_to_birthday}\n\n"
                except ValueError:
                    birthday_info = "Ungültiges Geburtsdatum\n\n"
            else:
                birthday_info = "\n"

            # Standarddatenausgabe
            firstname = person.get('Vorname')
            lastname = person.get('Nachname')
            contact = person.get('Telefonnummer')
            mail = person.get('E-mail')
            location = person.get('Adresse')
            recordData = (
                f"ID: {id}\n"
                f"Typ: {person['Type']}\n"
                f"Vorname: {firstname}\n"
                f"Nachname: {lastname}\n"
                f"Geburtstag: {birthday}\n"
                f"Telefonnummer: +{contact}\n"
                f"Email: {mail}\n"
                f"Adresse: {location}\n"
                f"{birthday_info}"
            )
            outputData.insert(tk.END, recordData)
    outputData.config(state='disabled')

def updateInputfield(_=None):
    # Blendet die ID-Felder für Besucher aus und zeigt sie für Mitarbeiter an
    if pickType.get() == 'Besucher':
        labelId.pack_forget()
        entryId.pack_forget()
    else:
        labelId.pack()
        entryId.pack()

#################  Reinigt das eingabe Feld von Platzhalter bei Anwahl #########################

def clearEntry(_, entry, placeholder):

    if entry.get() == placeholder:
        entry.delete(0,'end')
        entry.config(fg='black') # Setzt die Input farbe wieder auf Schwarz

################# Setzt den Platzhalter für das eingabe feld #######################
def setTxtEntry(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg='grey')
    entry.bind('<FocusIn>', lambda _: clearEntry(_, entry, placeholder))   #Bei Anwahl des eingabe Felds wird das Event ausgelöst und ruft ClearEntry() mit den parametern auf
    entry.bind('<FocusOut>', lambda _: addTxtEntry(_, entry, placeholder)) #Bei Abwahl des eingabe Felds wird das Event ausgelöst und ruft addTxtEntry() mit den parametern auf

################ Fügt bei abwahl des eingabe Feldes den Platzhalter wieder zu ########################
def addTxtEntry(_,entry,placeholder):

    if entry.get()=='':
        entry.insert(0,placeholder)
        entry.config(fg='grey')

root = tk.Tk()
root.title('Personen Daten')
root.geometry('550x600')
root.resizable(False, False)
mainFrame = tk.Frame(root)
mainFrame.pack(fill='both')

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
#########################  Hauptmenü frame  #####################
mainlabel = tk.Label(mainFrame, text='Bitte wählen sie aus:')
mainlabel.pack()

mainButton1 = tk.Button(mainFrame, text='Personen Daten erfassen', width=30, height=10, command=lambda: showFrame(frame1))
mainButton1.pack(pady=20)

mainButton2 = tk.Button(mainFrame, text='Personen Daten ändern', width=30, height=10, command=lambda: showFrame(frame2))
mainButton2.pack(pady=20)

mainButton3 = tk.Button(mainFrame, text='Personen Ausgabe', width=30, height=10, command=lambda: showFrame(frame3))
mainButton3.pack(pady=20)

################## Personen Daten erfassen Interface (frame1)###########################
frame1Title = tk.Label(frame1, text='Personen Daten erfassen', font=('Arial', 16))
frame1Title.pack(pady=10)

pickType = ttk.Combobox(frame1, values=['Besucher', 'Mitarbeiter'], state='readonly')
pickType.current(1)
pickType.pack()
pickType.bind('<<ComboboxSelected>>', lambda e: updateInputfield())

labelFirstname = tk.Label(frame1, text='Vorname:')
labelFirstname.pack()
entryFirstname = tk.Entry(frame1, width=30)
entryFirstname.pack()
errorFirstname = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entryFirstname,'z.B.: >  Max  <')

labelLastname = tk.Label(frame1, text='Nachname:')
labelLastname.pack()
entryLastname = tk.Entry(frame1, width=30)
entryLastname.pack(pady=5)
errorLastname = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entryLastname, 'z.B.: >  Mustermann  <')

labelbirth = tk.Label(frame1, text='Geburtstag:')
labelbirth.pack()
entrybirth = tk.Entry(frame1, width=30)
entrybirth.pack(pady=5)
errorBirth = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entrybirth, '>  (TT.MM.JJ)  < ')

labelContact = tk.Label(frame1, text='Telefonnummer:')
labelContact.pack()
entryContact = tk.Entry(frame1, width=30)
entryContact.pack(pady=5)
errorContact = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entryContact, 'z.B.: >  436601234567  <')

labelLocation = tk.Label(frame1, text='Adresse:')
labelLocation.pack()
entryLocation = tk.Entry(frame1, width=30)
entryLocation.pack(pady=5)
errorLocation = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entryLocation, 'z.B.:>  Musterstraße 12  <')

labelEmail = tk.Label(frame1, text="E-Mail:")
labelEmail.pack()
entryEmail = tk.Entry(frame1, width=30)
entryEmail.pack(pady=5)
errorEmail = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entryEmail,'z.B.: >  Muster@mail.com  <')

labelId = tk.Label(frame1, text='Sozial-Versicherungsnummer:')
labelId.pack()
entryId = tk.Entry(frame1, width=30)
entryId.pack(pady=5)
errorId = tk.Label(frame1, text='✘', fg='red', font=('Arial', 12))
setTxtEntry(entryId,'Bitte 10 stellige zahl eingeben ')

saveButton = tk.Button(frame1, text="Daten speichern", command=saveData)
saveButton.pack(side='bottom', pady=10)

backButton = tk.Button(frame1, text='← Hauptmenü', command=lambda: showFrame(mainFrame), width=10)
backButton.place(x=10, y=10)

##################### Personen Daten ändern Interface (frame2)################################
frame2Title = tk.Label(frame2, text='Personen Daten ändern', font=('Arial', 16))
frame2Title.pack(pady=10)

inputInfo = tk.Label(frame2, text='Bitte geben sie ihre ID ein:', font=('Arial', 10))
inputInfo.pack(pady=(10, 5), anchor='w')
idInput = tk.Entry(frame2, width=30)
idInput.pack(pady=(0, 20), anchor='w')

searchButton = tk.Button(frame2, text="Suchen", command=lambda: getData(idInput))
searchButton.pack(pady=(0, 10), anchor='w')

showId = tk.Label(frame2, text='ID:')
showId.pack(anchor='w')
dataId = tk.Entry(frame2, width=30, state='readonly')
dataId.pack(anchor='w')

showFirstname = tk.Label(frame2, text='Vorname:')
showFirstname.pack(anchor='w')
dataFirstname = tk.Entry(frame2, width=30)
dataFirstname.pack(anchor='w')

showLastname = tk.Label(frame2, text='Nachname:')
showLastname.pack(anchor='w')
dataLastname = tk.Entry(frame2, width=30)
dataLastname.pack(anchor='w')

showbirth = tk.Label(frame2, text='Geburtstag:')
showbirth.pack(anchor='w')
databirth = tk.Entry(frame2, width=30)
databirth.pack(anchor='w')

showContact = tk.Label(frame2, text='Telefonnummer:')
showContact.pack(anchor='w')
dataContact = tk.Entry(frame2, width=30)
dataContact.pack(anchor='w')

showLocation = tk.Label(frame2, text='Adresse:')
showLocation.pack(anchor='w')
dataLocation = tk.Entry(frame2, width=30)
dataLocation.pack(anchor='w')

showEmail = tk.Label(frame2, text="E-Mail:")
showEmail.pack(anchor='w')
dataEmail = tk.Entry(frame2, width=30)
dataEmail.pack(anchor='w')

saveChangesButton = tk.Button(frame2, text="Änderungen speichern", command=saveUpdatedData)
saveChangesButton.pack(pady=10, anchor='w')

backButton = tk.Button(frame2, text='← Hauptmenü', command=lambda: showFrame(mainFrame), width=10)
backButton.place(x=10, y=10)

################## Personen Ausgabe Interface (frame3)######################
frame3Title = tk.Label(frame3, text='Personen Ausgabe', font=('Arial', 16))
frame3Title.pack()

labelChoice = tk.Label(frame3, text='Bitte wählen sie was sie ausgeben möchten:', font=('Arial', 10))
labelChoice.place(x=10, y=60)

selectType = ttk.Combobox(frame3, values=['Alle', 'Mitarbeiter', 'Besucher'], state='readonly')
selectType.current(0)
selectType.place(x=10, y=95)

selectbirth = ttk.Combobox(frame3, values=months, state='readonly')
selectbirth.current(0)
selectbirth.place(x=160, y=95)

showDataButton = tk.Button(frame3, text='Daten anzeigen', command=showPersonData)
showDataButton.pack(side='bottom', pady=10)

outputData = tk.Text(frame3, height=30, wrap='word', font=('Arial', 12), state='disabled')
outputData.pack(fill='both', expand=True, padx=10, pady=(100, 0))

backButton = tk.Button(frame3, text='← Hauptmenü', command=lambda: showFrame(mainFrame), width=10)
backButton.place(x=10, y=10)

showFrame(mainFrame)
root.mainloop()
