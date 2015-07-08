all:
	pip install -r requirements/production.txt
	python manage.py migrate
	python manage.py collectstatic --noinput

test:
	python manage.py test

run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate
