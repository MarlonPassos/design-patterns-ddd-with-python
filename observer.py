import abc

from command import Command


class Observer(abc.ABC):
    operation: str

    @abc.abstractmethod
    def notify(self, command: Command) -> None:
        raise NotImplementedError
