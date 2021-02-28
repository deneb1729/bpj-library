db-up:
	docker-compose -f database/database.yml up -d

db-down:
	docker-compose -f database/database.yml down

test-up: db-down
	docker-compose -f database/db_testing.yml up -d

test-down:
	docker-compose -f database/db_testing.yml down

test-run:
	python3 manage.py test --settings library.testing_settings -v 2 --failfast

develop-up: test-down db-up
	python3 manage.py runserver

coverage-html:
	coverage html --omit='*/.virtualenvs/*'

coverage-report:
	coverage report --omit='*/.virtualenvs/*'

coverage-run:
	coverage run --omit='*/.virtualvenvs/*' manage.py test
