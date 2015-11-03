manage = python manage.py
install = pip install

all:
	${install} -r requirements/prod.txt
	echo "y" | bower install
	${manage} migrate
	${manage} collectstatic --noinput
test:
	${manage} test
migrate:
	${manage} migrate
run:
	${manage} runserver
