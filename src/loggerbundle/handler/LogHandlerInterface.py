from abc import ABC, abstractmethod
from logging import Handler

class LogHandlerInterface(ABC):

    @abstractmethod
    def create(self) -> Handler:
        pass
