.PHONY: up down logs

deploy:
	@echo "⬇️  Descargando últimos cambios de GitHub..."
	git pull
	
	@echo "🐳 Reconstruyendo contenedores de Docker..."
	docker compose up -d --build
	
	@echo "🗄️  Aplicando migraciones a la base de datos..."
	# Cambia 'worker_python' por el nombre de tu servicio de Python en docker-compose
	# Cambia los datos de la URL por los tuyos (usuario:pass@servicio_db:puerto/bd)
	docker compose exec worker_python yoyo apply --database postgresql://mi_usuario:mi_password@db:5432/weather_db
	
	@echo "✅ ¡Despliegue completado con éxito!"

dev:
	ENVIRONMENT=dev docker compose up -d --remove-orphans

prod:
	ENVIRONMENT=prod docker compose up -d --remove-orphans

down:
	docker compose down
