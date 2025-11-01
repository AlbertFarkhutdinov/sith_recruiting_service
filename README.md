# sith_recruiting_service

The recruiting service for the Order of the Sith realized on the Django framework

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

This project is implemented on Python 3.13.
It is recommended to run it in its own virtual environment.

Follow these steps to set up the project on your machine.

### 1. Clone the repository
Start by cloning the repository and navigating to the project directory:
```bash
git clone https://github.com/AlbertFarkhutdinov/sith_recruiting_service.git
cd sith_recruiting_service
```

### 2. Set Up a Virtual Environment & Install dependencies

Using a virtual environment is essential for isolating dependencies 
and maintaining a clean development setup. 

`uv` is a fast, modern Python package manager 
that handles both dependency installation and virtual environment creation.

To install `uv`, see [the documentation](https://docs.astral.sh/uv/).

After installing `uv`, install the project dependencies.

```bash
uv sync --frozen
```
This will automatically create a virtual environment 
and install all the packages 
listed in the `pyproject.toml` file within that environment.

`--frozen` allows to run installation without updating the `uv.lock` file.

Instead of checking if the lockfile is up-to-date,
uses the versions in the lockfile as the source of truth.
If the lockfile is missing, uv will exit with an error.
If the `pyproject.toml` includes changes to dependencies 
that have not been included in the lockfile yet,
they will not be present in the environment.

### 3. Add `recruitment/conf/local.conf` file

```aiignore
[main]
SECRET_KEY: some_secret
DEBUG: True
MEDIA_ROOT: media/
STATICFILES_DIRS: static

[db]
DATABASE_ENGINE: django.db.backends.sqlite3
DATABASE_NAME: db.sqlite3

[superuser]:
username: lord
email: dark_lord@sith.ru
password: password
age: 23
first_name: Lord
last_name: Dark
role: S
planet: Dathomir
is_shadow_hand: True
```

### 4. Prepare the Django project

```bash
cd .\src\recruitment\
uv run python clean_db.py
uv run python manage.py makemigrations main_app
uv run python manage.py makemigrations sith_app
uv run python manage.py makemigrations recruits_app
uv run python manage.py migrate
uv run python manage.py fill_db
```

## Usage

You can run the following command in terminal from root directory to start a project:

```bash
uv run python src/recruitment/manage.py runserver
```
	
Now that the server’s running, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your Web browser.  
