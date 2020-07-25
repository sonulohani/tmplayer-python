from command_invoker import CommandInvoker
from singleton import Singleton
import re


class InputHandler(metaclass=Singleton):
    def __init__(self, invoker: CommandInvoker) -> None:
        self._invoker = invoker

    def handle(self):
        stdin = input().strip()
        command_name = stdin.split(" ")[0]
        command_name_re = re.compile(f"^{command_name}")
        stdin = re.sub(command_name_re, "", stdin)
        arguments = stdin.split(",")
        self._invoker.invoke(command_name, arguments)

