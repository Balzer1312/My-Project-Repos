from KontoVerwalungsKlassen import AccountService,BankAccount
import datetime


def main_Menu():
   
    
    while True:
        print('\nWillkommen bei der MusterBank')
        AccountService.loadAccounts()
        print('1. Konten Verwalten    (Konten löschen, Alle Konten Anzeigen )')
        print('2. Konto Funktionen    (Auszahlen, Einzahlen, Konto Anzeigen)')
        print('3. Programm beenden')

        try:
            choice = int(input('Ihre Eingabe:'))
            if choice == 1:
                accountManagement()
            elif choice == 2:
                bankAccount()
            elif choice == 3:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')


def accountManagement():
    while True:
        print('\nWillkomen Mitarbeiter in der Konten Verwaltung')
        print('1. Alle Konten anzeigen')
        print('2. Konto Anlegen')
        print('3. Konto Löschen')
        print('4. Zurück in Hauptmenü')

        try:
            choice = int(input('Ihre Eingabe:'))
            if choice == 1:
                AccountService.showallAccounts()
                continue
            elif choice == 2:
                name=str(input('Bitte Namen Eingeben:'))
                iban=str(input('Bitte neuen IBAN Eingeben:'))
                balance=float(input('Ihren Betrag Eingeben:'))
                AccountService.createAccount(name, iban, balance)
                continue
            elif choice == 3:
                iban= str(input('Bitte IBAN zum löschen Eingeben:'))
                AccountService.deleteAccount(iban)
                continue
            elif choice == 4:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')


def bankAccount():
    

    while True:
        print('\nWillkomen in deiner Konten Verwaltung')
        print('1. Konto Anzeigen')
        print('2. Abheben')
        print('3. Einzahlen')
        print('4. Zurück in Hauptmenü')

        try:
            choice = int(input('Ihre Eingabe:'))
            if choice == 1:
                iban= str(input('Bitte IBAN zum Konto anzeigen Eingeben:'))
                AccountService.showOneAccount(iban)
                continue
            elif choice == 2:
                iban= str(input('IBAN für Auszahlung eingeben:'))
                amount=float(input('Bitte Auszahlung betrag Angeben (Bsp.:123.45):'))
                account = AccountService.bankAccounts.get(iban)
                if account:
                    account.withdraw(amount)
                    print('\nIhr neuer Kontostand:')
                    AccountService.showOneAccount(iban)
                continue

            elif choice == 3:
                iban = input('IBAN für Einzahlung eingeben:')
                if iban in AccountService.bankAccounts:
                    amount = float(input('Betrag zum Einzahlen eingeben (z.B. 123.45):'))
                    AccountService.bankAccounts[iban].deposit(amount)
                    print('\nIhr neuer Kontostand:')
                    AccountService.showOneAccount(iban)
                continue

            elif choice == 4:
                break
            else:
                print('Ungültige Eingabe')
        except ValueError:
            print('Bitte geben Sie eine Zahl ein.')

main_Menu()

