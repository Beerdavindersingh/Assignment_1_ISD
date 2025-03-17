from patterns.observer.observer import Observer

class subject:
    def __init__(self) -> None:
        """
        Creates a subject with no observers.
        """
        self.__observer = []

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer if it's not already in the list.

        Args:
            observer (Observer): The observer to add.
        """
        if observer not in self.__observer:
            self.__observer.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer if it's in the list.

        Args:
            observer (Observer): The observer to remove.
        """
        if observer in self.__observer:
            self.__observer.remove(observer)

    def notify(self, message: str) -> None:
        """
        Sends a message to all observers.

        Args:
            message (str): The message to send.
        """
        for observer in self.__observer:
            observer.update(message)