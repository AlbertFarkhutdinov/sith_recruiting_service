python clean_db.py
python manage.py makemigrations main_app
python manage.py makemigrations sith_app
python manage.py makemigrations recruits_app
python manage.py migrate
python manage.py fill_db
python manage.py runserver
pause