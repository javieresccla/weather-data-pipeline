.PHONY: up down logs

dev:
	ENVIRONMENT=dev docker compose up -d --remove-orphans

prod:
	ENVIRONMENT=prod docker compose up -d --remove-orphans

down:
	docker compose down
