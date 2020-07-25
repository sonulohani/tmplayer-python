#!/usr/bin/python3

import argparse
from globals import APP_VER


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
