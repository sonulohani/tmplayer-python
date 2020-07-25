from sys import exit

from command import Command


class QuitCommand(Command):
    def execute(self, arguments: object) -> None:
        exit()

    def command_type(self) -> Command.CommandType:
        return Command.CommandType.QUIT
