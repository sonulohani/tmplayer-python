from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, arguments: object) -> None:
        pass

