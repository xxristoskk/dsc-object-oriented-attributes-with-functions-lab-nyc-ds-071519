class School():
    def __init__(self, name):
        self.name = name
        self.roster = {}
        pass
    def add_student(self,name,grade):
        self.roster[grade] = [name]
        pass
