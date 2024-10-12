cd .\recruitment\recruitment\
poetry run python clean_db.py
poetry run python manage.py makemigrations main_app
poetry run python manage.py makemigrations sith_app
poetry run python manage.py makemigrations recruits_app
poetry run python manage.py migrate
poetry run python manage.py fill_db
poetry run python manage.py runserver
pause