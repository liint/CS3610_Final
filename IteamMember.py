#the observer interface
from abc import abstractmethod, ABC

class IteamMember(ABC):
    def __init__(self, name, task = None):
        self.__name = name
        self.__task = task
        self.__memberState = None
    
    @abstractmethod
    def update(self, context):
        pass
    
    @property
    def memberState(self):
        return self.__memberState
    
    @memberState.setter
    def memberState(self, state):
        self.__memberState = state
        
    @property
    def task(self):
        return self.__task
        
    @task.setter
    def task(self, task):
        self.__task = task
        
    @property
    def name(self):
        return self.__name
    