#the publisher class

class task:
    def __init__(self, name, state = None):
        self.__members = set()
        self.__name = name
        self.__subjectState = state
        
    def addMember(self, teamMember):
        if teamMember in self.__members:
            print(f"{teamMember.name} is already on this task")
        elif teamMember.task != None:
            print(f"{teamMember.name} is already working on another task")
        else:
            self.__members.add(teamMember)
            self.__notify(f"{teamMember.name} has been added to {self.name}")
            teamMember.task = self
        
    def removeMember(self, teamMember):
        if teamMember in self.__members:
            self.__members.remove(teamMember)
            self.__notify(f"{teamMember.name} has been removed from {self.name}")
            teamMember.task = self
        else:
            print(f"{teamMember.name} is already off this task")
        
    def __notify(self, update):
        for i in self.__members:
            i.update(update)
            print(f"To {i.name}: {update}")
    
    @property
    def subjectState(self):
        return self.__subjectState
        
    @subjectState.setter
    def subjectState(self, state):
        self.__subjectState = state
        self.__notify(state)
        
    @property
    def name(self):
        return self.__name
        
    @property
    def members(self):
        return self.__members
    
    
    
    
    
    
    
    
    
    
    