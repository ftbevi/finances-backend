ARGS = $(filter-out $@,$(MAKECMDGOALS))

build:
	docker-compose build

clean:
	docker-compose kill && docker-compose down --rmi all
	sudo rm -rf data/
	sudo rm -rf statics/

createsuperuser:
	docker-compose run web python manage.py shell -c "from django.contrib.auth.models import User; \
	u, _ = User.objects.get_or_create(email='dev@finances.co'); \
	u.username = 'dev'; \
	u.set_password('finances@#2022'); \
	u.is_superuser = u.is_staff = True; \
	u.save(); \
	print('Superuser: dev / finances@#2022');"

statics:
	docker-compose run --rm web python manage.py collectstatic --noinput

migrate:
	docker-compose run --rm web python manage.py migrate

migrations:
	docker-compose run --rm web python manage.py makemigrations

dbupdate: migrations migrate

dbunaccent:
	docker-compose exec db psql -U finances -c "CREATE EXTENSION IF NOT EXISTS UNACCENT;"

# fixtures:
# 	docker-compose run --rm web python manage.py loaddata finances/store/fixtures/auth.json
# 	docker-compose run --rm web python manage.py loaddata finances/store/fixtures/store.json

# dump:
# 	docker-compose run web python manage.py dumpdata --format=json auth.user > finances/store/fixtures/auth.json
# 	docker-compose run web python manage.py dumpdata --format=json store > finances/store/fixtures/store.json
precommit:
	pre-commit install
	pre-commit autoupdate

lint:
	docker-compose run --rm  web autoflake -i -r --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
	docker-compose run --rm  web isort -rc --atomic --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 .

services:
	docker-compose up -d db

setup: build services dbupdate dbunaccent createsuperuser statics

bash:
	docker-compose run --rm $(ARGS) sh

shell_plus:
	docker-compose run --rm web python manage.py shell_plus

stop:
	docker-compose down --remove-orphans

run:
	docker-compose run --rm --service-ports web python manage.py runserver 0.0.0.0:6600
