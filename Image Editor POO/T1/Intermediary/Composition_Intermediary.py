from abc import ABC, abstractmethod

class CompIntermediary(ABC):
    @classmethod
    @abstractmethod
    def get_description(cls):
        ...

    @classmethod
    @abstractmethod
    def ask_params(cls,  position, db):
        ...

    @classmethod
    @abstractmethod
    def create_action(cls, position, db):
        ...
    
    @classmethod
    @abstractmethod
    def params(cls):
        ...
    
    @classmethod
    @abstractmethod
    def ScriptAction(cls, dictionary, position, commands):
        ...
