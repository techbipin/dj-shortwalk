import os
import sys
import pathlib
import subprocess
from pathlib import Path

KEYS = {
    # General Management Commands
    'h': 'help',
    'c': 'collectstatic',
    'fs': 'findstatic',
    'ck': 'check',
    'gsk': 'generate_secret_key',
    'r': 'runserver',
    'r+': 'runserver_plus',
    'sp': 'startproject',
    'sa': 'startapp',
    't': 'test',

    # Database Management
    'm': 'migrate',
    'mm': 'makemigrations',
    'sm': 'schemamigration',
    'dm': 'datamigration',
    'db': 'dbshell',
    's': 'shell',
    's+': 'shell_plus',
    'gm': 'graph_models',
    'sqlm': 'sqlmigrate',
    'i': 'inspectdb',
    'sd': 'syncdb',
    'rdb': 'reset_db',
    'f': 'flush',
    'sf': 'sqlflush',
    'ssr': 'sqlsequencereset',
    'dd': 'dumpdata',
    'ld': 'loaddata',
    'sall': 'sqlall',
    'ssr': 'sqlsequencereset',

    # Debugging and Utility Commands
    'dc': 'diffsettings',
    'sd': 'sendtestemail',
    'cm': 'check --deploy',
    'vp': 'viewsettings',

    # User Management & Security Mechanism
    'csu': 'createsuperuser',
    'cpw': 'changepassword',
    'cs': 'clearsessions',

    # Development Specific
    'ro': 'runserver --noreload',
    'rd': 'runserver --debugger',
}

script_path = pathlib.Path.cwd()

def find_manage_py():
    first_manage_py_check = script_path / 'manage.py'
    
    if first_manage_py_check.exists():
        return first_manage_py_check
    else:
        for parent in script_path.parents:
            potential_manage_py = parent / 'manage.py'
            if potential_manage_py.exists():
                return potential_manage_py
    
    return None

def run(command=None, *arguments):
    if not command:
        sys.exit("dj-short-walk: No command provided. Please specify a command.")

    command = KEYS.get(command, command)

    try:
        if command == 'startproject':
            return subprocess.run(["django-admin.py", "startproject", *arguments], check=True)

        manage_py_path = find_manage_py()
        return subprocess.run([sys.executable, str(manage_py_path), command, *arguments], check=True)

    except FileNotFoundError as e:
        sys.exit(f"dj-short-walk: File not found error - {e}")
    except subprocess.CalledProcessError as e:
        sys.exit(f"dj-short-walk: Command execution failed with error - {e}")
    except Exception as e:
        sys.exit(f"dj-short-walk: An unexpected error occurred - {e}")

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("dj-short-walk: No command provided. Usage: script.py <command> [arguments...]")

        run(*sys.argv[1:])
    except Exception as e:
        sys.exit(f"dj-short-walk: An error occurred in main - {e}")

if __name__ == '__main__':
    main()