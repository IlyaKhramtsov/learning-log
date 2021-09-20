shell:
	python manage.py shell

migrate:
	python manage.py migrate

run:
	python manage.py runserver

.PHONY: shell migrate run