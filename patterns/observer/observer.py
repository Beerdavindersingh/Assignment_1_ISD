from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Sends a message to the observer.

        Args:
            message (str): The message to send.
        """
        pass