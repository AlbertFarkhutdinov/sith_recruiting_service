"""The script to remove database and temporary files."""
from os import remove
from pathlib import Path
from shutil import rmtree

PROJECT_DIR = Path(__file__).absolute().parent
DB_PATH = PROJECT_DIR.joinpath('db.sqlite3')
TMP_PATH = PROJECT_DIR.joinpath('tmp')

try:
    remove(DB_PATH)
except FileNotFoundError:
    print('"{0}" is not found.'.format(DB_PATH))
else:
    print('"{0}" is removed.'.format(DB_PATH))

try:
    rmtree(TMP_PATH)
except FileNotFoundError:
    print('"{0}" is not found.'.format(TMP_PATH))
else:
    print('"{0}" is removed.'.format(TMP_PATH))

for app in ('auth_app', ):
    migrations_path = PROJECT_DIR.joinpath(app, 'migrations')
    try:
        rmtree(migrations_path)
    except FileNotFoundError:
        print('"{0}" is not found.'.format(migrations_path))
    else:
        print('"{0}" is removed.'.format(migrations_path))
