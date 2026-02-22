# 1. Usamos una versión oficial y ligera de Python
FROM python:3.12-slim

# 2. Variables de entorno recomendadas para Python en Docker
# Evita que Python cree archivos innecesarios (.pyc)
ENV PYTHONDONTWRITEBYTECODE=1 
# Fuerza a que los prints() salgan en la terminal inmediatamente (vital para ver logs de Prefect)
ENV PYTHONUNBUFFERED=1

# 3. Creamos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# 4. TRUCO DE SENIOR: Copiamos los requirements ANTES que el resto del código.
# Esto hace que Docker guarde las librerías en caché. Si modificas tu main.py, 
# Docker no tendrá que volver a descargar todo Prefect o Psycopg2.
COPY requirements.txt .

# 5. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiamos el resto de tu proyecto a la carpeta /app del contenedor
COPY . .

# 7. El comando por defecto a ejecutar (aunque docker-compose lo sobrescribe)
CMD ["python", "-m", "src.extraction.main"]