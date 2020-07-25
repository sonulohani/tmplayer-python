from command import Command
from sys import exit


class QuitCommand(Command):
    def execute(self, arguments: object) -> None:
        exit()
