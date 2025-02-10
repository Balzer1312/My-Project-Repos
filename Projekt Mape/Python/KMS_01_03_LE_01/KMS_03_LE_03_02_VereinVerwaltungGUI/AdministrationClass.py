from associationClass import AssociationMember




class Administration(AssociationMember):
    def __init__(self,memberID,name,adress,email,entryDate,administrationBody):
        super().__init__(memberID,name,adress ,email,entryDate)
        self.administrationBody = administrationBody

    def __str__(self):
        return (f'Verwaltung: {self.administrationBody}{super().__str__()}')
    
class Chairperson(Administration):
    def __init__(self, memberID, name,adress, email, entryDate, administrationBody,responsibilities):
        super().__init__(memberID, name,adress, email, entryDate, administrationBody)
        self.responsibilities = responsibilities 
    
    def __str__(self):
        return (f'Verantworung:{self.responsibilities}{super().__str__()}\n')

class Treasurer(Administration):
    def __init__(self, memberID, name,adress, email, entryDate, administrationBody,financeArea):
        super().__init__(memberID, name,adress, email, entryDate, administrationBody)
        self.financeArea = financeArea

    def __str__(self):
        return (f'{super().__str__()}\n  Finanzbereich: {self.financeArea}')

class Manager(Administration):
    def __init__(self, memberID, name,adress, email, entryDate, administrationBody, group):
        super().__init__(memberID, name,adress, email, entryDate, administrationBody)
        self.group = group 

    def __str__(self):
        return (f'{super().__str__()}\n  Geplante Events: {self.event}')
