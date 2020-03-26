"""The script for removing database and temporary files"""
from shutil import rmtree
from os import getcwd, remove
from os.path import join

PROJECT_DIR = getcwd()
try:
    remove(join(PROJECT_DIR, 'db.sqlite3'))
except FileNotFoundError:
    pass

try:
    rmtree(join(PROJECT_DIR, 'tmp'))
except FileNotFoundError:
    pass

for app in ('main_app', 'recruits_app', 'sith_app'):
    app_path = join(PROJECT_DIR, app)
    try:
        rmtree(join(app_path, 'migrations'))
    except FileNotFoundError:
        pass
