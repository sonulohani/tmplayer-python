from abc import ABCMeta, abstractmethod
from enum import IntEnum


class Command(metaclass=ABCMeta):
    class CommandType(IntEnum):
        PLAY = 0
        PAUSE = 1
        ADD = 2
        SHUFFLE = 3
        QUIT = 4
        NONE = -1

    @abstractmethod
    def execute(self, arguments: object = None) -> None:
        pass

    def command_type(self) -> CommandType:
        return Command.CommandType.NONE

