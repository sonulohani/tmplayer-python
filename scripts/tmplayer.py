#!/usr/bin/python3

import argparse
from time import sleep

from globals import APP_VER
from input_handler import InputHandler
from command_invoker import CommandInvoker
from quit_command import QuitCommand


def setup_arguments(description: str):
    arg_parser = argparse.ArgumentParser(description=description)
    arg_parser.add_argument(
        "-v", "--version", action="store_true", help="TMPlayer version"
    )
    return arg_parser.parse_args()


def show_version():
    print(f"TMPlayer version {APP_VER}")


if __name__ == "__main__":
    args = setup_arguments("TMPlayer")
    if args.version:
        show_version()

    invoker = CommandInvoker()
    invoker.register_command(QuitCommand())

    handler = InputHandler(invoker)

    while True:
        handler.handle()
        sleep(1)
