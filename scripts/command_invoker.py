from enum import IntEnum

from command import Command


class CommandInvoker:

    command_map = {
        "play": Command.CommandType.PLAY,
        "pause": Command.CommandType.PAUSE,
        "add": Command.CommandType.ADD,
        "shuffle": Command.CommandType.SHUFFLE,
        "quit": Command.CommandType.QUIT,
    }

    def __init__(self) -> None:
        self._type_to_command = {}

    def register_command(self, cmd: Command):
        self._type_to_command[cmd.command_type()] = cmd

    def invoke(self, command_str: str, arguments: object):
        if self.command_map.get(command_str):
            command = self._type_to_command[self.command_map[command_str]]
            command.execute(arguments)
