db-up:
	docker-compose -f database/database.yml up -d

db-down:
	docker-compose -f database/database.yml down

test-run:
	python3 manage.py test --settings=library.settings_test -v 2

develop-up: test-down db-up
	python3 manage.py runserver

coverage-html:
	coverage html --omit='*/.virtualenvs/*','*/migrations/*'

coverage-report:
	coverage report --omit='*/.virtualenvs/*','*/migrations/*','*/tests/*','*/__init__.py'

coverage-run:
	coverage run --omit='*/.virtualenvs/*' manage.py test

server-up:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

server-create-user:
	python3 manage.py createsuperuser

requirements:
	pipenv lock -r > requirements.txt
