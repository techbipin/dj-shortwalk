DJ-ShortWalk
=============

Overview
--------

DJ-ShortWalk is a command-line tool designed to save you time and reduce the repetitive task of typing ``python manage.py`` or ``django-admin.py`` for every Django management command. This tool provides a convenient shortcut to run common Django commands with ease.

Features
--------

- **Simplified Commands**: DJ-ShortWalk creates a ``dj`` command-line utility that serves as a proxy for Django's ``manage.py`` and ``django-admin.py``.
- **Aliases for Common Commands**: Quickly execute standard Django management commands using intuitive shortcuts.
- **Flexible Usage**: Works from any subdirectory of a Django project, enabling you to run commands without navigating to the project root directory.

Installation
------------

DJ-ShortWalk can be easily installed via Python's package manager ``pip``. Once installed, it provides a ``dj`` binary that you can use directly from your terminal.

Usage
-----

Once installed, you can use the ``dj`` command followed by the Django management command or a shortcut.

### Basic Command Format:

::

    $ dj <command or shortcut>

### Example:

You can run commands from any project directory, whether you are at the root of the project or within a subdirectory.

::

    $ cd path/to/project/subdirectory
    $ dj <command or shortcut>

### List of Supported Commands and Shortcuts:
Refer to the project documentation or use the ``dj h (python manage.py help)`` command to see available commands and their respective shortcuts.

License
-------

DJ-ShortWalk is released under the MIT License. See the LICENSE file for more details.


Shortcuts
---------

::

    # General Management Commands
    h - help (Displays help information about Django management commands and their options.)
    c - collectstatic (Collects all static files from apps and places them into a single directory for production use.)
    fs - findstatic (Locates static files in your project’s file system.)
    ck - check (Runs checks for common issues in your project, such as missing migrations or other potential problems.)
    gsk - generate_secret_key (Generates a new secret key for your Django project, often used in settings.)
    r - runserver (Starts Django’s built-in development server to serve the project locally.)
    r+ - runserver_plus (Similar to `runserver`, but with enhanced features like automatic reloading, debugging, and better error reporting. Requires `django-extensions`.)
    sp - startproject (Creates a new Django project with the specified name.)
    sa - startapp (Creates a new Django app within your project, including initial files like models, views, and migrations.)
    t - test (Runs the tests for the project, checking for any failing test cases.)

    # Database Management
    m - migrate (Applies database migrations, updating your database schema to match the models in your code.)
    mm - makemigrations (Creates new migration files based on changes made to models or schema.)
    sm - schemamigration (Deprecated. Creates schema migrations in older Django versions before `makemigrations` was introduced.)
    dm - datamigration (Deprecated. Creates data migration scripts in older Django versions before `makemigrations` was introduced.)
    db - dbshell (Opens the database shell, allowing you to interact directly with your database.)
    s - shell (Starts a Python interactive shell with access to your Django project's settings, models, and database.)
    s+ - shell_plus (Similar to `shell`, but includes additional features like automatic loading of models and other utilities. Requires `django-extensions`.)
    gm - graph_models (Generates a graphical representation (diagram) of your Django models, useful for understanding your database schema. Requires `django-extensions`.)
    sqlm - sqlmigrate (Shows the SQL that will be executed by a given migration.)
    i - inspectdb (Inspects an existing database and generates corresponding Django model definitions.)
    sd - syncdb (Deprecated. Syncs the database with models, previously used before Django 1.7, now replaced by `migrate`.)
    rdb - reset_db (Resets the database by clearing all data and sometimes recreating the schema. Use with caution.)
    f - flush (Resets the database, clearing all data but preserving the schema.)
    sf - sqlflush (Displays the SQL that will be run when flushing the database, removing data but not the schema.)
    ssr - sqlsequencereset (Resets the sequence for all models, useful to reset the primary key auto-increment values.)
    dd - dumpdata (Dumps the entire data from the database into a JSON file, useful for backups or migrations.)
    ld - loaddata (Loads data from a file (usually JSON or XML) into the database.)
    sall - sqlall (Outputs SQL queries for all models in the project.)
    ssr - sqlsequencereset (Resets the sequence for all models' primary keys, often used after clearing data or recreating the database.)

    # Debugging and Utility Commands
    dc - diffsettings (Shows the differences between your current Django settings and the default settings provided by Django.)
    sd - sendtestemail (Sends a test email using the project's email backend configuration to ensure that email sending is working properly.)
    cm - check --deploy (Runs a security and deployment readiness check on your project, verifying best practices for deploying Django securely.)
    vp - viewsettings (Displays the current Django settings in a readable, human-friendly format, helping you review configurations.)

    # User Management & Security Mechanism
    csu - createsuperuser (Creates a new superuser for the Django admin interface, which has all permissions by default.)
    cpw - changepassword (Changes the password for a specific user in the database.)
    cs - clearsessions (Clears expired sessions from the database, freeing up space and improving performance.)

    # Development Specific
    ro - runserver --noreload (Starts the Django development server without automatic reloading of code, useful in certain debugging or performance scenarios.)
    rd - runserver --debugger (Starts the Django development server with the debugger enabled, allowing you to interact with the code on errors.)
