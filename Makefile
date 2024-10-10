# Переменные
DOCKER_COMPOSE = docker-compose
APP = web

# Запуск контейнеров
up:
	$(DOCKER_COMPOSE) up -d

# Остановка контейнеров
down:
	$(DOCKER_COMPOSE) down

# Просмотр логов
logs:
	$(DOCKER_COMPOSE) logs -f $(APP)

# Создание суперпользователя
createsuperuser:
	$(DOCKER_COMPOSE) exec $(APP) python manage.py createsuperuser

