.PHONY: deploy dev prod down

include .env
export

deploy:
	git pull
	
	docker compose up -d --build
	
	docker compose exec elt_pipeline yoyo apply -b ./migrations --database postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@db:5432/$(POSTGRES_DB)

dev:
	ENVIRONMENT=dev docker compose up -d --remove-orphans

prod:
	ENVIRONMENT=prod docker compose up -d --remove-orphans

down:
	docker compose down
