import abc


class Command(abc.ABC):
    operation: str

    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError
