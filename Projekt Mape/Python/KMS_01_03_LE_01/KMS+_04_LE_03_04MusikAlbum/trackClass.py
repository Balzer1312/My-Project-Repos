class Track:
    def __init__(self,title,length):
        self.title =title
        self.length = length


        
    def __str__(self):
        return f'{self.title} ({self.length})'