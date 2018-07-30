init:
	python3 -m venv venv; \
	echo 'source venv/bin/activate' >> .env; \
	echo 'export DATABASE_URL=""' >> .env; \
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt; \

run:
	python3 manage.py -c ../config/local.py runserver

test:
	py.test ./tests

update_deps:
	source ./venv/bin/activate; \
	pip install --upgrade -r requirements.txt; \

fake:
	python -m scripts/seed.py

revision:
	python manage.py db revision --autogenerate;

upgrade:
	python manage.py db upgrade

downgrade:
	python manage.py db downgrade