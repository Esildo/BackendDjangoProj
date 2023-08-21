migrate:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate

up:
	docker-compose up

down:
	docker-compose down