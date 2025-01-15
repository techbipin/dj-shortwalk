#!/usr/bin/env python

import os
import sys
import subprocess
from pathlib import Path
from shortcut_keys import KEYS


def run(command=None, *arguments):
    '''
    
    This function runs a specified Django management command along with any given arguments.
    It allows executing commands like migrations, tests, and custom management commands directly from the code.
    
    Parameters -
    command (str): The Django management command to execute, such as 'migrate', 'test', or any custom command.
    arguments (tuple): A tuple of arguments that will be passed to the command.
    
    '''

    if not command:
        sys.exit("dj-shortwalk: No command provided. Please specify a command.")

    command = KEYS.get(command, command)

    try:
        if command == 'startproject':
            return subprocess.run(["django-admin.py", "startproject", *arguments], check=True)

        script_path = os.getcwd()

        manage_py_path = None
        for parent in Path(script_path).parents:
            potential_manage_py = parent / 'manage.py'
            if potential_manage_py.exists():
                manage_py_path = potential_manage_py
                break

        if not manage_py_path:
            sys.exit("dj-shortwalk: 'manage.py' not found in this directory or its parents.")

        return subprocess.run([sys.executable, str(manage_py_path), command, *arguments], check=True)

    except FileNotFoundError as e:
        sys.exit(f"dj-shortwalk: File not found error - {e}")
    except subprocess.CalledProcessError as e:
        sys.exit(f"dj-shortwalk: Command execution failed with error - {e}")
    except Exception as e:
        sys.exit(f"dj-shortwalk: An unexpected error occurred - {e}")

def main():
    """
    This is the Entry point for the script.
    This Parses command-line arguments and calls the run function.
    """
    try:
        if len(sys.argv) < 2:
            sys.exit("dj-shortwalk: No command provided. Usage: script.py <command> [arguments...]")
        run(*sys.argv[1:])
    except Exception as e:
        sys.exit(f"dj-shortwalk: An error occurred in main - {e}")

if __name__ == '__main__':
    main()
