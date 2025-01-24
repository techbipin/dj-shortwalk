import os
import sys
import subprocess
from pathlib import Path
from shortcut_keys import KEYS

class DjangoShortwalk:

    def __init__(self):
        self.script_path = os.getcwd()

    def find_manage_py(self):
        for parent in Path(self.script_path).parents:
            potential_manage_py = parent / 'manage.py'
            if potential_manage_py.exists():
                return potential_manage_py

        sys.exit("dj-shortwalk: 'manage.py' not found in this directory or its parents.")

    def run(self, command=None, *arguments):
        if not command:
            sys.exit("dj-shortwalk: No command provided. Please specify a command.")

        command = KEYS.get(command, command)

        try:
            if command == 'startproject':
                return subprocess.run(["django-admin.py", "startproject", *arguments], check=True)

            manage_py_path = self.find_manage_py()

            return subprocess.run([sys.executable, str(manage_py_path), command, *arguments], check=True)

        except FileNotFoundError as e:
            sys.exit(f"dj-shortwalk: File not found error - {e}")
        except subprocess.CalledProcessError as e:
            sys.exit(f"dj-shortwalk: Command execution failed with error - {e}")
        except Exception as e:
            sys.exit(f"dj-shortwalk: An unexpected error occurred - {e}")

class DjangoShortwalkApp:

    @staticmethod
    def main():
        try:
            if len(sys.argv) < 2:
                sys.exit("dj-shortwalk: No command provided. Usage: script.py <command> [arguments...]")

            app = DjangoShortwalk()
            app.run(*sys.argv[1:])
        except Exception as e:
            sys.exit(f"dj-shortwalk: An error occurred in main - {e}")

if __name__ == '__main__':
    DjangoShortwalkApp.main()
