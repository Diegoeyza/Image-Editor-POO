from abc import ABC, abstractmethod
from typing import Optional

class FilterIntermediary(ABC):
    @classmethod
    @abstractmethod
    def get_description(cls):
        ...

    @classmethod
    @abstractmethod
    def ask_params(cls, position: Optional[int], db: Optional[dict]):
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